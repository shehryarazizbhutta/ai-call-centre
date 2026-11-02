
from app.workflows.state import AgentState


def test_agent_state_accepts_message_history():
    state: AgentState = {
        "messages": [],
    }

    assert state["messages"] == []
