import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Hugging Face API key from .env
HF_API_KEY = os.getenv("HF_API_KEY")
HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}

# Function to query Hugging Face API safely
def query_huggingface(model_url, payload):
    try:
        response = requests.post(model_url, headers=HEADERS, json=payload)
        result = response.json()

        # Check if API returned an error
        if response.status_code != 200 or 'error' in result:
            return {'error': result.get('error', 'Unknown error from Hugging Face')}

        return result

    except Exception as e:
        # Catch connection errors or unexpected issues
        return {'error': str(e)}
