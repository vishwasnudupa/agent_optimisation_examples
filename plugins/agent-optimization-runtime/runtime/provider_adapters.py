from __future__ import annotations

import json
import time
from dataclasses import dataclass
from typing import Protocol


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

    def __init__(self, client: object) -> None:
        self.client = client

    def complete(self, request: ModelRequest) -> ModelResponse:
        raise NotImplementedError(
            "Wire your OpenAI client here, call the Responses API, and return ModelResponse."
        )


class LiteLLMProvider:
    """Shape of a LiteLLM gateway adapter."""

    def __init__(self, gateway_url: str, api_key: str) -> None:
        self.gateway_url = gateway_url
        self.api_key = api_key

    def complete(self, request: ModelRequest) -> ModelResponse:
        raise NotImplementedError(
            "POST to your LiteLLM gateway and normalize the response into ModelResponse."
        )


class VLLMProvider:
    """Shape of a vLLM OpenAI-compatible HTTP adapter."""

    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        self.base_url = base_url
        self.api_key = api_key

    def complete(self, request: ModelRequest) -> ModelResponse:
        raise NotImplementedError(
            "Call the vLLM OpenAI-compatible endpoint and return ModelResponse."
        )
