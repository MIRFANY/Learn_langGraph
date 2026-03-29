from app.graph import build_graph

app = build_graph()

print("=== LangGraph Chatbot ===")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    state = {"question": user_input}
    result = app.invoke(state)

    print("Bot:", result["response"])