from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

st.title("Grok Chat Bot")
st.write("Ask any question to get an answer from the latest Grok model!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Send request to Grok
        for response in client.chat.completions.create(
            model="grok-vision-beta",
            messages=[
                {"role": "system", "content": "You are Grok, a helpful chatbot to answer user queries without any bias."},
                {"role": "user", "content": prompt},
            ],
            stream=True,
        ):
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Add a sidebar with additional information
st.sidebar.title("About Grok Chat Bot")
st.sidebar.info(
    "This chat bot uses the Grok model to provide answers "
    "related to your questions. It's powered by X.AI's API and Streamlit.")