import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def normalize_event(raw: str) -> dict[str, str]:
    pid, syscall, latency = raw.split()
    return {"pid": pid, "syscall": syscall, "latency_ms": latency}


def main() -> None:
    agent = Agent("ebpf-normalizer-agent", "small", normalize_event)
    result = agent.run("4242 tcp_sendmsg 7")
    print(demo_result("eBPF Telemetry Agents", "Normalize kernel telemetry events", result))


if __name__ == "__main__":
    main()
