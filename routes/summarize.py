from flask import Blueprint, request, jsonify
from utils.hf_request import query_huggingface

# Create a blueprint for summarization
summarize = Blueprint('summarize', __name__)

# Hugging Face model for summarizing
MODEL_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

# Route to summarize long text into short form
@summarize.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()

    # Check if input text is given
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Send input text to Hugging Face summarization model
        result = query_huggingface(MODEL_URL, {"inputs": data['text']})

        summary = result[0]['summary_text']

        return jsonify({'summary': summary})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
