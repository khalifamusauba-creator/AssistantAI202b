import streamlit as st
import google.generativeai as genai

# 1. Saita Sabon API Key ɗinka
API_KEY = "AIzaSyDe79TfZ0UUJcTqn9Wy0sKcGl0bH0dHYgM"
genai.configure(api_key=API_KEY)

# 2. Saita Model da System Instruction
instruction = "Sunanka Assistant AI 2026. Kai mataimaki ne ga Imrana Umar Abubakar na Kangon Wasagu."

# Mun yi amfani da try/except anan don tabbatar model din ya ruku (load) da kyau
try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash", 
        system_instruction=instruction
    )
except Exception as e:
    st.error(f"Matsalar Model: {e}")

# 3. Tsarin Fuskar Website
st.set_page_config(page_title="Assistant AI 2026", page_icon="🤖")

# Hoton Robot
st.image("https://raw.githubusercontent.com/khalifamusauba-creator/AssistantAI2026/main/FB_IMG_17735447707727859.jpg")
st.title("🤖 Assistant AI 2026")
st.caption("Mataimakin Ilimi da Bincike")

# Ma'ajiyar hirarrakin baya
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 4. Sashin Input mai suna 'Research'
if p := st.chat_input("Research"):
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    try:
        # Kira zuwa ga Gemini
        response = model.generate_content(p)
        
        with st.chat_message("assistant"):
            st.markdown(response.text)
        
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    except Exception as e:
        # Wannan zai nuna maka ainihin kuskuren idan har yanzu akwai matsala
        st.error(f"Kuskuren API: {e}")
