import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def compress_snapshots(snapshots: list[dict[str, str]]) -> list[dict[str, str]]:
    compressed = []
    previous = None
    for snapshot in snapshots:
        if snapshot != previous:
            compressed.append(snapshot)
        previous = snapshot
    return compressed


def main() -> None:
    snapshots = [
        {"task": "net", "state": "ready"},
        {"task": "net", "state": "ready"},
        {"task": "net", "state": "blocked"},
    ]
    agent = Agent("rtos-compression-agent", "small", compress_snapshots)
    result = agent.run(snapshots)
    print(demo_result("RTOS State Snapshot Compression", "Drop repeated state snapshots", result))


if __name__ == "__main__":
    main()
