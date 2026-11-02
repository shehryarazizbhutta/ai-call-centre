from unittest.mock import patch

from langchain_core.messages import HumanMessage, AIMessage

from app.workflows.response_graph import response_graph


def test_response_graph_returns_ai_response():
    with patch(
        "app.workflows.nodes.response_node.generate_response",
        return_value="Here is the answer.",
    ):
        result = response_graph.invoke({
            "messages": [HumanMessage(content="Hello")]
        })

    assert isinstance(result["messages"][-1], AIMessage)
    assert result["messages"][-1].content == "Here is the answer."