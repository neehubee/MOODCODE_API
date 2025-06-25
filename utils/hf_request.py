import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Hugging Face API key from environment
HF_API_KEY = os.getenv("HF_API_KEY")
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# Function to query Hugging Face API
def query_huggingface(model_url, payload):
    response = requests.post(model_url, headers=HEADERS, json=payload)
    result = response.json()

    # Handle API errors gracefully
    if 'error' in result:
        raise Exception(result['error'])
    return result

