# Human-in-the-Loop

Pause automation for human approval before risky, expensive, destructive, or
irreversible steps.

Use this for production deploys, firmware flashing, payments, deletions, and
security-sensitive operations.

This example detects a risky firmware flashing action and pauses for approval.

```powershell
python .\techniques\human_in_the_loop\agent_example.py
```
