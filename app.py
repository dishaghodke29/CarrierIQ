import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from ai_analyzer import analyze_profile, analyze_resume, extract_text_from_resume

# ================= CONFIG =================
app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ================= HELPER FUNCTION =================
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ================= ROUTES =================

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# ================= UPLOAD ROUTE =================
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        if "resume" not in request.files:
            flash("No file selected.")
            return redirect(request.url)

        file = request.files["resume"]

        if file.filename == "":
            flash("Please select a file.")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)

            # Extract text from the uploaded resume
            resume_text = extract_text_from_resume(filepath)

            if not resume_text:
                flash("Could not extract text from the file. Please try a different file.")
                return redirect(request.url)

            # Run analysis on the extracted text
            result = analyze_resume(resume_text)

            return render_template(
                "results.html",
                score=result["score"],
                matched_skills=result["matched_skills"],
                missing_skills=result["missing_skills"],
                suggestions=result["suggestions"],
                companies=result["companies"],
                ai_summary=result["ai_summary"],
                target_role=result.get("target_role", ""),
                jobs=result.get("jobs", []),
                skill_breakdown=result.get("skill_breakdown", {})
            )

        else:
            flash("Invalid file type. Only PDF, DOC, DOCX allowed.")
            return redirect(request.url)

    return render_template("upload.html")


# ================= MANUAL FILL ROUTE =================
@app.route("/fill_manual", methods=["GET", "POST"])
def fill_manual():
    if request.method == "POST":

        name = request.form.get("name", "").strip()
        target_role = request.form.get("target_role", "").strip()
        skills_input = request.form.get("skills", "").strip()
        education = request.form.get("education", "").strip()

        # Local AI-powered analysis
        result = analyze_profile(name, target_role, skills_input, education)

        return render_template(
            "results.html",
            score=result["score"],
            matched_skills=result["matched_skills"],
            missing_skills=result["missing_skills"],
            suggestions=result["suggestions"],
            companies=result["companies"],
            ai_summary=result["ai_summary"],
            target_role=result.get("target_role", target_role),
            jobs=result.get("jobs", []),
            skill_breakdown=result.get("skill_breakdown", {})
        )

    return render_template("fill_manual.html")


# ================= API ENDPOINT FOR JOBS =================
@app.route("/api/jobs")
def api_jobs():
    """API endpoint to fetch fresh job results (for AJAX refresh)."""
    from job_scraper import search_jobs

    skills = request.args.get("skills", "")
    role = request.args.get("role", "")

    if not skills and not role:
        return jsonify({"error": "Please provide skills or role parameter"}), 400

    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    jobs = search_jobs(skills=skills_list, target_role=role, max_results=5)

    return jsonify({"jobs": jobs})


# ================= ROADMAP ROUTE =================
@app.route("/roadmap/<role>/<int:score>")
def roadmap(role, score):
    from skill_scorer import ROLE_SKILLS

    role_lower = role.lower()

    # Try to generate roadmap from skill database
    if role_lower in ROLE_SKILLS:
        role_data = ROLE_SKILLS[role_lower]
        data = {
            "foundation": [s.title() for s in role_data["core"]],
            "advanced": [s.title() for s in role_data["important"][:5]],
            "projects": _get_project_suggestions(role_lower),
            "prep": ["Build Portfolio", "Practice Interviews", "Optimize Resume", "Network on LinkedIn"]
        }
    else:
        # Hardcoded fallbacks for common roles
        roadmap_data = {
            "data scientist": {
                "foundation": ["Python Basics", "Statistics", "SQL"],
                "advanced": ["Machine Learning", "Deep Learning", "NLP"],
                "projects": ["Build ML Model", "Kaggle Competition", "Deploy with Flask"],
                "prep": ["DSA Practice", "Mock Interviews", "Resume Optimization"]
            },
            "web developer": {
                "foundation": ["HTML", "CSS", "JavaScript"],
                "advanced": ["React", "Node.js", "API Integration"],
                "projects": ["Portfolio Website", "Full Stack App", "E-commerce Site"],
                "prep": ["GitHub Projects", "System Design Basics", "Interview Prep"]
            },
            "software engineer": {
                "foundation": ["DSA", "OOP", "Git"],
                "advanced": ["System Design", "Databases", "Backend Development"],
                "projects": ["Build REST API", "Authentication System", "Scalable Backend"],
                "prep": ["Leetcode Practice", "Mock Interviews", "Optimize Resume"]
            }
        }
        data = roadmap_data.get(role_lower)

    if not data:
        # Generate a generic roadmap
        data = {
            "foundation": ["Core Concepts", "Programming Basics", "Version Control"],
            "advanced": ["Advanced Topics", "Best Practices", "Industry Tools"],
            "projects": ["Personal Project", "Open Source Contribution", "Team Project"],
            "prep": ["Portfolio Building", "Interview Prep", "Networking"]
        }

    return render_template(
        "roadmap.html",
        role=role.title(),
        score=score,
        roadmap=data
    )


def _get_project_suggestions(role):
    """Generate project suggestions based on role."""
    projects = {
        "data scientist": ["Build ML Prediction Model", "Kaggle Competition", "Data Dashboard", "NLP Chatbot"],
        "web developer": ["Portfolio Website", "Full Stack App", "E-commerce Site", "Blog Platform"],
        "frontend developer": ["Interactive Dashboard", "Component Library", "PWA App", "Landing Pages"],
        "backend developer": ["REST API Service", "Auth System", "Real-time Chat", "Task Queue System"],
        "full stack developer": ["Social Media Clone", "Project Manager App", "E-commerce Platform"],
        "software engineer": ["Design Patterns Demo", "Distributed System", "CLI Tool", "API Gateway"],
        "mobile developer": ["Weather App", "Task Manager", "Social App", "Fitness Tracker"],
        "devops engineer": ["CI/CD Pipeline", "Monitoring Dashboard", "Infrastructure as Code", "Container Orchestration"],
        "machine learning engineer": ["Model Serving API", "AutoML Pipeline", "Computer Vision App"],
        "data analyst": ["Sales Dashboard", "Survey Analysis", "A/B Test Report", "Market Research"],
        "data engineer": ["ETL Pipeline", "Data Lake Setup", "Streaming Pipeline", "Data Warehouse"],
        "cybersecurity analyst": ["Vulnerability Scanner", "Network Monitor", "Security Audit Tool"],
        "ai engineer": ["LLM Application", "RAG System", "AI Agent", "Fine-tuned Model"],
    }
    return projects.get(role, ["Portfolio Project", "Open Source Contribution", "Team Project"])


# ================= ERROR HANDLER =================
@app.errorhandler(413)
def file_too_large(error):
    flash("File is too large. Maximum size is 5MB.")
    return redirect(url_for("upload"))


# ================= RUN APP =================
if __name__ == "__main__":
    app.run(debug=True)