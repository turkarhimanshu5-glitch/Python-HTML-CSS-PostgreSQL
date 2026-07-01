from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Flask Backend is Running Successfully",
        "status": "OK"
    })


@app.route("/api")
def api():
    return jsonify({
        "message": "Hello from Python Backend API"
    })


# Do not use app.run() in online runners
