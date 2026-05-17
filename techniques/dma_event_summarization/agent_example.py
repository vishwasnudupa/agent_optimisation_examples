import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def summarize_dma(events: list[str]) -> dict[str, int]:
    return {
        "transfer_complete": sum("TC" in event for event in events),
        "transfer_error": sum("TE" in event for event in events),
    }


def main() -> None:
    agent = Agent("dma-summary-agent", "small", summarize_dma)
    result = agent.run(["DMA1 TC ch2", "DMA1 TE ch2", "DMA1 TC ch2"])
    print(demo_result("DMA Event Summarization", "Convert noisy DMA logs to counts", result))


if __name__ == "__main__":
    main()
