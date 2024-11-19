from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow Cross-Origin Resource Sharing for React requests

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    age = request.form.get("age")
    file = request.files.get("file")

    if name and age and file:
        return jsonify({
            "status": "success",
            "message": f"Form submitted successfully! Name: {name}, Age: {age}, File: {file.filename}"
        })
    return jsonify({"status": "error", "message": "Missing fields!"})

if __name__ == "__main__":
    app.run(debug=True)

