from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class StepResult:
    name: str
    output: Any
    status: str = "ok"
    error: str | None = None

    def as_dict(self) -> dict[str, Any]:
        payload = {"name": self.name, "status": self.status, "output": self.output}
        if self.error:
            payload["error"] = self.error
        return payload


@dataclass
class PipelineTrace:
    final_output: Any
    steps: list[dict[str, Any]] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return {"final_output": self.final_output, "steps": self.steps}


@dataclass
class Step:
    name: str
    handler: Callable[[Any], Any]

    def run(self, value: Any) -> StepResult:
        try:
            return StepResult(name=self.name, output=self.handler(value))
        except Exception as exc:
            return StepResult(name=self.name, output=None, status="failed", error=str(exc))


class Pipeline:
    def __init__(self, steps: list[Step]) -> None:
        self.steps = steps

    def run(self, value: Any) -> PipelineTrace:
        trace: list[dict[str, Any]] = []
        current = value
        for step in self.steps:
            result = step.run(current)
            trace.append(result.as_dict())
            if result.status != "ok":
                return PipelineTrace(final_output=None, steps=trace)
            current = result.output
        return PipelineTrace(final_output=current, steps=trace)


class ParallelFanOut:
    def __init__(self, workers: dict[str, Callable[[Any], Any]]) -> None:
        self.workers = workers

    def run(self, value: Any) -> dict[str, Any]:
        with ThreadPoolExecutor(max_workers=len(self.workers) or 1) as pool:
            futures = {
                name: pool.submit(worker, value)
                for name, worker in self.workers.items()
            }
            return {name: future.result() for name, future in futures.items()}


class ApprovalGate:
    def __init__(self, risky_terms: tuple[str, ...]) -> None:
        self.risky_terms = risky_terms

    def evaluate(self, action: str) -> dict[str, Any]:
        approval_required = any(term in action.lower() for term in self.risky_terms)
        return {
            "action": action,
            "approval_required": approval_required,
            "status": "paused" if approval_required else "approved",
        }


class StateMachine:
    def __init__(self, transitions: dict[str, str], terminal: str) -> None:
        self.transitions = transitions
        self.terminal = terminal

    def run(self, start: str) -> list[str]:
        state = start
        trace = [state]
        while state != self.terminal:
            if state not in self.transitions:
                raise ValueError(f"no transition defined for state: {state}")
            state = self.transitions[state]
            trace.append(state)
        return trace
