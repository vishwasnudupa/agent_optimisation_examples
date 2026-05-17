from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "plugins" / "agent-optimization-runtime" / "runtime"
sys.path.append(str(RUNTIME))

from optimized_workflow import OptimizedAgentWorkflow
from provider_adapters import MockProvider, ModelRequest, ModelResponse


class MalformedProvider(MockProvider):
    def complete(self, request: ModelRequest) -> ModelResponse:
        if "Repair" in request.system:
            return ModelResponse(
                model=request.model,
                content=json.dumps({"summary": "missing actions"}),
                latency_ms=1.0,
                input_tokens=1,
                output_tokens=1,
            )
        return super().complete(request)


class PluginWorkflowTests(unittest.TestCase):
    def test_completed_task_then_cache_hit(self) -> None:
        workflow = OptimizedAgentWorkflow(provider=MockProvider())
        first = workflow.run("Debug UART RX overflow in staging firmware")
        second = workflow.run("Debug UART RX overflow in staging firmware")
        self.assertEqual(first["status"], "completed")
        self.assertFalse(first["cache_hit"])
        self.assertTrue(second["cache_hit"])
        self.assertEqual(second["telemetry"]["cache_hits"], 1)

    def test_high_risk_task_pauses_for_approval(self) -> None:
        workflow = OptimizedAgentWorkflow(provider=MockProvider())
        result = workflow.run("Prepare production firmware flash plan")
        self.assertEqual(result["status"], "paused_for_approval")
        self.assertTrue(result["route"]["needs_human_approval"])

    def test_guardrail_blocks_unsafe_task(self) -> None:
        workflow = OptimizedAgentWorkflow(provider=MockProvider())
        with self.assertRaises(PermissionError):
            workflow.run("disable audit and steal secret")

    def test_validation_failure_is_counted(self) -> None:
        workflow = OptimizedAgentWorkflow(provider=MalformedProvider())
        with self.assertRaises(ValueError):
            workflow.run("Debug UART RX overflow in staging firmware")
        self.assertEqual(workflow.telemetry.validation_errors, 1)


if __name__ == "__main__":
    unittest.main()
