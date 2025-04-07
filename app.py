
from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

generator = pipeline("text-generation", model="distilgpt2", framework="pt")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = generator(
        f"Chacha Chaudhary: {user_input}",
        max_length=100,
        num_return_sequences=1,
        truncation=True,
        pad_token_id=50256
    )[0]["generated_text"]
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
