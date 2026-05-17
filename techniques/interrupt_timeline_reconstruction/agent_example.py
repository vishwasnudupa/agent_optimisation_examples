import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def main() -> None:
    agent = Agent(
        "interrupt-timeline-agent",
        "small",
        lambda logs: sorted(logs, key=lambda item: item[0]),
    )
    result = agent.run([(10, "ISR_ENTER uart"), (14, "ISR_EXIT uart"), (12, "ISR_ENTER dma")])
    print(demo_result("Interrupt Timeline Reconstruction", "Chronological ISR trace", result))


if __name__ == "__main__":
    main()
