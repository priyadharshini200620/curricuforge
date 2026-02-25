import streamlit as st

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

def generate_curriculum(grade, subject, duration, approach):

    return f"""
# Course Overview
This {duration} {subject} course is designed for {grade} students using a {approach} approach.

The course builds foundational understanding and practical application skills in {subject}.

# Learning Objectives
- Understand core concepts of {subject}
- Apply theoretical knowledge to real-world scenarios
- Develop analytical and critical thinking skills
- Complete structured assessments and a capstone

# Weekly Breakdown

## Week 1
Introduction to fundamental concepts of {subject}

## Week 2
Core theories and structured exercises

## Week 3
Applied learning and guided practice

## Week 4
Review, assessments, and project development

# Assessment Strategy
- Weekly quizzes
- Assignments
- Final evaluation
- Capstone project

# Capstone Project
Students will design and present a practical project demonstrating mastery of {subject}.
"""

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
    else:
        with st.spinner("Generating curriculum..."):
            output = generate_curriculum(grade, subject, duration, approach)
            st.markdown(output)
