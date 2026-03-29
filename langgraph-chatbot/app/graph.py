from langgraph.graph import StateGraph
from app.state import GraphState
from app.nodes import classify, respond


def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("classify", classify)
    builder.add_node("respond", respond)

    builder.set_entry_point("classify")
    builder.add_edge("classify", "respond")
    builder.set_finish_point("respond")

    return builder.compile()