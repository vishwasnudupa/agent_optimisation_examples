# Deterministic State Machines

Represent workflow execution as explicit states and transitions. The model can
help decide content, but the allowed path is controlled by code.

Use this for safety-critical flows, retries, firmware flashing, approvals, and
banking or deployment workflows.

This example walks through a fixed `plan -> validate -> execute -> done` graph.

```powershell
python .\techniques\deterministic_state_machines\agent_example.py
```
