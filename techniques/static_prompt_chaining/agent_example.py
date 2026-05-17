import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from shared.agent_runtime import Agent, demo_result, run_pipeline


def main() -> None:
    chain = [
        Agent("transcribe", "small", lambda audio: "customer asked about invoice 42"),
        Agent("summarize", "small", lambda text: f"summary({text})"),
        Agent("lookup", "small", lambda summary: f"db result for {summary}"),
    ]
    result = run_pipeline("call.wav", chain)
    print(demo_result("Static Prompt Chaining", "Fixed linear agent pipeline", result))


if __name__ == "__main__":
    main()
