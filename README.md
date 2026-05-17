# Enterprise Agentic Workflow Optimization Examples

This project is a practical code companion for the optimization matrix. Each
folder under `techniques/` contains a small runnable Python agent example for
one optimization pattern.

The examples avoid external services and model API calls on purpose. They use a
shared local `Agent` abstraction so you can see the orchestration, validation,
caching, routing, memory, retrieval, telemetry, and safety patterns clearly
before swapping in real LLM clients.

## What You Can Do With This Directory

Use this repository as a learning lab, template library, or starting point for a
production agent system.

- Learn one optimization at a time from `techniques/<technique_name>/`.
- Run all examples to verify the complete project works.
- Copy a technique folder into another project when you need that pattern.
- Use `shared/agent_runtime.py` as the lightweight local teaching runtime.
- Use `plugins/agent-optimization-runtime/` as the more realistic production
  shape with provider adapters, routing, validation, cache, guardrails, HITL,
  and telemetry.

For the complete project map, read `MASTER_README.md`. For definitions of
important words and tools, read `GLOSSARY.md`.

## Quick Start

From the project root:

```powershell
python .\scripts\run_all.py
```

This runs every `techniques/*/agent_example.py` file and reports whether each
demo passed.

Run one technique directly when you want to study a specific optimization:

```powershell
python .\techniques\micro_agent_splitting\agent_example.py
```

Run the realistic plugin-style workflow:

```powershell
python .\plugins\agent-optimization-runtime\examples\realistic_workflow_demo.py
```

Use the CLI:

```powershell
python .\agentopt.py list
python .\agentopt.py run micro_agent_splitting
python .\agentopt.py run-all
python .\agentopt.py explain semantic_caching
python .\agentopt.py plugin-demo
```

## Layout

```text
.
├── README.md
├── pyproject.toml
├── scripts/
│   └── run_all.py
├── shared/
│   ├── agent_runtime.py
│   └── workflow.py
├── tests/
├── techniques/
│   └── <technique_name>/
│       ├── README.md
│       └── agent_example.py
└── plugins/
    └── agent-optimization-runtime/
        ├── .codex-plugin/
        ├── skills/
        ├── runtime/
        └── examples/
```

### `techniques/`

Contains 39 small examples. Each folder has:

- `README.md`: explains the technique, when to use it, and how to run it.
- `agent_example.py`: a runnable mini agent or workflow that demonstrates the
  optimization.

Use these folders when you want to understand or copy one pattern quickly.

### `shared/`

Contains the lightweight local runtime used by the examples:

- `Agent`: wraps a task handler and returns structured output.
- `AgentResult`: typed result object for agent output.
- `SimpleCache`: small cache helper for caching examples.
- `Telemetry`: records latency, errors, and cache hit ratio.
- validators, routing helpers, hashing helpers, and message compaction helpers.
- `workflow.py`: reusable `Pipeline`, `Step`, `ParallelFanOut`,
  `ApprovalGate`, and `StateMachine` primitives.

This is intentionally simple so the optimization logic stays visible.

### `agentopt.py`

Command-line helper for exploring the project:

```powershell
python .\agentopt.py list
python .\agentopt.py run <technique_name>
python .\agentopt.py run-all
python .\agentopt.py explain <technique_name>
python .\agentopt.py plugin-demo
python .\agentopt.py generate-index
```

### `tests/`

Contains standard-library `unittest` coverage for the shared runtime and plugin
workflow.

```powershell
python -m unittest discover -s tests
```

### `plugins/agent-optimization-runtime/`

Contains the realistic production-style version. Use this when you want to move
from toy examples to real architecture.

It demonstrates:

- provider adapters for OpenAI, vLLM, LiteLLM, or local models
- deterministic routing before model selection
- structured JSON validation
- response caching
- guardrail checks
- human approval gates for high-risk work
- runtime telemetry
- LangGraph-style and Temporal-style workflow boundaries

## Replacing Simulated Agents With Real Models

Each example keeps model calls behind a small function or `Agent` object. In a
real system, replace that function with your OpenAI, vLLM, LiteLLM, LangGraph,
Temporal, or local model call while keeping the deterministic orchestration
around it.

For a realistic starting point, use:

```text
plugins/agent-optimization-runtime/runtime/provider_adapters.py
plugins/agent-optimization-runtime/runtime/optimized_workflow.py
```

`provider_adapters.py` defines the model provider boundary. `optimized_workflow.py`
keeps the production rules around the model call.

## Recommended Learning Path

1. Run all examples:

```powershell
python .\scripts\run_all.py
```

2. Open a technique README, for example:

```text
techniques/micro_agent_splitting/README.md
```

3. Run its example:

```powershell
python .\techniques\micro_agent_splitting\agent_example.py
```

4. Compare the small example with the production-style plugin:

```powershell
python .\plugins\agent-optimization-runtime\examples\realistic_workflow_demo.py
```

5. Replace the mock provider with your real model provider.

## How To Build A Good Agent From These Techniques

Start with deterministic workflow control, then add model intelligence only
where it is useful:

1. Use `dynamic_model_routing` or `confidence_based_escalation` to pick the
   right model size.
2. Use `pydantic_structured_outputs` and `local_validation_grounding` before
   trusting model output.
3. Use `state_pruning_message_truncation`, `adaptive_context_injection`, and
   `retrieval_compression` to control context size.
4. Use `prompt_caching_layouts` and `semantic_caching` to reduce latency and
   cost.
5. Use `parallel_agent_fan_out` for independent work.
6. Use `human_in_the_loop`, `guardrail_validation_layers`, and
   `sandbox_execution_isolation` for safety.
7. Use `runtime_telemetry_feedback` to measure and improve the system.

## How To Add A New Technique

Create a new folder under `techniques/`:

```text
techniques/my_new_technique/
├── README.md
└── agent_example.py
```

In `agent_example.py`, import the shared runtime:

```python
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result
```

Then create an `Agent(...)`, run it, and print `demo_result(...)`. After adding
the folder, verify everything:

```powershell
python .\scripts\run_all.py
```

Then regenerate the index:

```powershell
python .\agentopt.py generate-index
```

## Notes

- The project uses only the Python standard library.
- No API keys are required for the local examples.
- The plugin includes realistic adapter shapes, but the real SDK calls are left
  for your production environment. Standard-library HTTP adapters are included
  for OpenAI-compatible endpoints.
- Keep orchestration deterministic: let code handle routing, retries,
  validation, cache, approval, and safety; let the model handle language and
  reasoning.
