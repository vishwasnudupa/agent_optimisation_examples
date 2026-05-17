import json
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result, fake_llm_json, validate_required_keys


@dataclass
class RouteDecision:
    task: str
    priority: str


def main() -> None:
    def parse_route(task: str) -> RouteDecision:
        payload = json.loads(fake_llm_json(task))
        validate_required_keys(payload, ["task", "priority"])
        return RouteDecision(**payload)

    agent = Agent("structured-output-agent", "small", parse_route)
    result = agent.run("prod deploy approval")
    print(demo_result("Pydantic Structured Outputs", "Schema-validated routing output", result))


if __name__ == "__main__":
    main()
