from flask import Blueprint, request, jsonify
from utils.hf_request import query_huggingface

# Create Blueprint for summarization
summarize = Blueprint('summarize', __name__)

# Hugging Face summarization model URL
MODEL_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"

# Route for summarizing text
@summarize.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Query Hugging Face model
        result = query_huggingface(MODEL_URL, {"inputs": data['text']})

        summary = result[0]['summary_text']

        return jsonify({'summary': summary})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
