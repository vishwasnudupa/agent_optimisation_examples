import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, confidence_score, demo_result


def main() -> None:
    agent = Agent(
        "escalation-router-agent",
        "small",
        lambda answer: {
            "draft_answer": answer,
            "confidence": confidence_score(answer),
        },
    )
    result = agent.run("maybe configure retries")
    confidence = result["output"]["confidence"]
    result["output"]["next_model"] = (
        "large-reasoning-model" if confidence < 0.7 else "small-fast-model"
    )
    print(demo_result("Confidence-Based Escalation", "Escalate only on low confidence", result))


if __name__ == "__main__":
    main()
