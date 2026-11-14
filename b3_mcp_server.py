"""MCP server for the mock bank: read-only tools, plus one write tool that needs a human approval token.

Run:  python b3_mcp_server.py        (serves Streamable HTTP at http://localhost:8001/mcp)
Uses the official MCP Python SDK v2 (pip install "mcp>=2"), where FastMCP is now called MCPServer.
"""
import hashlib, hmac, sqlite3, uuid
from typing import Any
from datetime import date, timedelta
from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
import config

server = MCPServer("mock-core-banking", instructions="Read-only banking data. Refunds need an approval token.")


def db():
    con = sqlite3.connect(config.BANK_DB)
    con.row_factory = sqlite3.Row
    return con


def rows(sql: str, *args) -> list[dict]:
    with db() as con:
        return [dict(r) for r in con.execute(sql, args)]


# ---------- read-only tools (least privilege: the agent can look, not change) ----------
@server.tool()
def get_account_summary(customer_id: str) -> dict[str, Any]:
    """Account type, status and balance for a customer. No name or contact details are returned."""
    acc = rows("SELECT account_id, type, status, balance_inr FROM accounts WHERE customer_id = ?", customer_id)
    if not acc:
        raise ToolError(f"No account for customer {customer_id}")
    return acc[0]


@server.tool()
def get_recent_transactions(account_id: str, days: int = 30) -> list[dict[str, Any]]:
    """Transactions in the last N days (max 90), newest first."""
    days = max(1, min(days, 90))
    since = str(date(2026, 11, 1) - timedelta(days=days))      # fixed 'today' so results are repeatable
    return rows("SELECT txn_id, txn_date, description, amount_inr, channel FROM transactions "
                "WHERE account_id = ? AND txn_date >= ? ORDER BY txn_date DESC", account_id, since)


@server.tool()
def get_ticket(ticket_id: str) -> dict[str, Any]:
    """Status, category and team of a complaint ticket."""
    t = rows("SELECT * FROM tickets WHERE ticket_id = ?", ticket_id)
    if not t:
        raise ToolError(f"Ticket {ticket_id} not found")
    return t[0]


# ---------- one write tool, gated behind a human approval token ----------
def approval_token(ticket_id: str, amount_inr: float) -> str:
    """Issued only by the human-review step in the API, never by the model."""
    msg = f"{ticket_id}:{amount_inr:.2f}".encode()
    return hmac.new(config.APPROVAL_SECRET.encode(), msg, hashlib.sha256).hexdigest()[:20]


@server.tool()
def request_refund(ticket_id: str, amount_inr: float, reason: str,
                   approval_token_value: str, approved_by: str) -> dict[str, Any]:
    """Record an approved refund request. Fails without a valid approval token. Safe to retry (idempotent)."""
    if not hmac.compare_digest(approval_token_value, approval_token(ticket_id, amount_inr)):
        raise ToolError("Refund refused: missing or invalid approval token")
    if amount_inr <= 0 or amount_inr > 100000:
        raise ToolError("Refund amount outside allowed range")
    existing = rows("SELECT * FROM refund_requests WHERE ticket_id = ? AND amount_inr = ?", ticket_id, amount_inr)
    if existing:
        return existing[0] | {"note": "already recorded"}
    rid = f"R{uuid.uuid4().hex[:8].upper()}"
    with db() as con:
        con.execute("INSERT INTO refund_requests VALUES (?,?,?,?,?,?,?)",
                    (rid, ticket_id, amount_inr, reason, "APPROVED_PENDING_PAYMENT", approved_by,
                     str(date.today())))
    return rows("SELECT * FROM refund_requests WHERE request_id = ?", rid)[0]


if __name__ == "__main__":
    server.run("streamable-http", host="0.0.0.0", port=8001)
