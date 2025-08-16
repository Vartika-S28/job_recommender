from flask import Flask, render_template, request, flash, redirect, url_for, session
import pandas as pd
import fitz
import os
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
        username = request.form["username"].strip()
        if username:
            session["username"] = username
            flash(f"Welcome back, {username}! Let's find your perfect job match.", "success")
            return redirect(url_for("index"))
        else:
            flash("Please enter your name to continue.", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
    username = session.get("username", "User")
    session.pop("username", None)
    flash(f"Goodbye, {username}! Come back soon.", "info")
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def index():
    if "username" not in session:
        return redirect(url_for("login"))

    recommendations = []
    resume_text = ""
    error_message = ""

    if request.method == "POST":
        try:
            if "resume" in request.files and request.files["resume"].filename:
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
                    flash("Resume uploaded successfully! Analyzing your skills...", "success")
                else:
                    flash("Please upload a PDF file.", "error")
                    return render_template("index.html", recommendations=[])
            elif request.form.get("skills", "").strip():
                user_input = request.form["skills"].strip()
                flash("Analyzing your skills...", "success")
            else:
                flash("Please either upload a resume or enter your skills.", "error")
                return render_template("index.html", recommendations=[])

            # Generate recommendations
            user_vec = vectorizer.transform([user_input])
            similarity_scores = cosine_similarity(user_vec, tfidf_matrix)
            top_indices = similarity_scores[0].argsort()[::-1][:3]
            recommendations = df.iloc[top_indices][["Job Title", "Required Skills"]].values.tolist()
            
            if recommendations:
                flash(f"Found {len(recommendations)} great job matches for you!", "success")
            else:
                flash("No matching jobs found. Try different skills or keywords.", "info")

        except Exception as e:
            flash("An error occurred while processing your request. Please try again.", "error")
            print(f"Error: {e}")

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
