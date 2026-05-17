"""Pseudo-realistic Temporal shape for this plugin.

This file avoids importing Temporal so the repository stays dependency-light.
Use these function boundaries as workflow/activity boundaries in a real app.
"""

from __future__ import annotations


def route_activity(task: str) -> dict[str, str | bool]:
    return {
        "route": "firmware_debug" if "uart" in task.lower() else "general",
        "risk": "high" if "production" in task.lower() else "low",
        "approval_required": "production" in task.lower(),
    }


def approval_activity(route: dict[str, str | bool]) -> str:
    return "wait_for_human" if route["approval_required"] else "continue"


def model_activity(task: str, route: dict[str, str | bool]) -> dict[str, object]:
    return {
        "model": "large-reasoning-model" if route["risk"] == "high" else "small-fast-model",
        "summary": f"Handled {task}",
        "actions": ["validate", "execute"],
    }
