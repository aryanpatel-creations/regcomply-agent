"""Integration tests: talk to the MCP server in-process, exactly as an agent would."""
import anyio, pytest
import config

@pytest.fixture(autouse=True)
def fresh_bank(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "BANK_DB", str(tmp_path / "bank.db"))
    import b3_mock_bank
    b3_mock_bank.build(config.BANK_DB)

def call(tool, args):
    from mcp import Client
    from b3_mcp_server import server
    async def go():
        async with Client(server) as client:
            return await client.call_tool(tool, args)
    return anyio.run(go)

def test_lists_four_tools():
    from mcp import Client
    from b3_mcp_server import server
    async def go():
        async with Client(server) as client:
            return [t.name for t in (await client.list_tools()).tools]
    assert sorted(anyio.run(go)) == ["get_account_summary", "get_recent_transactions",
                                     "get_ticket", "request_refund"]

def test_read_only_tool_returns_data():
    res = call("get_account_summary", {"customer_id": "C0001"})
    assert not res.is_error and res.structured_content["account_id"] == "A0001"

def test_unknown_customer_is_an_error_not_a_crash():
    assert call("get_account_summary", {"customer_id": "C9999"}).is_error

def test_refund_without_token_is_refused():
    res = call("request_refund", {"ticket_id": "K0001", "amount_inr": 500.0, "reason": "fee reversal",
                                  "approval_token_value": "guess", "approved_by": "agent"})
    assert res.is_error

def test_refund_with_token_is_recorded_once():
    from b3_mcp_server import approval_token
    args = {"ticket_id": "K0001", "amount_inr": 500.0, "reason": "fee reversal",
            "approval_token_value": approval_token("K0001", 500.0), "approved_by": "supervisor.s1"}
    first, second = call("request_refund", args), call("request_refund", args)
    assert not first.is_error and second.structured_content.get("note") == "already recorded"

def test_token_for_one_amount_cannot_approve_another():
    from b3_mcp_server import approval_token
    res = call("request_refund", {"ticket_id": "K0001", "amount_inr": 5000.0, "reason": "x",
                                  "approval_token_value": approval_token("K0001", 500.0), "approved_by": "s1"})
    assert res.is_error

def test_bank_tools_wrapper_used_by_the_agent():
    from agent.tools import BankTools
    from b3_mcp_server import server
    tools = BankTools(target=server)
    acc = tools.account_summary("C0002")
    txns = tools.recent_transactions(acc["account_id"], 30)
    assert acc["account_id"] == "A0002" and isinstance(txns, list) and all("amount_inr" in t for t in txns)
    with pytest.raises(RuntimeError):
        tools.ticket("K9999")

def test_inprocess_mode_for_one_container_deploys():
    from agent.tools import BankTools
    assert BankTools("inprocess").account_summary("C0003")["account_id"] == "A0003"
