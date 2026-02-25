import streamlit as st
from groq import Groq

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

if "GROQ_API_KEY" not in st.secrets:
    st.error("GROQ_API_KEY not set in Streamlit Secrets")
    st.stop()

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

user_input = st.text_area("Enter curriculum topic")

if st.button("Generate Curriculum"):
    if user_input:
        with st.spinner("Generating..."):
            try:
                response = client.chat.completions.create(
                    model="mixtral-8x7b-32768",
                    messages=[
                        {"role": "system", "content": "You are an expert academic curriculum designer."},
                        {"role": "user", "content": f"Create a detailed curriculum for {user_input}. Include objectives, modules, duration, and assessment methods."}
                    ],
                    temperature=0.7,
                )

                st.write(response.choices[0].message.content)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic.")
