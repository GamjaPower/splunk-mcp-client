"""List available MCP tools via JSON-RPC 2.0 (`tools/list`)."""

import json

from mcp_client import post_json


def mcp_toollist():
    """Call MCP tools/list to fetch available tools."""
    payload = {
        "jsonrpc": "2.0",
        "id": "1",  # keep a fixed id to match the sample request
        "method": "tools/list",
        "params": {},
    }
    return post_json(payload)


if __name__ == "__main__":
    result = mcp_toollist()
    print("✅ MCP tools/list response")
    print(json.dumps(result, indent=2, ensure_ascii=False))
