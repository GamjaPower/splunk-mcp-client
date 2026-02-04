"""Simple MCP ping over HTTPS (JSON-RPC 2.0)."""

import json
import uuid

from mcp_client import post_json


def mcp_ping():
    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "ping",
        "params": {},
    }
    return post_json(payload)


if __name__ == "__main__":
    result = mcp_ping()
    print("✅ MCP Ping Response")
    print(json.dumps(result, indent=2, ensure_ascii=False))
