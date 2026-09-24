# 📚 Study Tutor Agent

A beginner-friendly single-agent study tutor built with Streamlit, CrewAI, and Groq.

## Features

- Single Study Tutor agent
- Groq `openai/gpt-oss-120b`
- Calculator tool
- CrewAI memory
- Streamlit chat interface
- Subject, level, and learning mode selection

## GitHub

Upload the complete project structure to GitHub.

Do NOT upload `.env` or your Groq API key.

## Render

Build command:

`pip install -r requirements.txt`

Start command:

`streamlit run app.py --server.address 0.0.0.0 --server.port $PORT`

Add this environment variable in Render:

`GROQ_API_KEY=your_actual_groq_api_key`
