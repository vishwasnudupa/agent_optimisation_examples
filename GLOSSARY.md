# Glossary

This glossary explains the important concepts, tools, and terms used across the
Enterprise Agentic Workflow Optimization Examples project.

## Agent Concepts

**Agent**

A software unit that receives a task, performs reasoning or action, and returns
a result. In this project, `Agent` is a small wrapper around a Python handler so
each technique looks like an agent workflow.

**Agent workflow**

A sequence or graph of agent steps. A workflow can include routing, model calls,
tool calls, validation, retries, approval gates, and telemetry.

**Micro-agent**

A small specialized agent that handles one stage of a larger workflow, such as
planning, coding, testing, routing, or validation.

**Multi-agent system**

A system where several agents cooperate, split tasks, vote, validate each other,
or run in parallel.

**Router agent**

An agent that chooses the next model, tool, workflow branch, or specialist agent
for a task.

**Tool-using agent**

An agent that can call external tools such as shell commands, APIs, databases,
retrievers, queues, or code execution sandboxes.

**Human-in-the-loop (HITL)**

A checkpoint where automation pauses and waits for human approval before a
risky action.

## Optimization Techniques

**Adaptive context injection**

Adding only the relevant memory or documents to a prompt instead of sending all
available context.

**Build artifact fingerprinting**

Hashing build inputs so the system can detect when a binary or artifact is
already current.

**Compiler feedback grounding**

Using exact compiler, runtime, or test errors as evidence for repair loops.

**Confidence-based escalation**

Starting with a cheap or fast model, then escalating to a stronger model only
when confidence is low.

**Consensus voting**

Running multiple attempts and selecting the answer with the strongest agreement.

**Deterministic state machine**

A workflow where all valid states and transitions are defined in code.

**Dynamic model routing**

Choosing a model based on task difficulty, cost, latency, or risk.

**Event-driven architecture**

A design where agents respond to events from queues or streams instead of
polling repeatedly.

**Few-shot CoT scratchpad**

A prompt section with a few examples of step-by-step reasoning. CoT means
chain-of-thought.

**Guardrail**

A validation or policy layer that blocks unsafe prompts, outputs, or actions.

**Knowledge distillation**

Using outputs from stronger models or experts to train, guide, or simplify
smaller models.

**Local validation grounding**

Checking model output with deterministic code, tests, schemas, compilers, or
runtime commands.

**Parallel fan-out**

Running independent subtasks concurrently to reduce wall-clock latency.

**Prompt caching**

Reusing provider-side or local computation when prompt prefixes are repeated.

**Reflection loop**

A bounded loop where an agent critiques and repairs its own output.

**Reranking**

Sorting retrieved documents after initial search so the most relevant chunks are
sent to the model.

**Retrieval compression**

Summarizing or trimming retrieved content before injecting it into context.

**Semantic caching**

Caching responses for prompts that are similar in meaning, not only identical.

**Speculative decoding**

Using a smaller model to draft output while a larger model verifies or corrects
it.

**State pruning**

Removing or summarizing old state so long workflows do not overload the context
window.

**Static prompt chaining**

A fixed sequence of prompt or agent steps with no dynamic branching.

**Tree-of-thought**

Exploring multiple reasoning paths, scoring them, and selecting the best path.

## Retrieval And Memory

**RAG**

Retrieval-augmented generation. A pattern where documents are retrieved and then
provided to a model as context.

**Progressive RAG**

Retrieving a small amount first, then retrieving more only if the answer needs
more evidence.

**Vector database**

A database that stores embeddings and retrieves semantically similar text.
Examples include Qdrant, Weaviate, and Pinecone.

**Redis**

An in-memory data store often used for caches, queues, and short-term state.

**SQL database**

A relational database used for durable structured truth, records, and workflow
state.

**Short-term memory**

Recent task or conversation state.

**Episodic memory**

Past events or sessions that may be useful later.

**Long-term memory**

Persistent facts, preferences, domain data, or durable state.

## Production Safety

**Sandbox**

An isolated environment for running generated or untrusted code. Examples
include Docker containers and Firecracker microVMs.

**Approval gate**

A workflow step that requires a human to approve before continuing.

**Policy validation**

Checking whether an input, output, or action follows safety, compliance, or
business rules.

**Schema validation**

Checking that structured data contains required fields and expected types.

**Structured output**

Model output constrained to a shape such as JSON with required keys.

**Retry logic**

Rules for repeating failed steps safely, often with limits and backoff.

## Observability And Metrics

**Telemetry**

Runtime measurements such as latency, errors, cache hits, model choice, token
usage, and retry count.

**TTFT**

Time to first token. A responsiveness metric for model streaming.

**Latency**

How long a call or workflow takes to return.

**Cache hit ratio**

The fraction of requests served from cache instead of recomputed.

**Tool failure rate**

How often external tools fail during agent execution.

**Retry loop frequency**

How often tasks require repeated attempts.

**Cost per successful task**

Total inference and tool cost divided by successful completed tasks.

## Firmware And Networking Terms

**UART**

Universal asynchronous receiver-transmitter. A common serial communication
interface used in embedded systems.

**DMA**

Direct memory access. Hardware that moves data without constant CPU
intervention.

**ISR**

Interrupt service routine. Code that runs in response to a hardware or software
interrupt.

**RTOS**

Real-time operating system. An operating system designed for deterministic
timing and embedded tasks.

**Register map**

Documentation describing hardware registers and their bit fields.

**Packet flow graph**

A graph representation of how packets move through RX, parsing, routing,
filtering, and TX stages.

**Hardware-in-the-loop (HIL)**

Testing where software is validated against real or simulated hardware.

**eBPF**

Extended Berkeley Packet Filter. A Linux technology for safe kernel-level
observability and networking instrumentation.

## Tools And Frameworks

**OpenAI Responses API**

An OpenAI API shape for model calls, tool use, multimodal input, and structured
outputs.

**vLLM**

A high-throughput model serving engine often used for self-hosted inference.

**LiteLLM**

A gateway that provides a unified interface to many model providers.

**LangGraph**

A framework for building graph-based agent workflows with explicit state and
transitions.

**Temporal**

A durable workflow engine for long-running, retryable, observable workflows.

**Airflow**

A workflow scheduler often used for data pipelines and batch jobs.

**CrewAI**

A framework for building multi-agent role-based workflows.

**AutoGen**

A framework for multi-agent conversation and collaboration patterns.

**Pydantic**

A Python library for typed data validation. This project uses the idea of
schema validation while keeping examples dependency-free.

**Instructor**

A library that helps enforce structured model outputs using schemas.

**Prometheus**

A metrics collection and monitoring system.

**Grafana**

A dashboarding and observability tool often used with Prometheus.

**Kafka**

A distributed event streaming system.

**RabbitMQ**

A message broker for queue-based communication.

**Docker**

A container runtime used for sandboxing and repeatable execution.

**Firecracker**

A lightweight microVM technology often used for stronger isolation.

## Project-Specific Files

**`shared/agent_runtime.py`**

The local teaching runtime for the small examples.

**`scripts/run_all.py`**

Runs every technique example and reports failures.

**`plugins/agent-optimization-runtime/runtime/provider_adapters.py`**

Defines the boundary between workflow code and real model providers.

**`plugins/agent-optimization-runtime/runtime/optimized_workflow.py`**

Shows a production-style optimized agent workflow with routing, cache,
guardrails, validation, HITL, and telemetry.

**`plugins/agent-optimization-runtime/examples/realistic_workflow_demo.py`**

Runs the realistic workflow using `MockProvider`.
