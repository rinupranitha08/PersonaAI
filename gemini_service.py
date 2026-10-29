
import streamlit as st
from google import genai
from google.genai import types

MODEL_NAME = "gemini-3.5-flash-lite"

def generate_ai_response(prompt):

    # Retrieve the API key securely from Streamlit Secrets
    api_key = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=300,
            temperature=0.5
        )
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    return response.text
