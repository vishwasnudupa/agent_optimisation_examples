import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def sandbox_command(command: str) -> list[str]:
    return ["docker", "run", "--rm", "--network=none", "agent-sandbox", command]


def main() -> None:
    agent = Agent("sandbox-execution-agent", "small", sandbox_command)
    result = agent.run("python generated_code.py")
    print(demo_result("Sandbox Execution Isolation", "Wrap generated code in isolated runtime", result))


if __name__ == "__main__":
    main()
