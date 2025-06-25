from flask import Blueprint, request, jsonify
from utils.hf_request import query_huggingface

# Create a blueprint for crisis detection
crisis = Blueprint('crisis', __name__)

# Model URL for sentiment detection
MODEL_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"

# Route to detect if the user is in a crisis based on text input
@crisis.route('/detect_crisis', methods=['POST'])
def detect_crisis():
    data = request.get_json()

    # Check for valid input
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Query Hugging Face model
        result = query_huggingface(MODEL_URL, {"inputs": data['text']})

        label = result[0][0]['label']
        score = result[0][0]['score']

        # Basic logic: if the sentiment is negative and confidence is high, mark as crisis
        crisis_detected = label.upper() == 'NEGATIVE' and score > 0.85

        return jsonify({
            'crisis_detected': crisis_detected,
            'confidence': round(score, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
