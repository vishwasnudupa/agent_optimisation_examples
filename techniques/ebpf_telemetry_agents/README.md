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

## Realistic Scenarios

In production networking, an agent can consume eBPF-derived events for TCP
retransmits, syscall latency, packet drops, queue depth, and kernel path timing.
This gives the agent real runtime evidence instead of relying only on logs.

In a Kubernetes incident, eBPF telemetry can show whether latency is caused by
DNS, network policy, kernel drops, disk I/O, or application code.

Use this when normal app logs are too high-level. eBPF gives observability at
the operating-system and network boundary, where many hard failures hide.

## Pipeline Stage

Use this during **production observability ingestion**, before incident analysis
or automated remediation.

```mermaid
flowchart LR
    A["Kernel/network events"] --> B["eBPF collector"]
    B --> C["Normalize telemetry"]
    C --> D["Correlate with app metrics"]
    D --> E["Incident agent"]
```
