import streamlit as st
from agent_core import get_agent_response

st.set_page_config(
    page_title="Currency Converter Agent",
    page_icon="💱",
    layout="centered"
)

st.title("💱 Currency Converter Agent")
st.caption("Talk naturally. I’ll ask follow-ups if needed.")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY PAST CONVERSATION ----------------
for msg in st.session_state.messages:
    # Handle both objects and dicts
    if isinstance(msg, dict):
        role = msg.get("role", "assistant")
        content = msg.get("content", "")
    else:
        content = getattr(msg, "content", "")
        role = getattr(msg, "type", None) or getattr(msg, "role", "assistant")

    with st.chat_message(role):
        st.markdown(content)

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Append user message
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get agent reply
    st.session_state.messages = get_agent_response(st.session_state.messages)

    # Display assistant reply
    # Always take last message from agent
    last_msg = st.session_state.messages[-1]
    if isinstance(last_msg, dict):
        assistant_reply = last_msg.get("content", "")
    else:
        assistant_reply = getattr(last_msg, "content", "")

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
