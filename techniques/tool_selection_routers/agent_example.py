import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result

TOOLS = {
    "search": lambda task: f"searched docs for {task}",
    "shell": lambda task: f"ran diagnostic for {task}",
}


def choose_tool(task: str) -> str:
    return "shell" if "ping" in task or "compile" in task else "search"


def main() -> None:
    def route_and_call(task: str) -> dict[str, str]:
        tool_name = choose_tool(task)
        return {"tool": tool_name, "result": TOOLS[tool_name](task)}

    agent = Agent("tool-router-agent", "small", route_and_call)
    result = agent.run("compile firmware")
    print(demo_result("Tool Selection Routers", "Choose tool before execution", result))


if __name__ == "__main__":
    main()
