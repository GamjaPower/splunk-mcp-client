import os
import sys
from pathlib import Path
from typing import Any, Dict

import pytest
import requests

# Ensure project root on path for direct module imports
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import mcp_client
import mcp_get_indexes
import mcp_ping
import mcp_toollist


class FakeResponse:
    def __init__(self, payload: Dict[str, Any], status_code: int = 200):
        self._payload = payload
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")

    def json(self):
        return self._payload


def test_mcp_ping_posts_expected_payload(monkeypatch):
    endpoint = "https://example.com/services/mcp"
    token = "t0k3n"
    os.environ["MCP_ENDPOINT"] = endpoint
    os.environ["SPLUNK_MCP_TOKEN"] = token

    captured: Dict[str, Any] = {}

    def fake_post(url, headers, json, timeout, verify):
        captured.update({"url": url, "headers": headers, "json": json, "timeout": timeout, "verify": verify})
        return FakeResponse({"result": "pong"})

    monkeypatch.setattr(mcp_client.requests, "post", fake_post)

    result = mcp_ping.mcp_ping()

    assert result == {"result": "pong"}
    assert captured["url"] == endpoint
    assert captured["headers"]["Authorization"] == f"Bearer {token}"
    assert captured["json"]["method"] == "ping"
    assert captured["json"]["params"] == {}
    assert captured["timeout"] == 10
    assert captured["verify"] is False


def test_mcp_toollist_uses_fixed_id(monkeypatch):
    endpoint = "https://example.com/services/mcp"
    token = "tool-token"
    os.environ["MCP_ENDPOINT"] = endpoint
    os.environ["SPLUNK_MCP_TOKEN"] = token

    captured: Dict[str, Any] = {}

    def fake_post(url, headers, json, timeout, verify):
        captured["json"] = json
        return FakeResponse({"result": {"tools": []}})

    monkeypatch.setattr(mcp_client.requests, "post", fake_post)

    result = mcp_toollist.mcp_toollist()

    assert result == {"result": {"tools": []}}
    assert captured["json"]["id"] == "1"
    assert captured["json"]["method"] == "tools/list"
    assert captured["json"]["params"] == {}


def test_mcp_get_indexes_validates_row_limit():
    with pytest.raises(ValueError):
        mcp_get_indexes.mcp_get_indexes(row_limit=0)
    with pytest.raises(ValueError):
        mcp_get_indexes.mcp_get_indexes(row_limit=1001)


def test_mcp_get_indexes_posts_expected_payload(monkeypatch):
    endpoint = "https://example.com/services/mcp"
    token = "idx-token"
    os.environ["MCP_ENDPOINT"] = endpoint
    os.environ["SPLUNK_MCP_TOKEN"] = token

    captured: Dict[str, Any] = {}

    def fake_post(url, headers, json, timeout, verify):
        captured["json"] = json
        return FakeResponse({"result": {"indexes": ["main"]}})

    monkeypatch.setattr(mcp_client.requests, "post", fake_post)

    result = mcp_get_indexes.mcp_get_indexes(row_limit=200, offset=5)

    assert result == {"result": {"indexes": ["main"]}}
    payload = captured["json"]
    assert payload["method"] == "tools/call"
    assert payload["params"]["name"] == "get_indexes"
    assert payload["params"]["arguments"] == {"row_limit": 200, "offset": 5}


def test_mcp_get_indexes_raises_on_error(monkeypatch):
    def fake_post(url, headers, json, timeout, verify):
        return FakeResponse({"error": {"code": 500, "message": "boom"}})

    monkeypatch.setattr(mcp_client.requests, "post", fake_post)

    with pytest.raises(RuntimeError):
        mcp_get_indexes.mcp_get_indexes()
