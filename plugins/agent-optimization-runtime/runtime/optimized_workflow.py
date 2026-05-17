from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, field
from typing import Any

from provider_adapters import ModelProvider, ModelRequest


@dataclass
class WorkflowConfig:
    router_model: str = "small-router-model"
    reasoning_model: str = "large-reasoning-model"
    fast_model: str = "small-fast-model"
    high_risk_terms: tuple[str, ...] = ("production", "delete", "flash", "payment")


@dataclass
class WorkflowTelemetry:
    calls: int = 0
    cache_hits: int = 0
    validation_errors: int = 0
    model_latency_ms: list[float] = field(default_factory=list)

    def record_model_call(self, latency_ms: float) -> None:
        self.calls += 1
        self.model_latency_ms.append(latency_ms)

    def as_dict(self) -> dict[str, Any]:
        avg = sum(self.model_latency_ms) / max(1, len(self.model_latency_ms))
        return {
            "calls": self.calls,
            "cache_hits": self.cache_hits,
            "validation_errors": self.validation_errors,
            "avg_model_latency_ms": round(avg, 2),
        }


class ResponseCache:
    def __init__(self) -> None:
        self._items: dict[str, dict[str, Any]] = {}

    def key(self, task: str) -> str:
        normalized = " ".join(sorted(set(task.lower().split())))
        return hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]

    def get(self, task: str) -> dict[str, Any] | None:
        return self._items.get(self.key(task))

    def set(self, task: str, value: dict[str, Any]) -> None:
        self._items[self.key(task)] = value


class OptimizedAgentWorkflow:
    def __init__(
        self,
        provider: ModelProvider,
        config: WorkflowConfig | None = None,
        cache: ResponseCache | None = None,
    ) -> None:
        self.provider = provider
        self.config = config or WorkflowConfig()
        self.cache = cache or ResponseCache()
        self.telemetry = WorkflowTelemetry()

    def run(self, task: str) -> dict[str, Any]:
        started = time.perf_counter()
        cached = self.cache.get(task)
        if cached:
            self.telemetry.cache_hits += 1
            return {**cached, "cache_hit": True, "telemetry": self.telemetry.as_dict()}

        self._guardrail(task)
        route = self._route(task)
        if route["needs_human_approval"]:
            result = {
                "status": "paused_for_approval",
                "route": route,
                "reason": "Human approval required for high-risk action.",
            }
            self.cache.set(task, result)
            return {**result, "cache_hit": False, "telemetry": self.telemetry.as_dict()}

        model = self.config.reasoning_model if route["risk"] == "high" else self.config.fast_model
        response = self.provider.complete(
            ModelRequest(
                model=model,
                system="Repair or complete the task. Return JSON with summary and actions.",
                user=task,
                response_schema={
                    "type": "object",
                    "required": ["summary", "actions"],
                },
            )
        )
        self.telemetry.record_model_call(response.latency_ms)
        payload = self._validate_json(response.content, ["summary", "actions"])

        result = {
            "status": "completed",
            "route": route,
            "model": response.model,
            "summary": payload["summary"],
            "actions": payload["actions"],
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 2),
        }
        self.cache.set(task, result)
        return {**result, "cache_hit": False, "telemetry": self.telemetry.as_dict()}

    def _route(self, task: str) -> dict[str, Any]:
        response = self.provider.complete(
            ModelRequest(
                model=self.config.router_model,
                system="Route the task. Return JSON with route, risk, needs_human_approval.",
                user=task,
                response_schema={
                    "type": "object",
                    "required": ["route", "risk", "needs_human_approval"],
                },
            )
        )
        self.telemetry.record_model_call(response.latency_ms)
        return self._validate_json(response.content, ["route", "risk", "needs_human_approval"])

    def _guardrail(self, task: str) -> None:
        blocked_terms = ("exfiltrate", "disable audit", "steal secret")
        lowered = task.lower()
        if any(term in lowered for term in blocked_terms):
            raise PermissionError("Task blocked by guardrail policy.")

    def _validate_json(self, content: str, required: list[str]) -> dict[str, Any]:
        try:
            payload = json.loads(content)
            missing = [key for key in required if key not in payload]
            if missing:
                raise ValueError(f"missing required fields: {missing}")
            return payload
        except Exception:
            self.telemetry.validation_errors += 1
            raise
