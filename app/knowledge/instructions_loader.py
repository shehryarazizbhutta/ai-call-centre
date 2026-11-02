
from pathlib import Path


INSTRUCTIONS_PATH = Path(__file__).with_name("agent_instructions.txt")


def load_agent_instructions() -> str:
    return INSTRUCTIONS_PATH.read_text(encoding="utf-8").strip()
