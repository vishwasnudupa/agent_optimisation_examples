import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result

GRAPH = {
    "rx_dma": ["l2_parse"],
    "l2_parse": ["ipv4_route", "drop"],
    "ipv4_route": ["tx_queue"],
}


def walk(start: str) -> list[str]:
    path = [start]
    while GRAPH.get(path[-1]):
        path.append(GRAPH[path[-1]][0])
    return path


def main() -> None:
    agent = Agent("packet-flow-agent", "small", walk)
    result = agent.run("rx_dma")
    print(demo_result("Packet Flow Graph Modeling", "Graph-based packet reasoning", result))


if __name__ == "__main__":
    main()
