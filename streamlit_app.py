import requests

def generate_curriculum(prompt):
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]
