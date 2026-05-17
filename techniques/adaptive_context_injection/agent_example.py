import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result

MEMORY = {
    "uart": "UART baud rate is 115200.",
    "dma": "DMA channel 2 owns the network RX ring.",
    "billing": "Invoices are stored in the finance database.",
}


def main() -> None:
    agent = Agent(
        "context-injection-agent",
        "small",
        lambda task: {
            "task": task,
            "injected_context": [value for key, value in MEMORY.items() if key in task],
        },
    )
    result = agent.run("debug dma receive failure")
    print(demo_result("Adaptive Context Injection", "Inject only matching memory", result))


if __name__ == "__main__":
    main()
