import streamlit as st
import google.generativeai as genai

# Saita API Key
genai.configure(api_key="AIzaSyDJJW_Ah3Dgh59mpUcCDi91pouVXFmxISg")

# Saita System Instruction
instruction = "Sunanka Assistant AI 2026. Mataimaki ne ga Imrana Umar Abubakar na Kangon Wasagu, Kebbi. Kar ka fadi bayaninsa sai an tambaye ka."
model = genai.GenerativeModel("model = genai.GenerativeModel("gemini-1.5-flash")", system_instruction=instruction)

st.title("🤖 Assistant AI 2026")
st.write("Barka da zuwa! Ina sauraronka.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Rubuta sakonka anan..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
