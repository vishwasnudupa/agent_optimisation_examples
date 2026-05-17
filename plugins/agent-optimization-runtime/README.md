# Agent Optimization Runtime Plugin

This plugin is the realistic companion to the simple examples in `techniques/`.
It shows how to keep deterministic orchestration while replacing toy handlers
with real model providers such as OpenAI, vLLM, LiteLLM, LangGraph, Temporal, or
local model servers.

The plugin is intentionally dependency-light. Provider calls are wrapped behind
interfaces, so you can wire in real SDKs without changing the workflow shape.

## When To Use This Plugin

Use this plugin when you want a production-like agent architecture instead of a
single isolated toy technique.

It is useful for:

- turning the technique demos into a real application runtime
- testing model routing and approval flows
- designing provider adapters for OpenAI, vLLM, LiteLLM, or local models
- showing how LangGraph or Temporal could wrap the workflow
- keeping validation, cache, telemetry, and safety outside the LLM

## Contents

- `.codex-plugin/plugin.json` registers the plugin.
- `skills/optimized-agent-workflows/SKILL.md` tells Codex how to use the plugin.
- `runtime/provider_adapters.py` contains realistic provider adapter stubs.
- `runtime/optimized_workflow.py` contains a production-style optimized agent
  workflow.
- `examples/realistic_workflow_demo.py` runs the workflow with a mock provider.
- `examples/langgraph_shape.py` shows how to split the workflow into LangGraph
  nodes.
- `examples/temporal_shape.py` shows how to split the workflow into Temporal
  activity boundaries.

## Run Demo

From the repository root:

```powershell
python .\plugins\agent-optimization-runtime\examples\realistic_workflow_demo.py
```

The demo runs three tasks:

- a normal firmware debugging task
- the same task again to demonstrate cache reuse
- a production firmware flash task that pauses for human approval

The output includes:

- selected route
- selected model
- cache hit status
- validation status
- telemetry
- approval pause when needed

## How The Runtime Works

The main workflow lives in:

```text
runtime/optimized_workflow.py
```

The workflow follows this order:

1. Check cache.
2. Run guardrails.
3. Route the task with a lightweight router model.
4. Pause for human approval if the route is high risk.
5. Select fast or reasoning model.
6. Call the provider adapter.
7. Validate structured JSON.
8. Store result in cache.
9. Return telemetry.

The provider boundary lives in:

```text
runtime/provider_adapters.py
```

This file contains:

- `ModelRequest`
- `ModelResponse`
- `ModelProvider`
- `MockProvider`
- `OpenAIResponsesProvider`
- `LiteLLMProvider`
- `VLLMProvider`

The non-mock providers use standard-library HTTP calls and expect compatible
JSON APIs. They are optional and require your own endpoint/API key.

## Production Swap

Replace `MockProvider` with:

- OpenAI Responses API adapter
- vLLM HTTP adapter
- LiteLLM gateway adapter
- Local model server adapter
- LangGraph node wrapper
- Temporal activity wrapper

Keep the deterministic router, schema validation, guardrail, cache, telemetry,
and approval gate around the provider call.

## Minimal Integration Pattern

In your own app, create a provider and pass it into the workflow:

```python
from runtime.optimized_workflow import OptimizedAgentWorkflow
from runtime.provider_adapters import MockProvider

workflow = OptimizedAgentWorkflow(provider=MockProvider())
result = workflow.run("Debug UART RX overflow in staging firmware")
print(result)
```

For production, implement the `complete(...)` method on one provider adapter and
return a normalized `ModelResponse`.

For an OpenAI-compatible local/vLLM endpoint, configure `VLLMProvider`. For a
LiteLLM gateway, configure `LiteLLMProvider`. For OpenAI Responses API, configure
`OpenAIResponsesProvider`.

## Where LangGraph Fits

Use `examples/langgraph_shape.py` as a map:

- `route_node`
- `approval_node`
- `model_node`
- `validation_node`

In a real LangGraph app, these become graph nodes. The same rules still apply:
the graph controls transitions; the model only handles reasoning or generation.

## Where Temporal Fits

Use `examples/temporal_shape.py` as a map:

- `route_activity`
- `approval_activity`
- `model_activity`

In a real Temporal app, these become activities inside a durable workflow. This
is useful when approval, retries, timeouts, and long-running execution matter.

## Safe Production Checklist

Before connecting real tools or infrastructure:

- validate every model response against a schema
- block unsafe prompts and tool calls with guardrails
- require HITL approval for production, payment, delete, and firmware flash work
- run generated code only in a sandbox
- record telemetry for latency, cache hits, errors, retries, and model choice
- keep persistent truth in Redis, SQL, vector DB, or workflow state, not only in
  prompt history
