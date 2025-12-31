# A flask application for CI/CD Jenkins Pipeline practice

from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route("/")
def welcome():
    return ("Welcome to the Flask application")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)