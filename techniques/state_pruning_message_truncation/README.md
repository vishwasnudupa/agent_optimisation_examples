# State Pruning and Message Truncation

Summarize or remove irrelevant old chat history and keep only useful recent
state. This prevents context growth from degrading reasoning.

Use this for long-running debugging agents, repair loops, support chats, and
multi-step workflows.

This example compacts old messages into one summary and keeps the latest turns.

```powershell
python .\techniques\state_pruning_message_truncation\agent_example.py
```
