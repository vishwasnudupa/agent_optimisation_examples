import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def chunk_uart_log(lines: list[str]) -> list[list[str]]:
    chunks: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if "BOOT" in line and current:
            chunks.append(current)
            current = []
        current.append(line)
    if current:
        chunks.append(current)
    return chunks


def main() -> None:
    agent = Agent("uart-log-chunking-agent", "small", chunk_uart_log)
    result = agent.run(["BOOT", "init ok", "FAULT rx overflow", "BOOT", "init ok"])
    print(demo_result("UART Log Chunking", "Split UART stream into semantic chunks", result))


if __name__ == "__main__":
    main()
