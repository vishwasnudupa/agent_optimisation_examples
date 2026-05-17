# Micro-Agent Splitting

Split one large agent prompt into smaller specialized agents. Each agent owns a
clear stage and can use a model size appropriate to its job.

Use this for codegen pipelines, firmware workflows, compile-test loops, and
complex automation where one giant prompt becomes confused or slow.

This example runs planner, coder, and tester agents as a simple pipeline.

```powershell
python .\techniques\micro_agent_splitting\agent_example.py
```
