import streamlit as st
import requests

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

# Get HuggingFace token from secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

def generate_curriculum(prompt):
    API_URL = API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 500
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error {response.status_code}: {response.text}"

# Sidebar Inputs
with st.sidebar:
    st.header("Curriculum Inputs")
    grade = st.selectbox("Grade Level", ["Primary", "Middle School", "High School", "University"])
    subject = st.text_input("Subject")
    duration = st.text_input("Duration (e.g., 4 weeks)")
    approach = st.selectbox("Teaching Approach", ["Lecture-Based", "Project-Based", "Hybrid"])
    generate = st.button("Generate Curriculum")

if generate:
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
