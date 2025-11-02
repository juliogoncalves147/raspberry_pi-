from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Raspberry Pi API!"})

@app.route("/test")
def test():
    return jsonify({"status": "success", "data": [1, 2, 3]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
