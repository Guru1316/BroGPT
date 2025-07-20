from flask import Flask, render_template, request, jsonify
from logic.groq_client import ask_groq

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    response = ask_groq(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
