# Grok Chat Bot

A Streamlit-based chat interface that leverages X.AI's Grok model for interactive conversations.

## Features

- Real-time streaming responses
- Persistent chat history
- Clean chat interface
- System prompt customization
- Grok Vision Beta model integration

## Installation

```bash
pip install -r requirements.txt
```

## Required Dependencies

- streamlit
- openai
- python-dotenv

## Environment Setup

Create a `.env` file in the root directory:

```plaintext
XAI_API_KEY=your_xai_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Enter your question in the chat input
3. Receive streamed responses from Grok
4. View chat history from previous interactions

```

## Features Breakdown

**Chat Interface**
- Message history management
- Real-time response streaming
- Markdown formatting support
- User-friendly input field

**API Integration**
- X.AI API configuration
- Grok Vision Beta model
- Streaming response handling
- Custom system prompts

**State Management**
- Session state persistence
- Chat history tracking
- Message role organization

## Sidebar Information

The application includes an informative sidebar explaining:
- Bot functionality
- Model information
- API provider details

Sample Output:

![sample output](https://github.com/user-attachments/assets/6517b791-4c71-437a-9cf9-d720dfe902bc)
