from langgraph.graph import START, END, StateGraph

from app.workflows.state import AgentState
from app.workflows.nodes.response_node import response_node


builder = StateGraph(AgentState)

builder.add_node("response", response_node)

builder.add_edge(START, "response")
builder.add_edge("response", END)

response_graph = builder.compile()