import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

if "HF_TOKEN" not in st.secrets:
    st.error("HF_TOKEN not set in Streamlit Secrets")
    st.stop()

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=st.secrets["HF_TOKEN"]
)

user_input = st.text_area("Enter curriculum topic")

if st.button("Generate Curriculum"):
    if user_input:
        with st.spinner("Generating..."):
            try:
                response = client.text_generation(
                    user_input,
                    max_new_tokens=500
                )
                st.write(response)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic.")
