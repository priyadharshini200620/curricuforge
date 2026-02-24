import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

HF_TOKEN = st.secrets["HF_TOKEN"]

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

def generate_curriculum(prompt):
    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=500
