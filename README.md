# LangGraph Chatbot

A conversational AI chatbot built with **LangGraph** and **Google Generative AI** (Gemini), designed for state-based conversation management and intelligent response generation.


##
## Features

- 🤖 **Conversational AI** — Powered by Google's Generative AI (Gemini)
- 🔄 **State Management** — Built on LangGraph for stateful conversation handling
- 📊 **Graph-based Workflow** — Node-based architecture for modular conversation logic
- 🎯 **Configurable** — Easy configuration management for API keys and settings
- 🔌 **Modular Design** — Separate modules for graph definition, nodes, and state management

## Project Structure

```
langgraph-chatbot/
├── main.py                 # Entry point for the application
├── requirements.txt        # Project dependencies
└── app/
    ├── __init__.py        # Package initialization
    ├── config.py          # Configuration management
    ├── gemini.py          # Google Generative AI integration
    ├── graph.py           # LangGraph workflow definition
    ├── nodes.py           # Node implementations for the graph
    ├── state.py           # Conversation state definition
    └── __pycache__/       # Python cache (ignored in git)
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chatbot_lanGraph
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory with your API keys:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Requirements

- Python 3.8+
- langgraph
- langchain
- google-generativeai

See `requirements.txt` for the complete list of dependencies.

## Usage

Run the chatbot:
```bash
python main.py
```

## Configuration

Edit `app/config.py` to customize:
- API endpoints
- Model parameters
- Default conversation settings
- Logging configuration

## Key Components

### State Management (`app/state.py`)
Defines the conversation state structure that flows through the graph.

### Nodes (`app/nodes.py`)
Implements individual processing nodes that handle specific conversation tasks.

### Graph (`app/graph.py`)
Defines the LangGraph workflow connecting nodes and managing conversation flow.

### Gemini Integration (`app/gemini.py`)
Handles communication with Google's Generative AI API.

### Configuration (`app/config.py`)
Centralized configuration management for the application.

## License

MIT

## Contributing

Feel free to submit issues and enhancement requests!
