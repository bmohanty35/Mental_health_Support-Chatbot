import streamlit as st

def init_memory():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def add_message(role, text):
    st.session_state.messages.append((role, text))

def get_messages():
    return st.session_state.messages