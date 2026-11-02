
from app.knowledge.instructions_loader import load_agent_instructions


def test_load_agent_instructions():
    instructions = load_agent_instructions()

    assert instructions
    assert "AI call-centre agent" in instructions
