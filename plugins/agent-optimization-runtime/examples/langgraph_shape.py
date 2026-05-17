"""Pseudo-realistic LangGraph shape for this plugin.

This file avoids importing LangGraph so the repository stays dependency-light.
Copy the node functions into a real LangGraph app and wire them as graph nodes.
"""

from __future__ import annotations


def route_node(state: dict) -> dict:
    state["route"] = "firmware_debug" if "uart" in state["task"].lower() else "general"
    return state


def approval_node(state: dict) -> dict:
    state["approval_required"] = "production" in state["task"].lower()
    return state


def model_node(state: dict) -> dict:
    state["answer"] = "Call provider adapter, validate schema, then update graph state."
    return state


def validation_node(state: dict) -> dict:
    if "answer" not in state and not state.get("approval_required"):
        raise ValueError("missing answer")
    state["validated"] = True
    return state
