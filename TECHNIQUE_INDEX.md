# Technique Index

This file is generated from the technique folder READMEs.

| Technique | Description |
| --- | --- |
| `adaptive_context_injection` | Dynamically inject only the memory, documentation, or state that is relevant to the current task. This keeps prompts focused and avoids distracting the model with unrelated history. |
| `build_artifact_fingerprinting` | Create stable hashes for build inputs such as source files, flags, board configuration, and dependency versions. The fingerprint tells the workflow when an artifact is already current and when it must be rebuilt. |
| `compiler_feedback_grounding` | Feed exact compiler or runtime errors back into the repair step instead of asking the model to guess what happened. Deterministic error text gives the agent a concrete target. |
| `confidence_based_escalation` | Start with a cheap or fast model, then escalate only when confidence is low. This reduces cost while preserving quality for uncertain tasks. |
| `consensus_voting_agents` | Run multiple independent agents or attempts, then choose the answer with the strongest agreement. This improves robustness when single runs are unstable. |
| `crash_signature_clustering` | Group repeated crashes by stable signatures such as exception type, fault code, or top stack frame. Clustering helps agents focus on recurring root causes. |
| `deterministic_state_machines` | Represent workflow execution as explicit states and transitions. The model can help decide content, but the allowed path is controlled by code. |
| `dma_event_summarization` | Convert noisy DMA logs into structured event counts or timelines. This makes low-level debugging easier for agents and humans. |
| `dynamic_model_routing` | Route easy tasks to small fast models and difficult tasks to stronger reasoning models. This reduces latency and cost without forcing every task through the largest model. |
| `ebpf_telemetry_agents` | Normalize kernel or network telemetry into structured events that an agent can analyze. eBPF streams can expose real production behavior without relying on guesswork. |
| `event_driven_agent_architecture` | Trigger agents from events or queues instead of polling continuously. This makes distributed workflows more scalable and reduces idle compute. |
| `few_shot_cot_scratchpads` | Provide a few reasoning examples before the actual task so smaller models can follow a reliable problem-solving pattern. |
| `guardrail_validation_layers` | Check prompts, tool calls, and outputs against policy before execution or release. Guardrails reduce unsafe actions and compliance risk. |
| `hardware_in_the_loop_validation` | Verify generated firmware behavior on real or simulated hardware instead of accepting a model claim that something works. |
| `human_in_the_loop` | Pause automation for human approval before risky, expensive, destructive, or irreversible steps. |
| `incremental_retrieval_progressive_rag` | Retrieve a small amount of context first, then fetch more only if the current evidence is insufficient. This avoids paying for large retrievals on every task. |
| `interrupt_timeline_reconstruction` | Sort ISR and interrupt logs into chronological traces. Timelines help agents reason about latency, priority inversion, and event ordering. |
| `knowledge_distillation_pipelines` | Use outputs from strong models or expert agents to create simpler rules, examples, or datasets for smaller models. |
| `local_validation_grounding` | Validate model outputs with deterministic local code, tests, schemas, or system checks. The runtime result becomes the source of truth. |
| `micro_agent_splitting` | Split one large agent prompt into smaller specialized agents. Each agent owns a clear stage and can use a model size appropriate to its job. |
| `multi_level_memory_hierarchy` | Separate short-term, episodic, and long-term memory instead of putting all context into every prompt. |
| `packet_flow_graph_modeling` | Represent packet processing as graph state rather than loose prose. This helps agents reason deterministically through L2/L3 pipelines. |
| `parallel_agent_fan_out` | Run independent subtasks concurrently to reduce wall-clock time. Parallelism is often the biggest latency win in agent systems. |
| `prompt_caching_layouts` | Put stable, repeated context at the beginning of prompts so providers or local caches can reuse it across calls. |
| `pydantic_structured_outputs` | Force model output into a known schema before using it in routers, tools, state updates, or configuration generation. |
| `reflection_loops` | Let an agent critique and repair its own output in bounded iterations. The loop should have clear stopping conditions and external validation when possible. |
| `register_aware_retrieval` | Retrieve only the hardware register definitions relevant to the current firmware task instead of injecting an entire manual. |
| `reranking_layers` | Add a reranking step after broad retrieval so the most relevant chunks reach the model first. |
| `retrieval_compression` | Compress retrieved documents before injecting them into context. This keeps large RAG workflows cheaper and reduces irrelevant detail. |
| `rtos_state_snapshot_compression` | Compress repeated RTOS task-state snapshots so long debugging sessions do not fill the context window with duplicate state. |
| `runtime_telemetry_feedback` | Capture latency, error, retry, cache, and utilization metrics, then feed those signals back into orchestration decisions. |
| `sandbox_execution_isolation` | Run generated or untrusted code in an isolated environment rather than on the host machine. |
| `semantic_caching` | Cache responses for prompts that are semantically similar, not just identical. This can greatly reduce latency and cost for repeated support-style requests. |
| `speculative_decoding_pipelines` | Use a small fast model to draft tokens while a larger model verifies or corrects the draft. In real serving stacks, this reduces generation latency. |
| `state_pruning_message_truncation` | Summarize or remove irrelevant old chat history and keep only useful recent state. This prevents context growth from degrading reasoning. |
| `static_prompt_chaining` | Use a fixed linear pipeline when the workflow does not need dynamic branching. This is faster and easier to reason about than autonomous planning. |
| `tool_selection_routers` | Use a lightweight router to select the right tool before invoking expensive or state-changing operations. |
| `tree_of_thought_execution` | Explore multiple candidate reasoning paths before choosing one. This improves planning quality when a single direct answer often fails. |
| `uart_log_chunking` | Split raw UART logs into semantic chunks before analysis. Chunking prevents token overflow and keeps crash diagnosis focused. |
