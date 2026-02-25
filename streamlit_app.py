import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

# Check token
if "HF_TOKEN" not in st.secrets:
    st.error("HF_TOKEN missing in secrets.")
    st.stop()

HF_TOKEN = st.secrets["HF_TOKEN"]

# Use stable text-generation model
client = InferenceClient(
    model="google/flan-t5-large",
    token=HF_TOKEN
)

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

with st.sidebar:
    st.header("Curriculum Inputs")
    grade = st.selectbox("Grade Level", ["Primary", "Middle School", "High School", "University"])
    subject = st.text_input("Subject")
    duration = st.text_input("Duration (e.g., 4 weeks)")
    approach = st.selectbox("Teaching Approach", ["Lecture-Based", "Project-Based", "Hybrid"])
    generate = st.button("Generate Curriculum")

if generate:
    if not subject:
        st.warning("Please enter a subject.")
        st.stop()

    prompt = f"""
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
