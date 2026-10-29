# PersonaAI – One AI, Multiple Personalities

## Overview

PersonaAI is a Prompt Engineering project that demonstrates how
a single Generative AI model can produce different responses to
the same question using dynamic role-based prompting.

## Features

- Four AI personalities:
  - Kindergarten Teacher
  - College Professor
  - Comedian
  - Technical Interviewer
- Dynamic prompt generation
- Response-length constraints (50–80 words)
- Gemini API integration
- SHA-256 prompt-aware caching
- Generated prompt preview
- Interactive Streamlit interface

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- google-genai Python SDK
- SHA-256 hashing

## AI Model

gemini-3.5-flash-lite

## How It Works

1. The user enters a question.
2. The user selects an AI personality.
3. PersonaAI constructs a structured prompt.
4. The application checks its session cache.
5. If no cached response exists, Gemini generates an answer.
6. The answer is displayed to the user.

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your Gemini API key using Streamlit Secrets:

```toml
GEMINI_API_KEY = "your_api_key"
```

Run the application:

```bash
streamlit run app.py
```

Never commit your actual API key to GitHub.

## Project Category

Prompt Engineering / Generative Artificial Intelligence
