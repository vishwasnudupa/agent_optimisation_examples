from collections import defaultdict
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def signature(crash: str) -> str:
    return crash.split(":")[0]


def main() -> None:
    def cluster(crashes: list[str]) -> dict[str, list[str]]:
        clusters: dict[str, list[str]] = defaultdict(list)
        for crash in crashes:
            clusters[signature(crash)].append(crash)
        return dict(clusters)

    agent = Agent("crash-clustering-agent", "small", cluster)
    result = agent.run(["HardFault: pc=0x10", "Assert: dma busy", "HardFault: pc=0x20"])
    print(demo_result("Crash Signature Clustering", "Group recurring crash signatures", result))


if __name__ == "__main__":
    main()
