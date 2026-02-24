import streamlit as st
from huggingface_hub import InferenceClient

# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

# -----------------------
# Load HuggingFace Token
# -----------------------
if "HF_TOKEN" not in st.secrets:
    st.error("HF_TOKEN not found in Streamlit Secrets.")
    st.stop()

HF_TOKEN = st.secrets["HF_TOKEN"]

# -----------------------
# Create HF Client
# -----------------------
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)

# -----------------------
# Curriculum Generator
# -----------------------
def generate_curriculum(prompt):
    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=500,
            temperature=0.7
        )
        return response
    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------
# Sidebar Inputs
# -----------------------
with st.sidebar:
    st.header("Curriculum Inputs")

    grade = st.selectbox(
        "Grade Level",
        ["Primary", "Middle School", "High School", "University"]
    )

    subject = st.text_input("Subject")
    duration = st.text_input("Duration (e.g., 4 weeks)")
    approach = st.selectbox(
        "Teaching Approach",
        ["Lecture-Based", "Project-Based", "Hybrid"]
    )

    generate = st.button("Generate Curriculum")

# -----------------------
# Generate Button Logic
# -----------------------
if generate:

    if not subject:
        st.warning("Please enter a subject.")
        st.stop()

    prompt = f"""
You are an expert curriculum designer.

Create a structured curriculum in markdown format with:

# Course Overview
# Learning Objectives
# Weekly Breakdown
# Assessment Strategy
# Capstone Project

Grade: {grade}
Subject: {subject}
Duration: {duration}
Approach: {approach}
"""

    with st.spinner("Generating curriculum..."):
        output = generate_curriculum(prompt)
        st.markdown(output)
