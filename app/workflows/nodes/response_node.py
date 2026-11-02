from langchain_core.messages import HumanMessage, AIMessage

from app.services.response_generator import generate_response
from app.workflows.state import AgentState


def response_node(state: AgentState) -> dict:
    last_message = state["messages"][-1]

    if not isinstance(last_message, HumanMessage):
        raise ValueError("The last message must be from the user.")

    answer = generate_response(state["messages"])

    return {
        "messages": [AIMessage(content=answer)]
    }