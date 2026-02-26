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
from ats_scorer import score_ats


def extract_text_from_resume(filepath):
    """Extract text from PDF or DOCX resume files."""
    ext = os.path.splitext(filepath)[1].lower()

    if ext == ".pdf":
        try:
            with open(filepath, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = "\n".join(
                    page.extract_text() or "" for page in reader.pages
                )
            return text.strip()
        except Exception as e:
            print(f"[Resume Parser] PDF read error: {e}")
            return ""

    elif ext in (".doc", ".docx"):
        try:
            doc = Document(filepath)
            return "\n".join(para.text for para in doc.paragraphs).strip()
        except Exception as e:
            print(f"[Resume Parser] DOCX read error: {e}")
            return ""

    return ""


def analyze_resume(resume_text, target_role=""):
    """
    Analyze a resume using local skill scoring + live job scraping.

    Returns dict with: score, matched_skills, missing_skills, companies,
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
            "jobs": [],
            "ats_score": 0,
            "ats_grade": "F",
            "ats_criteria": [],
            "ats_tips": [],
            "ats_summary": {"passed": 0, "warnings": 0, "failed": 0},
        }

    extracted_skills = extract_skills_from_text(resume_text)
    skills_string = ", ".join(extracted_skills)

    result = score_skills(skills_string, target_role)
    jobs = _fetch_jobs(extracted_skills, result["target_role"], score=result["score"])

    # ATS scoring (only for resume uploads)
    ats_result = score_ats(resume_text, result["target_role"])
    result["ats_score"] = ats_result["ats_score"]
    result["ats_grade"] = ats_result["ats_grade"]
    result["ats_criteria"] = ats_result["criteria"]
    result["ats_tips"] = ats_result["ats_tips"]
    result["ats_summary"] = ats_result["summary"]

    return _build_result(result, jobs)


def analyze_profile(name, target_role, skills, education):
    """
    Analyze a manually entered profile using local scoring + job scraping.

    Returns dict with: score, matched_skills, missing_skills, companies,
                       suggestions, ai_summary, target_role, skill_breakdown, jobs
    """
    result = score_skills(skills, target_role)
    skills_list = [s.strip() for s in skills.split(",") if s.strip()]
    jobs = _fetch_jobs(skills_list, result["target_role"], score=result["score"])

    return _build_result(result, jobs)


def _build_result(result, jobs):
    """Attach job data and company list to a scoring result."""
    for job in jobs:
        job["eligibility"] = calculate_company_eligibility(result["score"], job.get("title", ""))

    companies = []
    for job in jobs:
        entry = job["company"]
        if job.get("title"):
            entry = f"{job['company']} — {job['title']}"
        companies.append(entry)

    # Fallback companies when scraping returns nothing
    if not companies:
        fallback = get_fallback_companies(result["company_tier"])
        companies = [f"{c['name']} ({c['type']})" for c in fallback]

    result["companies"] = companies
    result["jobs"] = jobs
    return result


def _fetch_jobs(skills, target_role, max_results=5, score=50):
    """Fetch jobs with error handling. Returns empty list on failure."""
    try:
        return search_jobs(
            skills=skills,
            target_role=target_role,
            location="India",
            max_results=max_results,
            score=score,
        )
    except Exception as e:
        print(f"[AI Analyzer] Job scraping failed: {e}")
        return []
