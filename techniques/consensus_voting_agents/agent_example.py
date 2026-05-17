from collections import Counter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result


def main() -> None:
    def vote(answers: list[str]) -> dict[str, int | str]:
        winner, votes = Counter(answers).most_common(1)[0]
        return {"winner": winner, "votes": votes}

    agent = Agent("consensus-agent", "medium", vote)
    result = agent.run(["retry with backoff", "retry with backoff", "increase timeout"])
    print(demo_result("Consensus Voting Agents", "Majority vote across attempts", result))


if __name__ == "__main__":
    main()
