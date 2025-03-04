import streamlit as st
from retriver import Retriver


st.title("🤖 Chatbot with Streamlit")


# Load Retriver only once
if "retriever" not in st.session_state:
    st.session_state.retriever = Retriver()  # Initialize once

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)

    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Use the existing retriever instance
    bot_response = st.session_state.retriever.get_answer(user_input)

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
