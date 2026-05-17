import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, compact_messages, demo_result


def main() -> None:
    messages = [f"debug turn {i}: noisy logs and tool output" for i in range(1, 8)]
    agent = Agent("state-pruning-agent", "small", lambda state: compact_messages(state, keep_last=3))
    result = agent.run(messages)
    print(demo_result("State Pruning and Message Truncation", "Summarize old state", result))


if __name__ == "__main__":
    main()
