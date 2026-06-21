from flask import Flask, request, jsonify
from flask_cors import CORS

from parser import extract_text
from llm import analyze_resume
from utils import clean_text, allowed_file

app = Flask(__name__)
CORS(app)


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        file = request.files.get("file")
        text = request.form.get("text", "").strip()

        # Validate input
        if not file and not text:
            return jsonify({
                "error": "Please upload a resume or paste resume text."
            }), 400

        if file and not allowed_file(file.filename):
            return jsonify({
                "error": "Only PDF and DOCX files are supported."
            }), 400

        resume_text = extract_text(file, text)

        resume_text = clean_text(resume_text)

        if not resume_text:
            return jsonify({
                "error": "Unable to extract text from resume."
            }), 400

        result = analyze_resume(resume_text)

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/")
def home():
    return jsonify({
        "message": "Resume Analyzer API Running"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )