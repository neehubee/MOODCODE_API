from flask import Flask, jsonify

# Importing the different route blueprints
from routes.mood import mood
from routes.crisis import crisis
from routes.summarize import summarize

# Initialize the Flask app
app = Flask(__name__)

# Register all the routes (blueprints)
app.register_blueprint(mood)
app.register_blueprint(crisis)
app.register_blueprint(summarize)

# Just a simple home route to check if the server is running
@app.route('/')
def home():
    return jsonify({"message": "MoodDecode API is running successfully"})

# Running the app
if __name__ == '__main__':
    app.run(debug=True)

