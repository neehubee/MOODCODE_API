from flask import Blueprint, request, jsonify
from utils.hf_request import query_huggingface

# Create a blueprint for mood analysis
mood = Blueprint('mood', __name__)

# Hugging Face model for sentiment analysis
MODEL_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"

# Route to analyze mood based on text input
@mood.route('/analyze_mood', methods=['POST'])
def analyze_mood():
    data = request.get_json()

    # Check if 'text' key is present
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    try:
        # Send the input text to Hugging Face model
        result = query_huggingface(MODEL_URL, {"inputs": data['text']})

        label = result[0][0]['label']
        score = result[0][0]['score']

        # Mapping labels to human-readable emotions
        mood_map = {
            'LABEL_0': 'negative',
            'LABEL_1': 'neutral',
            'LABEL_2': 'positive',
            'NEGATIVE': 'negative',
            'POSITIVE': 'positive'
        }
        mood_value = mood_map.get(label, label.lower())

        return jsonify({
            'emotion': mood_value,
            'confidence': round(score, 2)  # Rounded for cleaner output
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

