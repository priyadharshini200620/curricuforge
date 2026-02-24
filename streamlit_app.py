import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="CurricuForge")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Sidebar Inputs
with st.sidebar:
    st.header("Curriculum Inputs")

    grade = st.selectbox("Grade Level", ["Primary", "Middle School", "High School", "University"])
    subject = st.text_input("Subject")
    duration = st.text_input("Duration (e.g., 8 weeks)")
    approach = st.selectbox("Teaching Approach", ["Project-Based", "Lecture-Based", "Hybrid"])
    generate = st.button("Generate Curriculum")

# Session state
if "curriculum" not in st.session_state:
    st.session_state.curriculum = ""

# Generate curriculum
if generate and subject:
    prompt = f"""
    You are an expert curriculum designer.

    Create a structured curriculum in MARKDOWN format.

    Grade Level: {grade}
    Subject: {subject}
    Duration: {duration}
    Teaching Approach: {approach}

    Include:
    1. Course Overview
    2. Learning Objectives (Bloom’s Taxonomy verbs)
    3. Weekly Breakdown
    4. Assessment Strategy
    5. Capstone Project
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.session_state.curriculum = response.choices[0].message.content

# Display curriculum
if st.session_state.curriculum:
    st.markdown(st.session_state.curriculum)

    st.download_button(
        "Download Curriculum",
        st.session_state.curriculum,
        "CurricuForge_Curriculum.txt"
    )
