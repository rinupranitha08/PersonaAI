
import streamlit as st

from prompt_engine import (
    personalities,
    generate_prompt,
    create_cache_key
)

from gemini_service import generate_ai_response

st.set_page_config(
    page_title="PersonaAI",
    page_icon="🎭",
    layout="wide"
)

st.title("🎭 PersonaAI")
st.caption("One AI. Multiple Personalities.")

st.divider()

# Initialize response cache
if "response_cache" not in st.session_state:
    st.session_state.response_cache = {}

st.subheader("Ask PersonaAI")

question = st.text_area(
    "Enter your question:",
    placeholder="Example: What is Artificial Intelligence?",
    height=100
)

personality = st.selectbox(
    "Choose a personality:",
    list(personalities.keys())
)

if st.button("Generate Response", type="primary"):

    if not question.strip():
        st.warning("Please enter a question first.")

    else:
        question = question.strip()

        prompt = generate_prompt(personality, question)

        cache_key = create_cache_key(personality, question)

        try:
            if cache_key in st.session_state.response_cache:
                answer = st.session_state.response_cache[cache_key]
                st.info("Cached response – No new Gemini API request.")

            else:
                with st.spinner("Generating response..."):
                    answer = generate_ai_response(prompt)

                st.session_state.response_cache[cache_key] = answer

            st.subheader(personality)
            st.write(answer)

            with st.expander("View Generated Prompt"):
                st.code(prompt, language="text")

        except Exception as e:
            st.error(
                "Unable to generate a response. "
                "Please check the Gemini configuration."
            )

st.divider()

st.caption("PersonaAI | Prompt Engineering Project")
