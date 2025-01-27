import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

print(query({"inputs": "What is the capital of France?"}))
