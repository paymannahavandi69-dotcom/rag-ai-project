import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖")
st.title("🤖 RAG Chatbot")
st.caption("Ask questions about the documents")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask your questions..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            session = requests.Session()
            session.trust_env = False
            response = session.post(
                "http://127.0.0.1:8000/ask",
                json={"question": prompt}
            )
            answer = response.json()["answer"]
            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})