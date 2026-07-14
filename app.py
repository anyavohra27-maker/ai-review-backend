# full backend
from flask import Flask, request, jsonify
from reviewer.reviewer import review_code

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Code Review Assistant"

@app.route("/review", methods=["POST"])
def review():
    data = request.json

    code = data.get("code")

    result = review_code(code)

    return jsonify(result) 

if __name__ == "__main__":
    app.run(debug=False, port=5008)