from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
import pickle

app = Flask(__name__)
CORS(app)
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
    

model = tf.keras.models.load_model("sentiment_model.h5")
max_review_length = 200

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = text.strip()
    return text

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    review = data.get("text", "")
    if not review:
        return jsonify({"error": "No review provided"}), 400

    processed = preprocess_text(review)
    sequence = tokenizer.texts_to_sequences([processed])
    padded = pad_sequences(sequence, maxlen=max_review_length)
    prediction = model.predict(padded)[0][0]

    sentiment = "positive" if prediction > 0.5 else "negative"
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
