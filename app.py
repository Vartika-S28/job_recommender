from flask import Flask, render_template, request
import pandas as pd
import fitz
import os
from flask import session, redirect, url_for
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "some-secret-key"

# Load dataset
df = pd.read_csv("jobs.csv")

# Preprocess: convert skills into string format
df["Combined Skills"] = df["Required Skills"].fillna("").astype(str)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df["Combined Skills"])

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def index():
    if "username" not in session:
        return redirect(url_for("login"))

    recommendations = []
    resume_text = ""

    if request.method == "POST":
        if "resume" in request.files:
            resume = request.files["resume"]
            if resume.filename.endswith(".pdf"):
                # Save and extract text
                filepath = os.path.join("static", resume.filename)
                resume.save(filepath)
                with fitz.open(filepath) as doc:
                    for page in doc:
                        resume_text += page.get_text()
                os.remove(filepath)
                user_input = resume_text
            else:
                user_input = request.form["skills"]
        else:
            user_input = request.form["skills"]

        user_vec = vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(user_vec, tfidf_matrix)
        top_indices = similarity_scores[0].argsort()[::-1][:3]
        recommendations = df.iloc[top_indices][["Job Title", "Required Skills"]].values.tolist()

    return render_template("index.html", recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)
