from unittest.mock import patch

from langchain_core.messages import HumanMessage, AIMessage

from app.workflows.nodes.response_node import response_node


def test_response_node_returns_ai_message():
    state = {
        "messages": [HumanMessage(content="What can you tell me?")]
    }

    with patch(
        "app.workflows.nodes.response_node.generate_response",
        return_value="Here is the relevant information.",
    ):
        result = response_node(state)

    assert len(result["messages"]) == 1
    assert isinstance(result["messages"][0], AIMessage)
    assert result["messages"][0].content == "Here is the relevant information."