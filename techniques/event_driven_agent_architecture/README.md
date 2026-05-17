# Event-Driven Agent Architecture

Trigger agents from events or queues instead of polling continuously. This makes
distributed workflows more scalable and reduces idle compute.

Use this with queues, build systems, ticketing systems, deployment events, and
infrastructure automation.

This example processes a small in-memory event queue.

```powershell
python .\techniques\event_driven_agent_architecture\agent_example.py
```
