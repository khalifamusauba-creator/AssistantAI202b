import streamlit as st
import google.generativeai as genai

# 1. Saita API Key (Tabbatar ka kiyaye wannan lambar)
API_KEY = "AIzaSyDiDJEMC0z9rjy2EZcsbW-nJNsXD-l3ZOk"
genai.configure(api_key=API_KEY)

# 2. Saita System Instruction da Model
# Mun cire "models/" mun bar "gemini-1.5-flash" kadai
instruction = "Sunanka Assistant AI 2026. Kai mataimaki ne ga Imrana Umar Abubakar na Kangon Wasagu."
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", 
    system_instruction=instruction
)

# 3. Tsarin Fuskar Website
st.set_page_config(page_title="Assistant AI 2026", page_icon="🤖")

# Hoton Robot daga GitHub dinka
st.image("https://raw.githubusercontent.com/khalifamusauba-creator/AssistantAI2026/main/FB_IMG_17735447707727859.jpg")
st.title("🤖 Assistant AI 2026")
st.caption("Mataimakin Ilimi da Bincike")

# Ma'ajiyar hirarrakin baya (Chat History)
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# 4. Sashin Input mai suna 'Research'
if p := st.chat_input("Research"):
    # Nuna tambayar user
    st.session_state.messages.append({"role": "user", "content": p})
    with st.chat_message("user"):
        st.markdown(p)
    
    # Nuna amsar AI
    try:
        # Kira zuwa ga Gemini
        r = model.generate_content(p)
        
        with st.chat_message("assistant"):
            st.markdown(r.text)
        
        st.session_state.messages.append({"role": "assistant", "content": r.text})
    except Exception as e:
        st.error(f"Kuskure: An samu matsala wurin kiran API. Tab
