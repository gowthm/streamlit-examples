import streamlit as st
from PIL import Image

st.set_page_config(page_title="LLM Chatbot", layout="wide")

# ---------------------------
# Sidebar Profile
# ---------------------------
with st.sidebar:
    # st.image("profile.jpg", width=120)  # <-- Put your profile photo in same folder
    
    st.markdown("""
    ### **Gowtham M**
    AI & Backend Developer  
    Salem • Bangalore • India  

    🚀 I build fast, modern AI applications using  
    **Python**, **Streamlit**, and **Groq LLaMA models**.
    """)

    st.divider()

    st.markdown("### 🔧 **Tech Stack**")
    st.markdown("""
    - 🐍 Python  
    - 🎨 Streamlit  
    - ⚡ Groq LLMs  
    - 🦙 LLaMA 3 / 4  
    - ☁️ AWS / Serverless  
    - 🔗 APIs & Automation  
    """)

    st.divider()

    st.markdown("### 📬 **Connect**")
    st.markdown("""
    🔗 [LinkedIn](https://linkedin.com/)  
    🐙 [GitHub](https://github.com/)  
    📧 yourmail@example.com  
    """)

# ---------------------------
# Main Chat UI
# ---------------------------
st.title("💬 LLM Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # Placeholder assistant response
    reply = "This is a sample response. I'll connect Groq here later."

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
