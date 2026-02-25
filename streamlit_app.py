import streamlit as st
import requests

st.set_page_config(page_title="CurricuForge", layout="wide")

st.title("📚 CurricuForge")
st.subheader("AI Powered Curriculum Design System")

if "HF_TOKEN" not in st.secrets:
    st.error("HF_TOKEN not set in Streamlit Secrets")
    st.stop()

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {st.secrets['HF_TOKEN']}",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)

    # Show raw response if error
    if response.status_code != 200:
        st.error(f"Status Code: {response.status_code}")
        st.write(response.text)
        return None

    try:
        return response.json()
    except:
        st.error("Invalid JSON response received.")
        st.write(response.text)
        return None


user_input = st.text_area("Enter curriculum topic")

if st.button("Generate Curriculum"):
    if user_input:
        with st.spinner("Generating..."):

            output = query({
                "inputs": f"Create a detailed curriculum for {user_input}. Include objectives, modules, duration, and assessment."
            })

            if output:
                if isinstance(output, list):
                    st.write(output[0].get("generated_text", "No text generated."))
                else:
                    st.write(output)
    else:
        st.warning("Please enter a topic.")
