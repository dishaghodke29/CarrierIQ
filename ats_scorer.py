"""
ATS (Applicant Tracking System) Scorer for CarrierIQ.
Evaluates resume text for ATS compatibility across 10 weighted criteria.
Returns a numeric score, letter grade, per-criterion breakdown, and prioritised tips.
"""

import re
from skill_scorer import ROLE_SKILLS, _normalize, _fuzzy_match


# ── Reference Data ──────────────────────────────────────────────────────────

SECTION_HEADERS = [
    "education", "experience", "work experience", "professional experience",
    "skills", "technical skills", "projects", "certifications", "summary",
    "objective", "achievements", "awards", "publications", "volunteer",
    "internship", "internships", "training", "languages", "interests",
    "references", "contact", "profile", "about me",
]

ACTION_VERBS = [
    "achieved", "analyzed", "architected", "automated", "built", "collaborated",
    "conducted", "configured", "created", "decreased", "delivered", "deployed",
    "designed", "developed", "drove", "engineered", "enhanced", "established",
    "executed", "expanded", "generated", "grew", "implemented", "improved",
    "increased", "initiated", "integrated", "launched", "led", "managed",
    "mentored", "migrated", "negotiated", "optimized", "orchestrated",
    "organized", "oversaw", "performed", "planned", "presented", "produced",
    "published", "reduced", "refactored", "resolved", "restructured",
    "scaled", "secured", "simplified", "spearheaded", "streamlined",
    "supervised", "transformed", "upgraded",
]

BAD_PATTERNS = [
    r"[│┤├┬┴┼╔╗╚╝═║]",
    r"[\u2022\u2023\u25E6\u2043\u2219]",
    r"[★☆●○◆◇▶►]",
    r"\|{2,}",
    r"_{5,}",
    r"={5,}",
    r"-{5,}",
    r"\.{5,}",
]

# ── Grade Mapping ───────────────────────────────────────────────────────────

def _get_grade(score):
    """Return a letter grade string for a 0-100 score."""
    if score >= 95: return "A+"
    if score >= 85: return "A"
    if score >= 75: return "B+"
    if score >= 65: return "B"
    if score >= 55: return "C+"
    if score >= 45: return "C"
    if score >= 35: return "D"
    return "F"


# ── Main Entry Point ────────────────────────────────────────────────────────

def score_ats(resume_text, target_role=""):
    """
    Score a resume for ATS compatibility.

    Args:
        resume_text: Extracted text from resume
        target_role: Target job role for keyword relevance

    Returns:
        dict with:
            ats_score    – 0-100 numeric score
            ats_grade    – letter grade (A+ … F)
            criteria     – list of criterion dicts (name, score, weight, status, tip, tip_priority, details)
            ats_tips     – list of tip dicts (text, priority)
            summary      – dict with passed, warnings, failed counts
    """
    if not resume_text:
        return {
            "ats_score": 0,
            "ats_grade": "F",
            "criteria": [],
            "ats_tips": [{"text": "Upload a readable resume.", "priority": "high"}],
            "summary": {"passed": 0, "warnings": 0, "failed": 0},
        }

    text_lower = resume_text.lower()
    lines = resume_text.strip().split("\n")
    words = resume_text.split()
    word_count = len(words)

    # Ordered list: (checker_function, weight)
    checks = [
        (_check_contact_info(resume_text),              10),
        (_check_section_headers(text_lower, lines),     15),
        (_check_quantifiable(resume_text),              12),
        (_check_action_verbs(text_lower),               10),
        (_check_length(word_count),                      8),
        (_check_keywords(text_lower, target_role),      20),
        (_check_formatting(resume_text),                 8),
        (_check_education(text_lower),                   7),
        (_check_consistency(resume_text, lines),         5),
        (_check_parsability(lines, word_count),          5),
    ]

    criteria = []
    for criterion, weight in checks:
        criterion["weight"] = weight
        criteria.append(criterion)

    # Weighted score
    total_weight = sum(c["weight"] for c in criteria)
    raw = sum(c["score"] * c["weight"] for c in criteria)
    ats_score = round(raw / total_weight) if total_weight else 0

    # Summary counts
    passed  = sum(1 for c in criteria if c["status"] == "good")
    warnings = sum(1 for c in criteria if c["status"] == "warn")
    failed  = sum(1 for c in criteria if c["status"] == "bad")

    # Collect tips, sorted by priority (high first)
    priority_order = {"high": 0, "medium": 1, "low": 2}
    ats_tips = [
        {"text": c["tip"], "priority": c["tip_priority"]}
        for c in criteria
        if c["status"] != "good" and c.get("tip")
    ]
    ats_tips.sort(key=lambda t: priority_order.get(t["priority"], 9))

    return {
        "ats_score": ats_score,
        "ats_grade": _get_grade(ats_score),
        "criteria": criteria,
        "ats_tips": ats_tips,
        "summary": {"passed": passed, "warnings": warnings, "failed": failed},
    }


# ── Individual Criterion Checkers ───────────────────────────────────────────
# Each returns: {name, score, status, tip, tip_priority, details}

def _status(score):
    if score >= 70: return "good"
    if score >= 40: return "warn"
    return "bad"


def _check_contact_info(text):
    """Check for email, phone, and LinkedIn."""
    found = 0
    details = []

    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        found += 1
        details.append("Email found")
    else:
        details.append("Email missing")

    if re.search(r"[\+]?[\d\s\-\(\)]{7,15}", text):
        found += 1
        details.append("Phone found")
    else:
        details.append("Phone missing")

    if re.search(r"linkedin\.com|linkedin", text, re.IGNORECASE):
        found += 1
        details.append("LinkedIn found")
    else:
        details.append("LinkedIn missing")

    # GitHub / Portfolio bonus
    if re.search(r"github\.com|portfolio|website", text, re.IGNORECASE):
        found += 0.5
        details.append("Portfolio/GitHub found")

    score = min(100, round(found / 2.5 * 100))
    status = _status(score)
    tip = "" if status == "good" else "Add email, phone, and LinkedIn URL. A portfolio or GitHub link is a bonus."

    return {
        "name": "Contact Information",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "high",
        "details": " · ".join(details),
    }


def _check_section_headers(text_lower, lines):
    """Check for standard resume section headers."""
    found_sections = []
    for line in lines:
        line_clean = line.strip().lower().rstrip(":")
        for header in SECTION_HEADERS:
            if line_clean == header or line_clean.startswith(header):
                if header not in found_sections:
                    found_sections.append(header)
                break

    essential = ["education", "experience", "skills"]
    essential_found = sum(1 for s in essential if any(s in f for f in found_sections))

    total = len(found_sections)
    score = min(100, round((essential_found / 3 * 60) + (min(total, 6) / 6 * 40)))
    status = _status(score)
    tip = "" if status == "good" else "Use clear section headers: Education, Experience, Skills, Projects, Certifications."

    missing = [s.title() for s in essential if not any(s in f for f in found_sections)]
    detail = f"{total} sections detected"
    if missing:
        detail += f" · Missing: {', '.join(missing)}"

    return {
        "name": "Section Headers",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "high",
        "details": detail,
    }


def _check_quantifiable(text):
    """Check for numbers, percentages, and metrics."""
    metrics = re.findall(
        r"\d+[%xX]|\$[\d,]+[KkMm]?|\d{2,}[\+]|\d+\s*(?:users|customers|clients|projects|team|members|revenue|sales|increase|decrease|growth|reduction)",
        text, re.IGNORECASE,
    )
    numbers = re.findall(r"\b\d{2,}\b", text)

    metric_count = len(metrics)
    number_count = min(len(numbers), 10)

    score = min(100, metric_count * 18 + number_count * 5)
    status = _status(score)
    tip = "" if status == "good" else "Quantify your impact: 'increased revenue by 30%', 'managed team of 8', 'reduced load time by 2s'."

    return {
        "name": "Quantified Impact",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "medium",
        "details": f"{metric_count} metrics, {number_count} numeric values",
    }


def _check_action_verbs(text_lower):
    """Check for strong action verbs."""
    found_verbs = [v for v in ACTION_VERBS if v in text_lower]
    count = len(found_verbs)
    score = min(100, count * 14)
    status = _status(score)
    tip = "" if status == "good" else "Start bullet points with action verbs: Developed, Implemented, Optimized, Delivered, Led."

    examples = ", ".join(found_verbs[:5])
    detail = f"{count} found"
    if examples:
        detail += f" ({examples})"

    return {
        "name": "Action Verbs",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "medium",
        "details": detail,
    }


def _check_length(word_count):
    """Check if resume length is optimal."""
    if 300 <= word_count <= 800:
        score, detail = 100, f"{word_count} words — optimal length"
    elif 200 <= word_count < 300:
        score, detail = 70, f"{word_count} words — slightly short"
    elif 800 < word_count <= 1200:
        score, detail = 70, f"{word_count} words — slightly long"
    elif 100 <= word_count < 200:
        score, detail = 40, f"{word_count} words — too short"
    elif word_count > 1200:
        score, detail = 40, f"{word_count} words — too long, consider trimming"
    else:
        score, detail = 20, f"{word_count} words — very short"

    status = _status(score)
    tip = "" if status == "good" else "Aim for 300-800 words. 1 page for < 5 years experience, 2 pages max."

    return {
        "name": "Resume Length",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "low",
        "details": detail,
    }


def _check_keywords(text_lower, target_role):
    """Check density of role-relevant keywords."""
    role_key = _normalize(target_role) if target_role else ""

    if role_key not in ROLE_SKILLS:
        for r in ROLE_SKILLS:
            if _fuzzy_match(role_key, r, threshold=0.6):
                role_key = r
                break

    if not role_key or role_key not in ROLE_SKILLS:
        return {
            "name": "Keyword Relevance",
            "score": 50,
            "status": "warn",
            "tip": "Specify a target role to unlock keyword analysis.",
            "tip_priority": "medium",
            "details": "No target role detected",
        }

    role_data = ROLE_SKILLS[role_key]
    core_kw = role_data["core"]
    important_kw = role_data["important"]
    nice_kw = role_data["nice"]

    core_found = sum(1 for kw in core_kw if kw.lower() in text_lower)
    imp_found  = sum(1 for kw in important_kw if kw.lower() in text_lower)
    nice_found = sum(1 for kw in nice_kw if kw.lower() in text_lower)

    total_kw = len(core_kw) + len(important_kw) + len(nice_kw)
    total_found = core_found + imp_found + nice_found

    # Core keywords matter more
    weighted = (core_found * 3 + imp_found * 2 + nice_found * 1)
    max_weighted = (len(core_kw) * 3 + len(important_kw) * 2 + len(nice_kw) * 1)
    ratio = weighted / max_weighted if max_weighted else 0

    score = min(100, round(ratio * 120))
    status = _status(score)
    tip = "" if status == "good" else f"Add more {target_role} keywords — especially core skills shown in the skill breakdown above."

    detail = f"{total_found}/{total_kw} keywords · Core: {core_found}/{len(core_kw)}"

    return {
        "name": "Keyword Relevance",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "high",
        "details": detail,
    }


def _check_formatting(text):
    """Check for characters/patterns that break ATS parsers."""
    issues = 0
    for pattern in BAD_PATTERNS:
        issues += len(re.findall(pattern, text))

    score = max(0, 100 - issues * 15)
    status = _status(score)
    tip = "" if status == "good" else "Remove decorative symbols, table characters, and long divider lines. Use simple bullets (- or *)."

    return {
        "name": "Clean Formatting",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "high",
        "details": "No issues detected" if issues == 0 else f"{issues} problematic characters found",
    }


def _check_education(text_lower):
    """Check for education details."""
    found = 0

    degrees = [
        "b.tech", "btech", "b.e", "b.sc", "bsc", "m.tech", "mtech", "m.sc", "msc",
        "m.s.", "b.s.", "bachelor", "master", "mba", "phd", "ph.d", "diploma",
        "associate", "b.a.", "m.a.", "b.com", "m.com", "bca", "mca",
    ]
    if any(d in text_lower for d in degrees):
        found += 1

    if re.search(r"university|college|institute|iit|nit|iiit|school", text_lower):
        found += 1

    if re.search(r"20[0-3]\d|19[89]\d", text_lower):
        found += 1

    # GPA / CGPA
    if re.search(r"gpa|cgpa|percentage|grade|first class|distinction", text_lower):
        found += 0.5

    score = min(100, round(found / 3 * 100))
    status = _status(score)
    tip = "" if status == "good" else "Include degree name, university, graduation year, and GPA/CGPA if strong."

    return {
        "name": "Education Details",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "medium",
        "details": f"{int(found)}/3 key details present",
    }


# ── New Criteria ────────────────────────────────────────────────────────────

def _check_consistency(text, lines):
    """Check for date format consistency and tense usage."""
    issues = 0
    details = []

    # Date format detection
    dash_dates = len(re.findall(r"\b\d{4}\s*[-–]\s*\d{4}\b", text))
    slash_dates = len(re.findall(r"\b\d{1,2}/\d{4}\b", text))
    month_dates = len(re.findall(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\b", text, re.IGNORECASE))
    
    formats_used = sum(1 for f in [dash_dates, slash_dates, month_dates] if f > 0)
    if formats_used > 1:
        issues += 1
        details.append("Mixed date formats")
    elif formats_used == 1:
        details.append("Consistent date format")
    else:
        details.append("No dates detected")

    # Check for consistent bullet style
    bullet_dash = sum(1 for l in lines if l.strip().startswith("-"))
    bullet_dot  = sum(1 for l in lines if l.strip().startswith("*"))
    bullet_special = sum(1 for l in lines if l.strip() and l.strip()[0] in "•◦▪")
    
    bullet_types = sum(1 for b in [bullet_dash, bullet_dot, bullet_special] if b > 0)
    if bullet_types > 1:
        issues += 1
        details.append("Mixed bullet styles")
    elif bullet_types == 1:
        details.append("Consistent bullets")

    # Tense mixing (simple check: past vs present in verb endings)
    past_count = len(re.findall(r"\b\w+ed\b", text))
    present_count = len(re.findall(r"\b(?:manage|develop|create|build|lead|design|implement|maintain|optimize|deploy)s?\b", text, re.IGNORECASE))
    if past_count > 3 and present_count > 3:
        ratio = min(past_count, present_count) / max(past_count, present_count)
        if ratio > 0.4:
            issues += 1
            details.append("Mixed verb tenses")
        else:
            details.append("Consistent tense")
    else:
        details.append("Tense OK")

    score = max(0, 100 - issues * 30)
    status = _status(score)
    tip = "" if status == "good" else "Keep formatting consistent: use one date format, one bullet style, and past tense for previous roles."

    return {
        "name": "Consistency",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "low",
        "details": " · ".join(details),
    }


def _check_parsability(lines, word_count):
    """Check structural parsability — empty lines ratio, extreme line lengths, noise."""
    issues = 0
    details = []

    # Empty lines ratio
    empty = sum(1 for l in lines if not l.strip())
    total = max(len(lines), 1)
    empty_ratio = empty / total

    if empty_ratio > 0.4:
        issues += 1
        details.append("Too many blank lines")
    elif empty_ratio < 0.05 and total > 10:
        issues += 1
        details.append("No spacing between sections")
    else:
        details.append("Good spacing")

    # Very long lines (> 150 chars — may indicate paragraph blocks)
    long_lines = sum(1 for l in lines if len(l.strip()) > 150)
    if long_lines > 3:
        issues += 1
        details.append(f"{long_lines} overly long lines")
    else:
        details.append("Line lengths OK")

    # Header/footer noise (page numbers, "Page X of Y", repeated names at top/bottom)
    noise = len(re.findall(r"page\s+\d+\s+of\s+\d+|confidential|all rights reserved", " ".join(lines), re.IGNORECASE))
    if noise > 0:
        issues += 1
        details.append("Header/footer noise detected")
    else:
        details.append("Clean structure")

    score = max(0, 100 - issues * 25)
    status = _status(score)
    tip = "" if status == "good" else "Remove page headers/footers, avoid huge text blocks, and add spacing between sections."

    return {
        "name": "File Parsability",
        "score": score,
        "status": status,
        "tip": tip,
        "tip_priority": "low",
        "details": " · ".join(details),
    }
