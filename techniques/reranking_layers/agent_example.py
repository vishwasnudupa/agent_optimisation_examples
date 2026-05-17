import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def rerank(query: str, chunks: list[str]) -> list[str]:
    terms = set(query.lower().split())
    return sorted(chunks, key=lambda chunk: len(terms & set(chunk.lower().split())), reverse=True)


def main() -> None:
    agent = Agent(
        "reranker-agent",
        "small",
        lambda task: rerank(task["query"], task["chunks"]),
    )
    result = agent.run(
        {"query": "uart register crash", "chunks": ["billing policy", "uart crash overflow register", "network setup"]}
    )
    print(demo_result("Reranking Layers", "Sort retrieved chunks by relevance", result))


if __name__ == "__main__":
    main()
