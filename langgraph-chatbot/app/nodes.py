from app.state import GraphState
from app.gemini import ask_gemini


def classify(state: GraphState) -> GraphState:
    question = state.get("question", "").lower()

    if any(word in question for word in ["hello", "hi", "hey"]):
        classification = "greeting"
    else:
        classification = "search"

    return {**state, "classification": classification}


def respond(state: GraphState) -> GraphState:
    classification = state.get("classification")
    question = state.get("question")

    if classification == "greeting":
        response = "Hello! How can I help you?"
    elif classification == "search":
        response = ask_gemini(question)
    else:
        response = "I don't understand."

    return {**state, "response": response}