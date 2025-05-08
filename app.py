import streamlit as st
from openai_assistant import get_assistant_response

st.set_page_config(page_title="L1 Helpdesk Agent")
st.title("💼 AI Helpdesk Agent")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.chat_input("Ask your IT Helpdesk...")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = get_assistant_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": response})

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])