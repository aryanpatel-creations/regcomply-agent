"""Synchronous wrapper so graph nodes can call the MCP server (runs in FastAPI's worker threads)."""
import json
import anyio
from mcp import Client
import config


def _content(result) -> dict | list:
    if result.is_error:
        raise RuntimeError(result.content[0].text if result.content else "tool error")
    data = result.structured_content
    if data is None:
        return json.loads(result.content[0].text)
    return data.get("result", data)          # list results come wrapped as {"result": [...]}


class BankTools:
    def __init__(self, target=None):
        target = target or config.MCP_URL         # a URL, an MCPServer object, or "inprocess"
        if target == "inprocess":                 # one-container cloud demo: same MCP protocol, no network hop
            from b3_mcp_server import server
            target = server
        self.target = target

    def _call(self, name: str, args: dict):
        async def go():
            async with Client(self.target) as client:
                return await client.call_tool(name, args)
        return _content(anyio.run(go))         # raise errors outside the async block, so they stay readable

    def account_summary(self, customer_id):
        return self._call("get_account_summary", {"customer_id": customer_id})

    def recent_transactions(self, account_id, days):
        return self._call("get_recent_transactions", {"account_id": account_id, "days": days})

    def ticket(self, ticket_id):
        return self._call("get_ticket", {"ticket_id": ticket_id})

    def request_refund(self, **kwargs):
        return self._call("request_refund", kwargs)
