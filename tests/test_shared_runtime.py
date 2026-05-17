from __future__ import annotations

import unittest

from shared.agent_runtime import (
    Agent,
    SimpleCache,
    compact_messages,
    route_by_complexity,
    validate_required_keys_result,
)
from shared.workflow import ApprovalGate, ParallelFanOut, Pipeline, StateMachine, Step


class SharedRuntimeTests(unittest.TestCase):
    def test_agent_returns_structured_result(self) -> None:
        agent = Agent("unit-agent", "small", lambda value: value.upper())
        result = agent.run("ok")
        self.assertEqual(result["agent"], "unit-agent")
        self.assertEqual(result["model"], "small")
        self.assertEqual(result["output"], "OK")

    def test_agent_reports_error_after_retries(self) -> None:
        agent = Agent("failing-agent", "small", lambda _: (_ for _ in ()).throw(ValueError("bad")))
        result = agent.run("task")
        self.assertIsNone(result["output"])
        self.assertIn("bad", result["error"])

    def test_cache_hit_and_miss(self) -> None:
        cache = SimpleCache()
        value, hit = cache.get_or_set("key", lambda: "created")
        self.assertEqual(value, "created")
        self.assertFalse(hit)
        value, hit = cache.get_or_set("key", lambda: "new")
        self.assertEqual(value, "created")
        self.assertTrue(hit)

    def test_routing_and_validation_helpers(self) -> None:
        self.assertEqual(route_by_complexity("format json"), "small-fast-model")
        self.assertEqual(route_by_complexity("debug race condition"), "large-reasoning-model")
        self.assertTrue(validate_required_keys_result({"a": 1}, ["a"]).valid)
        self.assertFalse(validate_required_keys_result({}, ["a"]).valid)

    def test_compact_messages_keeps_recent_state(self) -> None:
        compacted = compact_messages(["one", "two", "three", "four"], keep_last=2)
        self.assertEqual(compacted[-2:], ["three", "four"])
        self.assertTrue(compacted[0].startswith("Summary:"))


class WorkflowPrimitiveTests(unittest.TestCase):
    def test_pipeline_runs_steps(self) -> None:
        pipeline = Pipeline(
            [
                Step("double", lambda value: value * 2),
                Step("add", lambda value: value + 1),
            ]
        )
        result = pipeline.run(2).as_dict()
        self.assertEqual(result["final_output"], 5)
        self.assertEqual(len(result["steps"]), 2)

    def test_parallel_fan_out(self) -> None:
        fan_out = ParallelFanOut(
            {
                "upper": lambda value: value.upper(),
                "length": lambda value: len(value),
            }
        )
        self.assertEqual(fan_out.run("agent"), {"upper": "AGENT", "length": 5})

    def test_approval_gate_and_state_machine(self) -> None:
        gate = ApprovalGate(("production", "delete"))
        self.assertTrue(gate.evaluate("deploy production")["approval_required"])
        machine = StateMachine({"plan": "validate", "validate": "done"}, terminal="done")
        self.assertEqual(machine.run("plan"), ["plan", "validate", "done"])


if __name__ == "__main__":
    unittest.main()
