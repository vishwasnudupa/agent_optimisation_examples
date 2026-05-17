import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def main() -> None:
    def assemble_memory(task: str) -> dict[str, object]:
        return {
            "short_term": [task],
            "episodic": {"last_debug_session": "uart timeout fixed by baud change"},
            "long_term": {"device_profile": "stm32 networking board"},
        }

    agent = Agent("memory-hierarchy-agent", "small", assemble_memory)
    result = agent.run("debug uart timeout")
    print(demo_result("Multi-Level Memory Hierarchy", "Separate memory by lifetime", result))


if __name__ == "__main__":
    main()
