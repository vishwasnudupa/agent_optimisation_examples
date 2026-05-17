---
name: optimized-agent-workflows
description: Build realistic production-style agent workflows using provider adapters, deterministic routing, schema validation, cache, telemetry, guardrails, and human approval gates.
---

# Optimized Agent Workflows

Use this plugin when the user wants a realistic production version of the
optimization demos, especially when they mention OpenAI, vLLM, LiteLLM,
LangGraph, Temporal, local models, routing, validation, caching, or agent
orchestration.

## Workflow

1. Keep model calls behind a provider adapter.
2. Use a deterministic router before selecting a model or tool.
3. Validate structured model output before state updates or tool execution.
4. Add guardrails before external actions.
5. Cache stable or repeated requests.
6. Record telemetry for latency, cache hits, model choice, and validation errors.
7. Pause for human approval before destructive or production-impacting actions.

## Files

- `../../runtime/provider_adapters.py` has provider adapter interfaces and mock
  production adapters.
- `../../runtime/optimized_workflow.py` has the reusable optimized workflow.
- `../../examples/realistic_workflow_demo.py` is the runnable example.

## Guidance

For real deployments, replace the mock provider with an SDK-backed adapter, but
do not remove the deterministic orchestration around it. The provider should
only generate or reason; code should decide routing, validation, retries,
approval, caching, and final state transitions.
