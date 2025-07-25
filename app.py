from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, Friend!"})

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to my API!"})

@app.route("/greet", methods=["POST"])
def greet():
    data = request.get_json()
    name = data.get("name", "friend")
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(debug=True)
