# RTOS State Snapshot Compression

Compress repeated RTOS task-state snapshots so long debugging sessions do not
fill the context window with duplicate state.

Use this for embedded tracing, task scheduling analysis, and long-duration
firmware diagnostics.

This example removes consecutive duplicate snapshots.

```powershell
python .\techniques\rtos_state_snapshot_compression\agent_example.py
```
