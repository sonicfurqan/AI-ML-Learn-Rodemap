import streamlit as st
from chatbot import callChatbot


if "messages" not in st.session_state:
    st.session_state.messages = []


def refreshChat():
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


def invokeLLM():
    with st.status("Checking"):
        llmResponse = callChatbot(st.session_state["messages"])
        st.session_state["messages"].extend(llmResponse)
        for msg in llmResponse:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])


if __name__ == "__main__":
    refreshChat()


prompt = st.chat_input("Enter your message")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        invokeLLM()
