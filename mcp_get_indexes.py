"""Fetch Splunk MCP indexes via JSON-RPC 2.0 using the `get_indexes` tool."""

import argparse
import json
import uuid

from mcp_client import post_json


def mcp_get_indexes(row_limit=100, offset=0):
    """Call MCP get_indexes with pagination support."""
    if row_limit < 1 or row_limit > 1000:
        raise ValueError("row_limit must be between 1 and 1000")
    if offset < 0:
        raise ValueError("offset must be non-negative")

    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),
        "method": "tools/call",
        "params": {
            "name": "get_indexes",
            "arguments": {"row_limit": row_limit, "offset": offset},
        },
    }
    return post_json(payload)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Call MCP get_indexes")
    parser.add_argument(
        "--row-limit",
        type=int,
        default=100,
        help="Maximum number of rows to return (1-1000)",
    )
    parser.add_argument(
        "--offset",
        type=int,
        default=0,
        help="Offset for pagination (0+)",
    )
    args = parser.parse_args()

    result = mcp_get_indexes(row_limit=args.row_limit, offset=args.offset)
    print("✅ MCP get_indexes response")
    print(json.dumps(result, indent=2, ensure_ascii=False))
