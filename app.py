# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import openai

load_dotenv()  # loads OPENAI_API_KEY from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    lesson = None
    if request.method == "POST":
        grade = request.form["grade"]
        subject = request.form["subject"]
        focus = request.form["focus"]
        # TODO: call OpenAI here
        lesson = f"Generated lesson for grade {grade} on {subject} ({focus})"
    return render_template("index.html", lesson=lesson)

if __name__ == "__main__":
    app.run(debug=True)
