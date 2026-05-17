import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def compress_document(text: str, max_sentences: int = 2) -> str:
    return ". ".join(text.split(". ")[:max_sentences])


def main() -> None:
    agent = Agent("retrieval-compression-agent", "small", compress_document)
    result = agent.run("DMA channel 1 overflowed. ISR latency was high. More unrelated history. Extra logs.")
    print(demo_result("Retrieval Compression", "Compress retrieved context", result))


if __name__ == "__main__":
    main()
