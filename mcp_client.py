"""Shared helpers for calling Splunk MCP over JSON-RPC."""

import os
from typing import Any, Dict, Tuple

import requests
from dotenv import load_dotenv


# Load environment once; individual calls read current env values.
load_dotenv(override=True)

# Silence TLS warnings when using verify=False for Splunk dev endpoints
requests.packages.urllib3.disable_warnings(  # type: ignore[attr-defined]
    category=requests.packages.urllib3.exceptions.InsecureRequestWarning  # type: ignore[attr-defined]
)


def _settings() -> Tuple[str, str]:
    """Return endpoint and token from the current environment."""
    endpoint = os.getenv("MCP_ENDPOINT", "")
    token = os.getenv("SPLUNK_MCP_TOKEN", "")
    return endpoint, token


def post_json(payload: Dict[str, Any], *, timeout: int = 10, verify: bool = False) -> Dict[str, Any]:
    """Send a JSON-RPC payload to MCP and handle common error cases."""
    endpoint, token = _settings()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    response = requests.post(
        endpoint,
        headers=headers,
        json=payload,
        timeout=timeout,
        verify=verify,
    )

    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(f"MCP error: {data['error']}")
    return data
