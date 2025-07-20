import os
from flask import Flask, render_template, request, jsonify
from logic.groq_client import ask_groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    response = ask_groq(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render uses dynamic port
    app.run(host="0.0.0.0", port=port, debug=True)
