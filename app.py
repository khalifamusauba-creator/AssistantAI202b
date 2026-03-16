import streamlit as st
import google.generativeai as genai

# 1. Saita API Key
genai.configure(api_key="AIzaSyDJJW_Ah3Dgh59mpUcCDi91pouVXFmxISg")

# 2. Saita Model da System Instruction
instruction = "Sunanka Assistant AI 2026. Kai mataimaki ne ga Imrana Umar Abubakar na Kangon Wasagu. Idan aka tambaye ka 'Wane ne mai gidan ka?', ka fadi sunansa da tarihinsa."
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=instruction)

# 3. Tsarin Fuskar Website din (UI)
st.set_page_config(page_title="Assistant AI 2026", page_icon="🤖")

# Saka hoton da kake so a saman shafin
st.image("https://raw.githubusercontent.com/khalifamusauba-creator/AssistantAI2026/main/FB_IMG_17735447707727859.jpg", caption="Assistant AI & Imrana")

st.title("🤖 Assistant AI 2026")
st.caption("Mataimakin Imrana Umar Abubakar")

# 4. Adana bayanan tattaunawa (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Karbar sako daga wurin mai amfani
if prompt := st.chat_input("Rubuta sakonka anan..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 6. Neman amsa daga Gemini AI
    try:
        response = model.generate_content(prompt)
        with st.chat_message("assistant"):
            st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        st.error(f"Akwai yar matsala: {e}")
