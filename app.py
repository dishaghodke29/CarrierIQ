import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from werkzeug.utils import secure_filename
from ai_analyzer import analyze_profile, analyze_resume, extract_text_from_resume

# Config
app = Flask(__name__)
app.secret_key = "supersecretkey"

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Routes

@app.route("/")
def home():
    return render_template("index.html")


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

            resume_text = extract_text_from_resume(filepath)

            if not resume_text:
                flash("Could not extract text from the file. Please try a different file.")
                return redirect(request.url)

            result = analyze_resume(resume_text)
            return _render_results(result)

        else:
            flash("Invalid file type. Only PDF, DOC, DOCX allowed.")
            return redirect(request.url)

    return render_template("upload.html")


@app.route("/fill_manual", methods=["GET", "POST"])
def fill_manual():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        target_role = request.form.get("target_role", "").strip()
        skills_input = request.form.get("skills", "").strip()
        education = request.form.get("education", "").strip()

        result = analyze_profile(name, target_role, skills_input, education)
        return _render_results(result)

    return render_template("fill_manual.html")


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


@app.route("/roadmap/<role>/<int:score>")
def roadmap(role, score):
    from skill_scorer import ROLE_SKILLS
    from learning_resources import build_learning_roadmap

    role_lower = role.lower()

    # Read missing skills from query params (passed from results page)
    missing_core = [s.strip() for s in request.args.get("core", "").split(",") if s.strip()]
    missing_important = [s.strip() for s in request.args.get("important", "").split(",") if s.strip()]
    missing_nice = [s.strip() for s in request.args.get("nice", "").split(",") if s.strip()]

    # If no missing skills provided, derive from role database
    if not missing_core and not missing_important and not missing_nice:
        if role_lower in ROLE_SKILLS:
            role_data = ROLE_SKILLS[role_lower]
            missing_core = [s.title() for s in role_data["core"]]
            missing_important = [s.title() for s in role_data["important"]]
            missing_nice = [s.title() for s in role_data["nice"]]

    # Build the personalized learning roadmap with resources
    phases = build_learning_roadmap(missing_core, missing_important, missing_nice)

    # Also keep project suggestions
    projects = _get_project_suggestions(role_lower)

    return render_template(
        "roadmap.html",
        role=role.title(),
        score=score,
        phases=phases,
        projects=projects,
    )


@app.route("/career-finder", methods=["GET", "POST"])
def career_finder():
    """Find best matching career roles for user skills."""
    from skill_scorer import find_best_roles, ROLE_SKILLS

    if request.method == "POST":
        skills_input = request.form.get("skills", "").strip()
        education = request.form.get("education", "").strip()

        roles = find_best_roles(skills_input)

        return render_template(
            "career_finder.html",
            roles=roles,
            skills_input=skills_input,
            education=education,
            total_roles=len(ROLE_SKILLS),
        )

    return render_template("career_finder.html", roles=None)


@app.route("/ats")
def ats_page():
    """Render the dedicated ATS analysis page from session data."""
    ats_data = session.get("ats_data", {})
    if not ats_data:
        flash("No ATS data available. Please upload a resume first.")
        return redirect(url_for("upload"))
    return render_template(
        "ats.html",
        ats_score=ats_data.get("ats_score", 0),
        ats_grade=ats_data.get("ats_grade", ""),
        ats_criteria=ats_data.get("ats_criteria", []),
        ats_tips=ats_data.get("ats_tips", []),
        ats_summary=ats_data.get("ats_summary", {}),
    )


# Helpers

def _render_results(result):
    """Render the results template from an analysis result dict."""
    # Store ATS data in session for the dedicated ATS page
    if result.get("ats_score") is not None:
        session["ats_data"] = {
            "ats_score": result.get("ats_score"),
            "ats_grade": result.get("ats_grade", ""),
            "ats_criteria": result.get("ats_criteria", []),
            "ats_tips": result.get("ats_tips", []),
            "ats_summary": result.get("ats_summary", {}),
        }

    return render_template(
        "results.html",
        score=result["score"],
        matched_skills=result["matched_skills"],
        missing_skills=result["missing_skills"],
        companies=result["companies"],
        ai_summary=result["ai_summary"],
        target_role=result.get("target_role", ""),
        jobs=result.get("jobs", []),
        skill_breakdown=result.get("skill_breakdown", {}),
        ats_score=result.get("ats_score"),
        ats_grade=result.get("ats_grade", ""),
        ats_criteria=result.get("ats_criteria", []),
        ats_tips=result.get("ats_tips", []),
        ats_summary=result.get("ats_summary", {}),
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
        # Mechanical Engineering
        "mechanical design engineer": ["3D Machine Part Design", "FEA Stress Analysis Project", "Assembly Drawing", "DFM Analysis Report"],
        "robotics engineer": ["Line-Following Robot", "Robotic Arm Controller", "SLAM Navigation Bot", "ROS2 Simulation"],
        # Electrical & Electronics
        "embedded systems engineer": ["IoT Weather Station", "RTOS Task Scheduler", "Motor Controller", "BLE Sensor Network"],
        "vlsi design engineer": ["ALU Design in Verilog", "FPGA Image Processor", "SoC Design Project", "Timing Analysis Report"],
        "iot engineer": ["Smart Home System", "Environmental Monitor", "Asset Tracking System", "Edge AI Device"],
        "electrical design engineer": ["PLC Automation Project", "SCADA Dashboard", "Motor Drive System", "Power System Simulation"],
        # Civil Engineering
        "structural engineer": ["RCC Building Design", "Steel Truss Analysis", "Foundation Design", "Earthquake Resistant Design"],
        "construction manager": ["Project Schedule (Primavera)", "Cost Estimation Report", "BIM 3D Model", "Safety Management Plan"],
        # Additional IT
        "blockchain developer": ["DeFi Token Contract", "NFT Marketplace", "DAO Voting System", "Decentralized App"],
        "game developer": ["2D Platformer Game", "3D FPS Prototype", "Mobile Puzzle Game", "Multiplayer Demo"],
        "network engineer": ["Network Topology Design", "Firewall Configuration", "VPN Setup Lab", "Network Monitoring Tool"],
        "database administrator": ["Database Optimization Report", "Backup & Recovery Plan", "Replication Setup", "Performance Tuning Lab"],
        "technical writer": ["API Documentation Site", "User Guide for App", "Technical Blog Series", "Knowledge Base Setup"],
        # Interdisciplinary
        "biomedical engineer": ["ECG Signal Analyzer", "Medical Image Processor", "Prosthetic Design Concept", "Clinical Data Dashboard"],
        "environmental engineer": ["Water Quality Monitor", "EIA Report Template", "GIS Mapping Project", "Carbon Footprint Calculator"],
    }
    return projects.get(role, ["Portfolio Project", "Open Source Contribution", "Team Project"])


@app.errorhandler(413)
def file_too_large(error):
    flash("File is too large. Maximum size is 5MB.")
    return redirect(url_for("upload"))


if __name__ == "__main__":
    app.run(debug=True)