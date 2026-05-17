import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def retrieve(query: str, depth: int) -> list[str]:
    docs = ["quick answer", "deeper hardware note", "full manual section"]
    return docs[:depth]


def main() -> None:
    def progressive_retrieve(query: str) -> dict[str, object]:
        for depth in [1, 2, 3]:
            docs = retrieve(query, depth)
            if any("hardware" in doc for doc in docs):
                return {"query": query, "depth": depth, "docs": docs}
        return {"query": query, "depth": 3, "docs": docs}

    agent = Agent("progressive-rag-agent", "small", progressive_retrieve)
    result = agent.run("why did uart crash")
    print(demo_result("Incremental Retrieval / Progressive RAG", "Retrieve more only if needed", result))


if __name__ == "__main__":
    main()
