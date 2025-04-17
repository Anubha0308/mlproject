from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re

app = Flask(__name__)
CORS(app)

# Load model and tokenizer
model = load_model("model/sentiment_model.h5")
with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 200  

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = text.strip()
    return text

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("text", "")

    if not review:
        return jsonify({"error": "No text provided"}), 400

    review_clean = preprocess_text(review)
    seq = tokenizer.texts_to_sequences([review_clean])
    padded = pad_sequences(seq, maxlen=MAX_LEN)

    pred = model.predict(padded)[0][0]
    sentiment = "positive" if pred > 0.5 else "negative"

    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(debug=True)
