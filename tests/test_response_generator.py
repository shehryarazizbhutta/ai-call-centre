from app.services.response_generator import generate_response
from langchain_core.messages import HumanMessage


def test_generate_response_returns_text():
    response = generate_response([
    HumanMessage(
        content="What information can you provide from the campaign knowledge?"
    )
    ])

    assert isinstance(response, str)
    assert response.strip()