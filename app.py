import streamlit as st
import google.generativeai as genai

# 1. Saita API Key
genai.configure(api_key="AIzaSyDJJW_Ah3Dgh59mpUcCDi91pouVXFmxISg")

# 2. Saita Model (An saka 'models/' a farko don kaucewa 404)
instruction = "Sunanka Assistant AI 2026. Mataimaki ne ga Imrana Umar Abubakar."
model = genai.GenerativeModel("models/gemini-1.5-pro", system_instruction=instruction)

# 3. Tsarin Fuskar Website
st.set_page_config(page_title="Assistant AI 2026", page_icon="🤖")

# Hoton Robot
st.image("https://raw.githubusercontent.com/khalifamusauba-creator/AssistantAI2026/main/FB_IMG_17735447707727859.jpg")
st.title("🤖 Assistant AI 2026")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

# 4. Sashin da ka ce a sa 'Research'
if p := st.chat_input("Research"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"): st.markdown(p)
    try:
        r = model.generate_content(p)
        with st.chat_message("assistant"): st.markdown(r.text)
        st.session_state.messages.append({"role": "assistant", "content": r.text})
    except Exception as e:
        st.error(f"Kuskure: {e}")
