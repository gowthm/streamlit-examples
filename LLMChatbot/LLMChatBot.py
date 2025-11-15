import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Page config
st.set_page_config(page_title="Groq Chat", page_icon="⚡", layout="wide")

# ---------------------------------------------------
# Inject Custom CSS for Sidebar + Chat UI
# ---------------------------------------------------
st.markdown("""
<style>

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1117, #1b1f24);
        padding: 20px 15px;
    }

    .sidebar-box {
        background: #161b22;
        padding: 16px;
        border-radius: 14px;
        box-shadow: 0px 0px 6px rgba(255,255,255,0.05);
        margin-bottom: 20px;
    }

    .sidebar-title {
        color: #fff;
        font-size: 17px;
        font-weight: 600;
        padding-bottom: 8px;
        border-bottom: 1px solid #30363d;
        margin-bottom: 12px;
    }

    /* Chat message styling */
    .chat-bubble-user {
        background: #0066ff;
        color: white;
        padding: 12px 18px;
        border-radius: 16px;
        margin: 6px 0;
        width: fit-content;
        max-width: 80%;
        margin-left: auto;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
    }

    .chat-bubble-assistant {
        background: #e3e3e3;
        color: black;
        padding: 12px 18px;
        border-radius: 16px;
        margin: 6px 0;
        width: fit-content;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:


    st.markdown("<div class='sidebar-title'>⚡ Model Selection</div>", unsafe_allow_html=True)

    model = st.selectbox(
        "",
        [
            "llama-3.3-70b-versatile",
            "meta-llama/llama-4-maverick-17b-128e-instruct",
            "meta-llama/llama-4-scout-17b-16e-instruct",
            "meta-llama/llama-guard-4-12b",
            "meta-llama/llama-prompt-guard-2-22m"
        ]
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# Main Header
# ---------------------------------------------------
st.title("⚡ Groq Chat Assistant")
st.write("Fast, enhanced UI experience powered by Groq LLMs.")

# ---------------------------------------------------
# API Key
# ---------------------------------------------------
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    st.error("❌ Please add GROQ_API_KEY in Streamlit → Secrets")
    st.stop()

client = Groq(api_key=api_key)

# ---------------------------------------------------
# Chat History
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render message bubbles
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-assistant'>{msg['content']}</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    st.markdown(f"<div class='chat-bubble-user'>{user_input}</div>", unsafe_allow_html=True)

    # Assistant reply
    placeholder = st.empty()
    full_reply = ""

    with st.spinner("Generating response..."):
        response = client.chat.completions.create(
            model=model,
            messages=st.session_state.messages,
            stream=True
        )

        for chunk in response:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                full_reply += delta.content
                placeholder.markdown(
                    f"<div class='chat-bubble-assistant'>{full_reply}</div>",
                    unsafe_allow_html=True
                )

    st.session_state.messages.append({"role": "assistant", "content": full_reply})
