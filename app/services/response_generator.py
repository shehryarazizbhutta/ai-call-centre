from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage

from app.core.config import settings
from app.knowledge.instructions_loader import load_agent_instructions
from app.knowledge.vector_store import retrieve_knowledge


llm = ChatGroq(
    model=settings.GROQ_MODEL,
    api_key=settings.GROQ_API_KEY,
)


def generate_response(messages: list[BaseMessage]) -> str:
    last_message = messages[-1]
    question = last_message.content

    knowledge = retrieve_knowledge(question)

    if not knowledge:
        knowledge = ["No relevant campaign knowledge was found."]

    instructions = load_agent_instructions()

    system_prompt = (
        f"{instructions}\n\n"
        f"Relevant knowledge:\n{chr(10).join(knowledge)}"
    )

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        *messages,
    ])

    return response.content