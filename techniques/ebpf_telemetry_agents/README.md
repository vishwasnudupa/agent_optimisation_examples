# eBPF Telemetry Agents

Normalize kernel or network telemetry into structured events that an agent can
analyze. eBPF streams can expose real production behavior without relying on
guesswork.

Use this for networking diagnostics, syscall tracing, latency analysis, and
production observability.

This example parses a simulated eBPF event into a dictionary.

```powershell
python .\techniques\ebpf_telemetry_agents\agent_example.py
```
