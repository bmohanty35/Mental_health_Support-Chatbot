import streamlit as st
from backend.gemini_client import GeminiClient
from backend.memory import init_memory, add_message, get_messages
from utils.logger import setup_logger

logger = setup_logger()

st.set_page_config(page_title="Mental Health Support Chatbot")

st.title("🧠 Mental Health Support Chatbot")
st.caption("This assistant provides emotional support, not medical diagnosis.")

# Initialize Memory
init_memory()

# Initialize Client
if "gemini_client" not in st.session_state:
    try:
        st.session_state.gemini_client = GeminiClient()
    except Exception as e:
        st.error(str(e))
        st.stop()

client = st.session_state.gemini_client

# Display History
for role, text in get_messages():
    with st.chat_message(role):
        st.markdown(text)

# Input
user_input = st.chat_input("How are you feeling today?")

if user_input:
    add_message("user", user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.send_message(user_input)
                reply = response.text
                add_message("assistant", reply)
                st.markdown(reply)
                logger.info("Response generated successfully")
            except Exception as e:
                logger.error(str(e))
                st.error(f"Error: {str(e)}")   # TEMP DEBUG