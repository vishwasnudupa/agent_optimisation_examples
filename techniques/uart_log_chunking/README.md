# UART Log Chunking

Split raw UART logs into semantic chunks before analysis. Chunking prevents
token overflow and keeps crash diagnosis focused.

Use this for firmware boot logs, serial traces, embedded crash reports, and
device diagnostics.

This example splits a UART log stream into boot-session chunks.

```powershell
python .\techniques\uart_log_chunking\agent_example.py
```
