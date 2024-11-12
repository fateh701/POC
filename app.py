from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response  # Ensure this file exists with your chatbot logic

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/predict', methods=['POST'])  # Ensure this is correct
def predict():
    text = request.get_json().get("message")
    response = get_response(text)  # Replace with your chatbot logic
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
