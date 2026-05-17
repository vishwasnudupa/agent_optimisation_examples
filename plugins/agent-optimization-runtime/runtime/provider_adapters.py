from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Protocol
from urllib import request as urllib_request
from urllib.error import HTTPError


@dataclass
class ModelRequest:
    model: str
    system: str
    user: str
    response_schema: dict[str, object] | None = None


@dataclass
class ModelResponse:
    model: str
    content: str
    latency_ms: float
    input_tokens: int
    output_tokens: int


class ModelProvider(Protocol):
    def complete(self, request: ModelRequest) -> ModelResponse:
        """Return a model response from OpenAI, vLLM, LiteLLM, or a local server."""


class MockProvider:
    """Deterministic local provider for tests and demos."""

    def complete(self, request: ModelRequest) -> ModelResponse:
        started = time.perf_counter()
        if "route" in request.system.lower():
            payload = {
                "route": "firmware_debug" if "uart" in request.user.lower() else "general",
                "risk": "high" if "production" in request.user.lower() else "low",
                "needs_human_approval": "production" in request.user.lower(),
            }
        elif "repair" in request.system.lower():
            payload = {
                "summary": "UART crash likely caused by RX overflow under interrupt latency.",
                "actions": [
                    "Chunk UART logs by boot session",
                    "Retrieve USART and DMA register context",
                    "Run deterministic validation before firmware flashing",
                ],
            }
        else:
            payload = {"summary": "Task handled", "actions": ["validate output"]}

        content = json.dumps(payload)
        latency_ms = (time.perf_counter() - started) * 1000
        return ModelResponse(
            model=request.model,
            content=content,
            latency_ms=round(latency_ms, 2),
            input_tokens=max(1, len(request.user.split())),
            output_tokens=max(1, len(content.split())),
        )


class OpenAIResponsesProvider:
    """Shape of a real OpenAI adapter.

    Install and wire the official SDK in your app, then implement `complete`.
    Keep this class thin; orchestration belongs in `optimized_workflow.py`.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.openai.com/v1") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def complete(self, request: ModelRequest) -> ModelResponse:
        started = time.perf_counter()
        payload = {
            "model": request.model,
            "input": [
                {"role": "system", "content": request.system},
                {"role": "user", "content": request.user},
            ],
        }
        if request.response_schema:
            payload["text"] = {"format": {"type": "json_object"}}
        data = _post_json(f"{self.base_url}/responses", payload, self.api_key)
        content = _extract_responses_text(data)
        return ModelResponse(
            model=request.model,
            content=content,
            latency_ms=round((time.perf_counter() - started) * 1000, 2),
            input_tokens=data.get("usage", {}).get("input_tokens", 0),
            output_tokens=data.get("usage", {}).get("output_tokens", 0),
        )


class LiteLLMProvider:
    """Shape of a LiteLLM gateway adapter."""

    def __init__(self, gateway_url: str, api_key: str) -> None:
        self.gateway_url = gateway_url
        self.api_key = api_key

    def complete(self, request: ModelRequest) -> ModelResponse:
        return _complete_chat_compatible(
            base_url=self.gateway_url,
            api_key=self.api_key,
            request=request,
        )


class VLLMProvider:
    """Shape of a vLLM OpenAI-compatible HTTP adapter."""

    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        self.base_url = base_url
        self.api_key = api_key

    def complete(self, request: ModelRequest) -> ModelResponse:
        return _complete_chat_compatible(
            base_url=self.base_url,
            api_key=self.api_key,
            request=request,
        )


def _complete_chat_compatible(
    base_url: str,
    api_key: str | None,
    request: ModelRequest,
) -> ModelResponse:
    started = time.perf_counter()
    payload: dict[str, object] = {
        "model": request.model,
        "messages": [
            {"role": "system", "content": request.system},
            {"role": "user", "content": request.user},
        ],
    }
    if request.response_schema:
        payload["response_format"] = {"type": "json_object"}
    data = _post_json(f"{base_url.rstrip('/')}/chat/completions", payload, api_key)
    content = data["choices"][0]["message"]["content"]
    usage = data.get("usage", {})
    return ModelResponse(
        model=request.model,
        content=content,
        latency_ms=round((time.perf_counter() - started) * 1000, 2),
        input_tokens=usage.get("prompt_tokens", 0),
        output_tokens=usage.get("completion_tokens", 0),
    )


def _post_json(url: str, payload: dict[str, object], api_key: str | None) -> dict[str, object]:
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = urllib_request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib_request.urlopen(req, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"provider request failed: {exc.code} {body}") from exc


def _extract_responses_text(data: dict[str, object]) -> str:
    if "output_text" in data:
        return str(data["output_text"])
    for item in data.get("output", []):
        if not isinstance(item, dict):
            continue
        for content in item.get("content", []):
            if isinstance(content, dict) and "text" in content:
                return str(content["text"])
    raise ValueError("could not extract text from Responses API payload")
