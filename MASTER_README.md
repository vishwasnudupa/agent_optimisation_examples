# Master Project Guide

This file is the complete navigation guide for the Enterprise Agentic Workflow
Optimization Examples project. Start here when you want to understand the whole
directory, choose a technique, run examples, or move from demos to a realistic
agent runtime.

## Project Purpose

This repository teaches how to build better agent systems using production
optimization patterns:

- split large workflows into specialized agents
- route tasks to the right model
- validate model output with code
- control context size
- cache repeated work
- run independent work in parallel
- pause risky actions for human approval
- isolate generated code
- collect telemetry and improve over time

The project has two layers:

1. `techniques/`: small runnable examples, one folder per optimization.
2. `plugins/agent-optimization-runtime/`: a realistic plugin-style runtime that
   shows how these ideas fit into a production architecture.

## Quick Commands

Run every technique demo:

```powershell
python .\scripts\run_all.py
```

Run one technique:

```powershell
python .\techniques\micro_agent_splitting\agent_example.py
```

Run the realistic plugin workflow:

```powershell
python .\plugins\agent-optimization-runtime\examples\realistic_workflow_demo.py
```

## Full Directory View

```text
agent optimisation/
├── README.md
├── MASTER_README.md
├── GLOSSARY.md
├── TECHNIQUE_INDEX.md
├── agentopt.py
├── pyproject.toml
├── config/
│   └── examples.yaml
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── scripts/
│   └── run_all.py
├── shared/
│   ├── __init__.py
│   ├── agent_runtime.py
│   └── workflow.py
├── tests/
│   ├── __init__.py
│   ├── test_plugin_workflow.py
│   └── test_shared_runtime.py
├── techniques/
│   ├── adaptive_context_injection/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── build_artifact_fingerprinting/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── compiler_feedback_grounding/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── confidence_based_escalation/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── consensus_voting_agents/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── crash_signature_clustering/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── deterministic_state_machines/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── dma_event_summarization/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── dynamic_model_routing/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── ebpf_telemetry_agents/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── event_driven_agent_architecture/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── few_shot_cot_scratchpads/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── guardrail_validation_layers/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── hardware_in_the_loop_validation/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── human_in_the_loop/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── incremental_retrieval_progressive_rag/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── interrupt_timeline_reconstruction/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── knowledge_distillation_pipelines/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── local_validation_grounding/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── micro_agent_splitting/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── multi_level_memory_hierarchy/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── packet_flow_graph_modeling/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── parallel_agent_fan_out/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── prompt_caching_layouts/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── pydantic_structured_outputs/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── reflection_loops/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── register_aware_retrieval/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── reranking_layers/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── retrieval_compression/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── rtos_state_snapshot_compression/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── runtime_telemetry_feedback/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── sandbox_execution_isolation/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── semantic_caching/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── speculative_decoding_pipelines/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── state_pruning_message_truncation/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── static_prompt_chaining/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── tool_selection_routers/
│   │   ├── README.md
│   │   └── agent_example.py
│   ├── tree_of_thought_execution/
│   │   ├── README.md
│   │   └── agent_example.py
│   └── uart_log_chunking/
│       ├── README.md
│       └── agent_example.py
└── plugins/
    └── agent-optimization-runtime/
        ├── README.md
        ├── .codex-plugin/
        │   └── plugin.json
        ├── skills/
        │   └── optimized-agent-workflows/
        │       └── SKILL.md
        ├── runtime/
        │   ├── __init__.py
        │   ├── optimized_workflow.py
        │   └── provider_adapters.py
        └── examples/
            ├── langgraph_shape.py
            ├── realistic_workflow_demo.py
            └── temporal_shape.py
```

## How To Navigate

Use `README.md` for the quick overview and day-to-day commands.

Use this `MASTER_README.md` when you want the complete project map.

Use `GLOSSARY.md` when a concept, tool, or acronym is unfamiliar.

Use each technique folder's local `README.md` when you want a focused
explanation of one optimization.

Use `plugins/agent-optimization-runtime/README.md` when you want the realistic
production-style implementation.

## Core Code Files

### `shared/agent_runtime.py`

This is the small teaching runtime used by all technique examples.

Important objects:

- `Agent`: wraps a handler and returns structured output with agent name, model
  tier, latency, and result.
- `AgentResult`: typed result object for agent execution.
- `ValidationResult`: typed result object for validation helpers.
- `demo_result`: standard output wrapper for each example.
- `Telemetry`: records calls, latency, cache hits, and errors.
- `SimpleCache`: tiny in-memory cache.
- `route_by_complexity`: simple dynamic model routing helper.
- `compact_messages`: state pruning helper.
- `validate_required_keys`: schema validation helper.

### `scripts/run_all.py`

Discovers and runs every `techniques/*/agent_example.py` file. Use this after
changes to make sure all examples still work.

### `shared/workflow.py`

Reusable workflow primitives:

- `Step`
- `Pipeline`
- `ParallelFanOut`
- `ApprovalGate`
- `StateMachine`

These are useful when moving from one-off examples to real orchestration code.

### `agentopt.py`

Project CLI:

```powershell
python .\agentopt.py list
python .\agentopt.py run micro_agent_splitting
python .\agentopt.py run-all
python .\agentopt.py explain semantic_caching
python .\agentopt.py plugin-demo
python .\agentopt.py generate-index
```

### `TECHNIQUE_INDEX.md`

Generated index of every technique folder and its short description. Regenerate
it with:

```powershell
python .\agentopt.py generate-index
```

### `plugins/agent-optimization-runtime/runtime/provider_adapters.py`

Defines realistic provider boundaries:

- `ModelRequest`
- `ModelResponse`
- `ModelProvider`
- `MockProvider`
- `OpenAIResponsesProvider`
- `LiteLLMProvider`
- `VLLMProvider`

The mock provider runs locally. The other providers show where real SDK or HTTP
calls belong.

### `plugins/agent-optimization-runtime/runtime/optimized_workflow.py`

Contains the realistic optimized workflow:

1. cache check
2. guardrail check
3. lightweight routing
4. human approval gate
5. model selection
6. provider call
7. JSON validation
8. cache write
9. telemetry output

## Technique Index

| Folder | What it demonstrates |
| --- | --- |
| `adaptive_context_injection` | Inject only relevant memory or context. |
| `build_artifact_fingerprinting` | Hash build inputs to avoid unnecessary rebuilds. |
| `compiler_feedback_grounding` | Repair using exact compiler/runtime errors. |
| `confidence_based_escalation` | Escalate to stronger models only when confidence is low. |
| `consensus_voting_agents` | Use multiple answers and choose the majority result. |
| `crash_signature_clustering` | Group recurring crashes by signature. |
| `deterministic_state_machines` | Control workflow paths with explicit transitions. |
| `dma_event_summarization` | Summarize noisy DMA events into structured counts. |
| `dynamic_model_routing` | Route easy/hard tasks to different model tiers. |
| `ebpf_telemetry_agents` | Normalize kernel/network telemetry for agent analysis. |
| `event_driven_agent_architecture` | Trigger agents from queues/events instead of polling. |
| `few_shot_cot_scratchpads` | Add reasoning examples before hard tasks. |
| `guardrail_validation_layers` | Check policy before execution or output. |
| `hardware_in_the_loop_validation` | Verify generated behavior on real/simulated hardware. |
| `human_in_the_loop` | Pause risky actions for approval. |
| `incremental_retrieval_progressive_rag` | Retrieve more context only when needed. |
| `interrupt_timeline_reconstruction` | Rebuild chronological ISR timelines. |
| `knowledge_distillation_pipelines` | Compress strong-model outputs into smaller-model rules. |
| `local_validation_grounding` | Validate output using deterministic code. |
| `micro_agent_splitting` | Split a big task into specialized agents. |
| `multi_level_memory_hierarchy` | Separate short-term, episodic, and long-term memory. |
| `packet_flow_graph_modeling` | Model packet processing as graph state. |
| `parallel_agent_fan_out` | Run independent subtasks concurrently. |
| `prompt_caching_layouts` | Structure prompts for stable prefix cache reuse. |
| `pydantic_structured_outputs` | Validate model output with schema-like objects. |
| `reflection_loops` | Critique and repair output in a bounded loop. |
| `register_aware_retrieval` | Retrieve only relevant hardware register docs. |
| `reranking_layers` | Sort retrieved chunks by relevance before injection. |
| `retrieval_compression` | Compress retrieved context before prompting. |
| `rtos_state_snapshot_compression` | Remove repeated RTOS state snapshots. |
| `runtime_telemetry_feedback` | Measure latency, cache, and errors for optimization. |
| `sandbox_execution_isolation` | Run generated code in isolated environments. |
| `semantic_caching` | Reuse answers for semantically similar requests. |
| `speculative_decoding_pipelines` | Draft with a small model, verify with a large model. |
| `state_pruning_message_truncation` | Summarize old state and keep recent turns. |
| `static_prompt_chaining` | Use fixed linear pipelines for predictable tasks. |
| `tool_selection_routers` | Choose the correct tool before execution. |
| `tree_of_thought_execution` | Explore and score multiple reasoning paths. |
| `uart_log_chunking` | Split UART logs into semantic chunks. |

## Recommended Study Order

1. `micro_agent_splitting`
2. `pydantic_structured_outputs`
3. `deterministic_state_machines`
4. `local_validation_grounding`
5. `dynamic_model_routing`
6. `prompt_caching_layouts`
7. `state_pruning_message_truncation`
8. `parallel_agent_fan_out`
9. `guardrail_validation_layers`
10. `runtime_telemetry_feedback`
11. `plugins/agent-optimization-runtime`

This path starts with agent structure, adds validation and routing, then moves
into performance, safety, and production architecture.

## Building A Real Agent From This Project

Use the plugin runtime as the base:

```python
from runtime.optimized_workflow import OptimizedAgentWorkflow
from runtime.provider_adapters import MockProvider

workflow = OptimizedAgentWorkflow(provider=MockProvider())
result = workflow.run("Debug UART RX overflow in staging firmware")
print(result)
```

Then replace `MockProvider` with a real provider adapter:

- OpenAI Responses API adapter
- vLLM HTTP adapter
- LiteLLM gateway adapter
- local model server adapter

Keep the workflow code responsible for:

- routing
- validation
- retries
- cache
- telemetry
- human approval
- guardrails
- state transitions

Let the model handle:

- language generation
- reasoning
- summarization
- code repair suggestions
- classification when code rules are insufficient

## Verification

After any change, run:

```powershell
python -m unittest discover -s tests
python .\scripts\run_all.py
python .\plugins\agent-optimization-runtime\examples\realistic_workflow_demo.py
```

Both commands should pass before you treat the project as healthy.
