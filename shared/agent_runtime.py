from __future__ import annotations

import hashlib
import json
import queue
import random
import re
import statistics
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable


@dataclass
class AgentResult:
    agent: str
    model: str
    latency_ms: float
    output: Any
    error: str | None = None

    def as_dict(self) -> dict[str, Any]:
        payload = {
            "agent": self.agent,
            "model": self.model,
            "latency_ms": self.latency_ms,
            "output": self.output,
        }
        if self.error:
            payload["error"] = self.error
        return payload


@dataclass
class ValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)


@dataclass
class Agent:
    name: str
    model_size: str
    handler: Callable[[Any], Any]
    retries: int = 0

    def run(self, task: Any) -> Any:
        started = time.perf_counter()
        attempts = 0
        while True:
            try:
                output = self.handler(task)
                elapsed_ms = (time.perf_counter() - started) * 1000
                return AgentResult(
                    agent=self.name,
                    model=self.model_size,
                    latency_ms=round(elapsed_ms, 2),
                    output=output,
                ).as_dict()
            except Exception as exc:
                attempts += 1
                if attempts > self.retries:
                    elapsed_ms = (time.perf_counter() - started) * 1000
                    return AgentResult(
                        agent=self.name,
                        model=self.model_size,
                        latency_ms=round(elapsed_ms, 2),
                        output=None,
                        error=str(exc),
                    ).as_dict()


def demo_result(
    technique: str,
    optimization: str,
    result: Any,
    scenario: str | None = None,
    pipeline_stage: str | None = None,
) -> dict[str, Any]:
    payload = {
        "technique": technique,
        "optimization_used": optimization,
        "result": result,
    }
    if scenario:
        payload["scenario"] = scenario
    if pipeline_stage:
        payload["pipeline_stage"] = pipeline_stage
    return payload


@dataclass
class Telemetry:
    latencies_ms: list[float] = field(default_factory=list)
    errors: int = 0
    cache_hits: int = 0
    cache_misses: int = 0

    def record_latency(self, value: float) -> None:
        self.latencies_ms.append(value)

    def summary(self) -> dict[str, Any]:
        avg = statistics.mean(self.latencies_ms) if self.latencies_ms else 0
        return {
            "calls": len(self.latencies_ms),
            "avg_latency_ms": round(avg, 2),
            "errors": self.errors,
            "cache_hit_ratio": round(
                self.cache_hits / max(1, self.cache_hits + self.cache_misses), 2
            ),
        }


class SimpleCache:
    def __init__(self) -> None:
        self._items: dict[str, Any] = {}

    def get_or_set(self, key: str, factory: Callable[[], Any]) -> tuple[Any, bool]:
        if key in self._items:
            return self._items[key], True
        value = factory()
        self._items[key] = value
        return value, False


def stable_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def semantic_key(text: str) -> str:
    words = sorted(set(re.findall(r"[a-z0-9]+", text.lower())))
    return stable_hash(" ".join(words[:12]))


def validate_required_keys(payload: dict[str, Any], keys: Iterable[str]) -> None:
    missing = [key for key in keys if key not in payload]
    if missing:
        raise ValueError(f"missing required keys: {missing}")


def validate_required_keys_result(
    payload: dict[str, Any], keys: Iterable[str]
) -> ValidationResult:
    missing = [key for key in keys if key not in payload]
    if missing:
        return ValidationResult(valid=False, errors=[f"missing required keys: {missing}"])
    return ValidationResult(valid=True)


def compact_messages(messages: list[str], keep_last: int = 3) -> list[str]:
    if len(messages) <= keep_last:
        return messages
    summary = "Summary: " + " | ".join(message[:36] for message in messages[:-keep_last])
    return [summary, *messages[-keep_last:]]


def route_by_complexity(task: str) -> str:
    hard_terms = {"architect", "debug", "prove", "race", "deadlock", "optimize"}
    words = set(re.findall(r"[a-z]+", task.lower()))
    if len(task.split()) > 18 or words & hard_terms:
        return "large-reasoning-model"
    return "small-fast-model"


def run_pipeline(task: str, agents: list[Agent]) -> str:
    value: Any = task
    trace = []
    for agent in agents:
        response = agent.run(value)
        trace.append(response)
        value = response["output"]
    return {"final_output": value, "trace": trace}


def fake_llm_json(task: str) -> str:
    return json.dumps({"task": task, "priority": "high" if "prod" in task else "normal"})


def event_queue(items: Iterable[str]) -> queue.Queue[str]:
    events: queue.Queue[str] = queue.Queue()
    for item in items:
        events.put(item)
    return events


def confidence_score(answer: str) -> float:
    base = 0.9 if "validated" in answer.lower() else 0.55
    return round(min(0.99, base + random.random() * 0.05), 2)
