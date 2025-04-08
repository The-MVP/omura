from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username == "admin" and password == "123456":
        return jsonify({"success": True, "message": "Login successful!", "token": "yourToken"})

    else:
        return jsonify({"success": False, "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)