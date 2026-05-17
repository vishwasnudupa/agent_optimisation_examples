import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result

REGISTERS = {
    "USART_CR1": "USART control register 1: enables RX/TX and interrupts.",
    "DMA_CCR": "DMA channel config register: direction, circular mode, priority.",
}


def main() -> None:
    agent = Agent(
        "register-retrieval-agent",
        "small",
        lambda task: [text for name, text in REGISTERS.items() if name in task],
    )
    result = agent.run("debug DMA_CCR circular mode")
    print(demo_result("Register-Aware Retrieval", "Fetch only matching register docs", result))


if __name__ == "__main__":
    main()
