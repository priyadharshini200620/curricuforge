import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

# Stop app if token missing
if "HF_TOKEN" not in st.secrets:
    st.error("HF_TOKEN not set in Streamlit Secrets")
    st.stop()

client = InferenceClient(
    model="google/flan-t5-large",
    token=st.secrets["HF_TOKEN"]
)

user_input = st.text_area("Enter curriculum topic")

if st.button("Generate Curriculum"):
    if user_input:
        with st.spinner("Generating..."):
            try:
                response = client.text_generation(
                    f"Create a detailed academic curriculum for {user_input}. Include objectives, modules, duration, and assessment.",
                    max_new_tokens=500
                )

                st.write(response)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic.")
