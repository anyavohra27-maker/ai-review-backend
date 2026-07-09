# Day 3
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/")  # Route = URL path         # Decorator = attaches behavior to a function or we can say connect URL to the function
# def home():  # Function = what happens on that path
#     return "Welcome" 

# @app.route("/about")  # Multiple routes
# def about():
#     return "About"

# @app.route("/review")  # Multiple routes
# def review():
#     return "Review"


# @app.route("/data")
# def data():
#     return jsonify({
#         "name": "Anya",
#         "project": "AI reviewer"
#     })

# if __name__ == "__main__":
#     app.run(debug=True, port=5004)


# Day 4
# get request input
# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/hello")
# def hello():
#     name = request.args.get("name")
#     return f"Hello {name}"

# if __name__ == "__main__":
#     app.run(debug=True, port=5005)  # after running visit http://127.0.0.1:5005/hello?name=Anya

# post request input
# from flask import Flask, request
# app = Flask(__name__)

# @app.route("/review", methods=["POST"])
# def review():
#     data = request.json
#     return data["code"]

# if __name__ == "__main__":
#     app.run(debug=True, port=5006)

# full backend
from flask import Flask, request, jsonify
from reviewer import review_code

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Code Review Assistant"

@app.route("/review", methods=["POST"])
def review():
    data = request.json

    code = data.get("code")

    result = review_code(code)

    return result["data"]["review"]

if __name__ == "__main__":
    app.run(debug=False, port=5008)