import streamlit as st
from chatbot import get_response

# Page configuration
st.set_page_config(page_title="Chatbot UI", page_icon=":speech_balloon:", layout="wide")

# Chatbot UI layout
st.title("Chat with Sam")
st.markdown("Type a message below and interact with Sam, your personal chatbot!")

# Persistent state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["sender"] == "user":
        st.markdown(f"**You:** {message['text']}")
    else:
        st.markdown(f"**Sam:** {message['text']}")

# Temporary user input handler
def handle_user_input():
    if st.session_state.temp_input:
        # Add user message to chat history
        st.session_state.messages.append({"sender": "user", "text": st.session_state.temp_input})

        # Get bot response
        bot_response = get_response(st.session_state.temp_input)

        # Add bot response to chat history
        st.session_state.messages.append({"sender": "bot", "text": bot_response})

        # Clear the input field
        st.session_state.temp_input = ""

# Input field for user message
st.text_input("Type your message here", key="temp_input", on_change=handle_user_input)

# Display the updated chat history
for message in st.session_state.messages:
    if message["sender"] == "user":
        st.markdown(f"**You:** {message['text']}")
    else:
        st.markdown(f"**Sam:** {message['text']}")
