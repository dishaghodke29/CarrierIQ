"""
AI Analyzer for CarrierIQ.
Uses local skill scoring engine + job scraping for real company data.
No external AI API needed.
"""

import os
import PyPDF2
from docx import Document

from skill_scorer import score_skills, extract_skills_from_text, get_fallback_companies, calculate_company_eligibility
from job_scraper import search_jobs


def extract_text_from_resume(filepath):
    """Extract text from PDF or DOCX resume files."""
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        text = ""
        try:
            with open(filepath, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            print(f"[Resume Parser] PDF read error: {e}")
        return text.strip()

    elif ext in (".doc", ".docx"):
        try:
            doc = Document(filepath)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text.strip()
        except Exception as e:
            print(f"[Resume Parser] DOCX read error: {e}")
            return ""

    return ""


def analyze_resume(resume_text, target_role=""):
    """
    Analyze a resume using local skill scoring + live job scraping.

    Args:
        resume_text: Extracted text from resume
        target_role: Optional target role

    Returns:
        dict with: score, matched_skills, missing_skills, companies,
                   suggestions, ai_summary, target_role, skill_breakdown, jobs
    """
    if not resume_text:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "companies": [],
            "suggestions": ["Upload a valid PDF or DOCX file with readable text."],
            "ai_summary": "Could not extract text from the uploaded resume.",
            "target_role": target_role or "General",
            "skill_breakdown": {},
            "jobs": []
        }

    # Step 1: Extract skills from resume text
    extracted_skills = extract_skills_from_text(resume_text)
    skills_string = ", ".join(extracted_skills)

    # Step 2: Score skills locally
    result = score_skills(skills_string, target_role)

    # Step 3: Fetch real job postings tailored to score tier
    jobs = _fetch_jobs(extracted_skills, result["target_role"], score=result["score"])

    # Step 4: Calculate eligibility for each company
    for job in jobs:
        job["eligibility"] = calculate_company_eligibility(result["score"], job.get("title", ""))

    # Build company list from jobs
    companies = []
    for job in jobs:
        company_entry = job["company"]
        if job.get("title"):
            company_entry = f"{job['company']} — {job['title']}"
        companies.append(company_entry)

    # Fallback companies if scraping returned nothing
    if not companies:
        fallback = get_fallback_companies(result["company_tier"])
        companies = [f"{c['name']} ({c['type']})" for c in fallback]

    result["companies"] = companies
    result["jobs"] = jobs

    return result


def analyze_profile(name, target_role, skills, education):
    """
    Analyze a manually entered profile using local scoring + job scraping.

    Args:
        name: Candidate name
        target_role: Target job role
        skills: Comma-separated skills string
        education: Education background

    Returns:
        dict with: score, matched_skills, missing_skills, companies,
                   suggestions, ai_summary, target_role, skill_breakdown, jobs
    """
    # Step 1: Score skills locally
    result = score_skills(skills, target_role)

    # Step 2: Fetch real job postings
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    # Step 2: Fetch real job postings tailored to score tier
    jobs = _fetch_jobs(skills_list, result["target_role"], score=result["score"])

    # Step 3: Calculate eligibility for each company
    for job in jobs:
        job["eligibility"] = calculate_company_eligibility(result["score"], job.get("title", ""))

    # Build company list from jobs
    companies = []
    for job in jobs:
        company_entry = job["company"]
        if job.get("title"):
            company_entry = f"{job['company']} — {job['title']}"
        companies.append(company_entry)

    # Fallback companies if scraping returned nothing
    if not companies:
        fallback = get_fallback_companies(result["company_tier"])
        companies = [f"{c['name']} ({c['type']})" for c in fallback]

    result["companies"] = companies
    result["jobs"] = jobs

    return result


def _fetch_jobs(skills, target_role, max_results=5, score=50):
    """
    Fetch jobs with error handling. Passes score to search_jobs
    so results are tailored to the candidate's level.
    Returns empty list on failure rather than crashing the app.
    """
    try:
        jobs = search_jobs(
            skills=skills,
            target_role=target_role,
            location="India",
            max_results=max_results,
            score=score
        )
        return jobs
    except Exception as e:
        print(f"[AI Analyzer] Job scraping failed: {e}")
        return []
