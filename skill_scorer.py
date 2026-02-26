"""
Local Skill Scoring Engine for CarrierIQ.
Scores candidate skills against role requirements using fuzzy matching.
"""

from difflib import SequenceMatcher

# Role-Skill Database
# Each role has skills in 3 tiers: core (3x weight), important (2x), nice (1x)

ROLE_SKILLS = {
    "data scientist": {
        "core": ["python", "machine learning", "statistics", "data analysis", "sql"],
        "important": ["deep learning", "pandas", "numpy", "scikit-learn", "data visualization",
                       "tensorflow", "pytorch", "nlp", "r", "jupyter"],
        "nice": ["spark", "hadoop", "aws", "docker", "git", "tableau", "power bi",
                 "keras", "matplotlib", "seaborn", "feature engineering", "a/b testing"]
    },
    "data analyst": {
        "core": ["sql", "excel", "data analysis", "python", "data visualization"],
        "important": ["tableau", "power bi", "pandas", "statistics", "r",
                       "google analytics", "reporting", "dashboard"],
        "nice": ["machine learning", "jupyter", "vba", "looker", "dax",
                 "etl", "data warehousing", "bigquery"]
    },
    "web developer": {
        "core": ["html", "css", "javascript", "responsive design", "git"],
        "important": ["react", "node.js", "typescript", "rest api", "sql",
                       "mongodb", "sass", "webpack", "tailwind css"],
        "nice": ["next.js", "vue.js", "angular", "graphql", "docker", "aws",
                 "firebase", "redis", "ci/cd", "testing", "figma"]
    },
    "frontend developer": {
        "core": ["html", "css", "javascript", "react", "responsive design"],
        "important": ["typescript", "redux", "sass", "webpack", "git",
                       "tailwind css", "next.js", "figma", "rest api"],
        "nice": ["vue.js", "angular", "graphql", "testing", "storybook",
                 "accessibility", "performance optimization", "pwa"]
    },
    "backend developer": {
        "core": ["python", "sql", "rest api", "git", "databases"],
        "important": ["node.js", "java", "docker", "postgresql", "mongodb",
                       "redis", "microservices", "linux", "aws"],
        "nice": ["kubernetes", "graphql", "rabbitmq", "kafka", "ci/cd",
                 "terraform", "nginx", "elasticsearch", "grpc"]
    },
    "full stack developer": {
        "core": ["html", "css", "javascript", "python", "sql", "git"],
        "important": ["react", "node.js", "rest api", "mongodb", "docker",
                       "typescript", "postgresql", "aws"],
        "nice": ["next.js", "graphql", "redis", "kubernetes", "ci/cd",
                 "tailwind css", "firebase", "testing"]
    },
    "software engineer": {
        "core": ["data structures", "algorithms", "python", "git", "oop"],
        "important": ["system design", "sql", "java", "c++", "linux",
                       "rest api", "docker", "testing", "databases"],
        "nice": ["kubernetes", "aws", "microservices", "ci/cd", "agile",
                 "design patterns", "distributed systems", "golang"]
    },
    "machine learning engineer": {
        "core": ["python", "machine learning", "deep learning", "tensorflow", "mathematics"],
        "important": ["pytorch", "scikit-learn", "nlp", "computer vision", "sql",
                       "docker", "mlops", "feature engineering", "pandas"],
        "nice": ["kubernetes", "spark", "aws sagemaker", "kubeflow", "onnx",
                 "model optimization", "a/b testing", "rust"]
    },
    "devops engineer": {
        "core": ["linux", "docker", "ci/cd", "aws", "git"],
        "important": ["kubernetes", "terraform", "ansible", "jenkins", "python",
                       "monitoring", "networking", "bash scripting"],
        "nice": ["prometheus", "grafana", "helm", "argocd", "gcp", "azure",
                 "security", "istio", "pulumi"]
    },
    "cloud engineer": {
        "core": ["aws", "linux", "networking", "docker", "security"],
        "important": ["terraform", "kubernetes", "ci/cd", "python", "gcp",
                       "azure", "iam", "serverless", "monitoring"],
        "nice": ["cloudformation", "ansible", "cost optimization", "compliance",
                 "databricks", "snowflake", "kafka"]
    },
    "mobile developer": {
        "core": ["java", "kotlin", "swift", "mobile ui", "git"],
        "important": ["react native", "flutter", "rest api", "firebase",
                       "android sdk", "ios sdk", "sql"],
        "nice": ["graphql", "ci/cd", "testing", "push notifications",
                 "app store optimization", "redux", "typescript"]
    },
    "android developer": {
        "core": ["java", "kotlin", "android sdk", "xml", "git"],
        "important": ["jetpack compose", "mvvm", "rest api", "firebase",
                       "room database", "coroutines", "material design"],
        "nice": ["flutter", "ci/cd", "testing", "dagger/hilt", "graphql",
                 "app performance", "kotlin multiplatform"]
    },
    "ios developer": {
        "core": ["swift", "xcode", "uikit", "ios sdk", "git"],
        "important": ["swiftui", "core data", "rest api", "cocoapods",
                       "mvvm", "auto layout", "combine"],
        "nice": ["objective-c", "firebase", "ci/cd", "testing", "arkit",
                 "core ml", "app store connect"]
    },
    "cybersecurity analyst": {
        "core": ["network security", "linux", "firewalls", "incident response", "siem"],
        "important": ["penetration testing", "vulnerability assessment", "python",
                       "encryption", "compliance", "ids/ips", "malware analysis"],
        "nice": ["aws security", "forensics", "threat intelligence", "splunk",
                 "wireshark", "burp suite", "oscp"]
    },
    "ui/ux designer": {
        "core": ["figma", "user research", "wireframing", "prototyping", "usability testing"],
        "important": ["adobe xd", "sketch", "design systems", "information architecture",
                       "interaction design", "accessibility", "html", "css"],
        "nice": ["motion design", "illustration", "after effects", "framer",
                 "analytics", "a/b testing", "branding"]
    },
    "product manager": {
        "core": ["product strategy", "roadmapping", "user research", "data analysis", "agile"],
        "important": ["jira", "sql", "a/b testing", "stakeholder management",
                       "market research", "wireframing", "okrs"],
        "nice": ["python", "tableau", "figma", "pricing strategy", "go-to-market",
                 "competitive analysis", "technical writing"]
    },
    "data engineer": {
        "core": ["sql", "python", "etl", "data warehousing", "spark"],
        "important": ["airflow", "kafka", "aws", "snowflake", "databricks",
                       "hadoop", "docker", "data modeling"],
        "nice": ["kubernetes", "dbt", "flink", "terraform", "ci/cd",
                 "scala", "bigquery", "redshift"]
    },
    "ai engineer": {
        "core": ["python", "machine learning", "deep learning", "nlp", "mathematics"],
        "important": ["tensorflow", "pytorch", "transformers", "langchain", "llm",
                       "computer vision", "mlops", "docker"],
        "nice": ["rust", "cuda", "onnx", "kubernetes", "aws", "vector databases",
                 "reinforcement learning", "generative ai"]
    },
    "business analyst": {
        "core": ["data analysis", "sql", "excel", "requirements gathering", "reporting"],
        "important": ["tableau", "power bi", "jira", "agile", "process mapping",
                       "stakeholder management", "documentation"],
        "nice": ["python", "r", "uml", "erp systems", "sap", "salesforce",
                 "data modeling", "six sigma"]
    },
    "qa engineer": {
        "core": ["testing", "test automation", "selenium", "bug tracking", "sql"],
        "important": ["python", "java", "api testing", "jira", "git",
                       "performance testing", "ci/cd", "agile"],
        "nice": ["cypress", "playwright", "k6", "docker", "mobile testing",
                 "security testing", "testng", "cucumber"]
    },

    # ── Mechanical Engineering ─────────────────────────────────────────────
    "mechanical design engineer": {
        "core": ["solidworks", "autocad", "mechanical design", "gd&t", "manufacturing processes"],
        "important": ["fea", "ansys", "catia", "thermodynamics", "material science",
                       "3d printing", "creo", "tolerance analysis"],
        "nice": ["python", "matlab", "six sigma", "lean manufacturing", "plm",
                 "sheet metal design", "injection molding", "dfm/dfa"]
    },
    "robotics engineer": {
        "core": ["python", "ros", "c++", "control systems", "kinematics"],
        "important": ["sensors", "actuators", "embedded systems", "matlab", "computer vision",
                       "linux", "solidworks", "plc programming"],
        "nice": ["deep learning", "slam", "gazebo", "opencv", "tensorflow",
                 "reinforcement learning", "pcb design", "arduino"]
    },

    # ── Electrical & Electronics Engineering ───────────────────────────────
    "embedded systems engineer": {
        "core": ["c", "c++", "microcontrollers", "rtos", "embedded linux"],
        "important": ["arm", "pcb design", "uart", "spi", "i2c",
                       "debugging", "firmware", "oscilloscope"],
        "nice": ["python", "fpga", "ble", "can bus", "iot",
                 "freertos", "zephyr", "device drivers"]
    },
    "vlsi design engineer": {
        "core": ["verilog", "vhdl", "digital design", "fpga", "asic design"],
        "important": ["cadence", "synopsys", "sta", "synthesis", "floorplanning",
                       "dft", "low power design", "clock tree synthesis"],
        "nice": ["tcl scripting", "perl", "python", "uvm", "system verilog",
                 "analog design", "spice", "layout design"]
    },
    "iot engineer": {
        "core": ["python", "embedded c", "sensors", "mqtt", "cloud platforms"],
        "important": ["raspberry pi", "arduino", "aws iot", "ble", "wifi",
                       "node.js", "edge computing", "pcb design"],
        "nice": ["machine learning", "docker", "grafana", "influxdb", "lorawan",
                 "zigbee", "tensorflow lite", "security"]
    },
    "electrical design engineer": {
        "core": ["autocad electrical", "circuit design", "power systems", "plc programming", "electrical safety"],
        "important": ["scada", "hmi", "motor drives", "transformers", "relay protection",
                       "iec standards", "eplan", "matlab"],
        "nice": ["python", "embedded systems", "renewable energy", "power electronics",
                 "ethernet/ip", "modbus", "siemens tia portal", "allen bradley"]
    },

    # ── Civil Engineering ──────────────────────────────────────────────────
    "structural engineer": {
        "core": ["staad pro", "etabs", "autocad", "structural analysis", "concrete design"],
        "important": ["steel design", "revit", "sap2000", "foundation design", "earthquake engineering",
                       "is codes", "quantity surveying", "primavera"],
        "nice": ["python", "bim", "tekla", "safe", "ansys",
                 "cost estimation", "ms project", "3d modeling"]
    },
    "construction manager": {
        "core": ["project management", "autocad", "cost estimation", "scheduling", "construction methods"],
        "important": ["primavera", "ms project", "bim", "revit", "quantity surveying",
                       "contract management", "safety management", "quality control"],
        "nice": ["lean construction", "python", "gis", "drone surveying",
                 "leed certification", "six sigma", "erp systems", "stakeholder management"]
    },

    # ── Additional IT Roles ────────────────────────────────────────────────
    "blockchain developer": {
        "core": ["solidity", "ethereum", "smart contracts", "web3.js", "javascript"],
        "important": ["react", "node.js", "truffle", "hardhat", "defi",
                       "cryptography", "ipfs", "git"],
        "nice": ["rust", "golang", "layer 2", "nft", "dao",
                 "hyperledger", "polkadot", "security auditing"]
    },
    "game developer": {
        "core": ["unity", "c#", "game design", "3d math", "physics engine"],
        "important": ["unreal engine", "c++", "shader programming", "animation", "git",
                       "blender", "ai programming", "multiplayer networking"],
        "nice": ["ar/vr", "procedural generation", "mobile games", "steam sdk",
                 "sound design", "ue blueprints", "godot", "playtesting"]
    },
    "network engineer": {
        "core": ["networking", "cisco", "routing", "switching", "firewalls"],
        "important": ["tcp/ip", "vpn", "dns", "dhcp", "linux",
                       "wireshark", "subnetting", "load balancing"],
        "nice": ["python", "ansible", "sd-wan", "cloud networking", "ccnp",
                 "network automation", "ipv6", "bgp"]
    },
    "database administrator": {
        "core": ["sql", "database design", "backup and recovery", "performance tuning", "security"],
        "important": ["oracle", "sql server", "postgresql", "mysql", "replication",
                       "indexing", "query optimization", "monitoring"],
        "nice": ["python", "mongodb", "redis", "cloud databases", "automation",
                 "data modeling", "etl", "high availability"]
    },
    "technical writer": {
        "core": ["technical writing", "documentation", "api documentation", "markdown", "content strategy"],
        "important": ["git", "html", "css", "swagger", "jira",
                       "confluence", "information architecture", "editing"],
        "nice": ["python", "javascript", "dita", "readthedocs", "postman",
                 "seo", "video scripting", "ux writing"]
    },

    # ── Interdisciplinary Engineering ──────────────────────────────────────
    "biomedical engineer": {
        "core": ["matlab", "signal processing", "medical devices", "biology", "physiology"],
        "important": ["python", "fda regulations", "biomechanics", "medical imaging", "statistics",
                       "labview", "solidworks", "clinical trials"],
        "nice": ["machine learning", "deep learning", "3d printing", "arduino",
                 "r", "bioinformatics", "iso 13485", "risk management"]
    },
    "environmental engineer": {
        "core": ["wastewater treatment", "environmental impact assessment", "air quality", "gis", "sustainability"],
        "important": ["autocad", "water resources", "solid waste management", "eia regulations", "python",
                       "remote sensing", "environmental monitoring", "hse"],
        "nice": ["matlab", "qgis", "climate modeling", "renewable energy",
                 "iso 14001", "life cycle assessment", "carbon footprint", "data analysis"]
    },
}

# Company Tiers (Fallback)
COMPANY_TIERS = {
    "high": [
        {"name": "Google", "type": "Top Tech", "careers_url": "https://careers.google.com"},
        {"name": "Microsoft", "type": "Top Tech", "careers_url": "https://careers.microsoft.com"},
        {"name": "Amazon", "type": "Top Tech", "careers_url": "https://www.amazon.jobs"},
        {"name": "Apple", "type": "Top Tech", "careers_url": "https://jobs.apple.com"},
        {"name": "Meta", "type": "Top Tech", "careers_url": "https://www.metacareers.com"},
        {"name": "Netflix", "type": "Top Tech", "careers_url": "https://jobs.netflix.com"},
    ],
    "mid": [
        {"name": "TCS", "type": "IT Services", "careers_url": "https://www.tcs.com/careers"},
        {"name": "Infosys", "type": "IT Services", "careers_url": "https://www.infosys.com/careers"},
        {"name": "Wipro", "type": "IT Services", "careers_url": "https://careers.wipro.com"},
        {"name": "Accenture", "type": "Consulting", "careers_url": "https://www.accenture.com/careers"},
        {"name": "Cognizant", "type": "IT Services", "careers_url": "https://careers.cognizant.com"},
        {"name": "Capgemini", "type": "Consulting", "careers_url": "https://www.capgemini.com/careers"},
    ],
    "entry": [
        {"name": "Internshala", "type": "Internships", "careers_url": "https://internshala.com"},
        {"name": "AngelList", "type": "Startups", "careers_url": "https://angel.co/jobs"},
        {"name": "Freshworks", "type": "Startup", "careers_url": "https://www.freshworks.com/company/careers"},
        {"name": "Zoho", "type": "Product Company", "careers_url": "https://www.zoho.com/careers.html"},
        {"name": "Razorpay", "type": "Fintech", "careers_url": "https://razorpay.com/jobs"},
        {"name": "Swiggy", "type": "Startup", "careers_url": "https://careers.swiggy.com"},
    ],
}


def _normalize(skill):
    """Normalize a skill string for comparison."""
    return skill.lower().strip().replace("-", " ").replace("_", " ")


def _fuzzy_match(user_skill, required_skill, threshold=0.7):
    """Check if two skills match using fuzzy string matching."""
    u = _normalize(user_skill)
    r = _normalize(required_skill)

    # Exact match
    if u == r:
        return True

    # Substring match (e.g., "ml" in "machine learning" won't match, but "react.js" ~ "react")
    if len(u) > 2 and len(r) > 2:
        if u in r or r in u:
            return True

    # Common abbreviations
    abbreviations = {
        "ml": "machine learning",
        "dl": "deep learning",
        "ds": "data structures",
        "dsa": "data structures",
        "algo": "algorithms",
        "js": "javascript",
        "ts": "typescript",
        "py": "python",
        "ai": "artificial intelligence",
        "nlp": "natural language processing",
        "cv": "computer vision",
        "k8s": "kubernetes",
        "tf": "tensorflow",
        "aws": "amazon web services",
        "gcp": "google cloud platform",
        "oop": "object oriented programming",
        "ci/cd": "continuous integration",
        "react.js": "react",
        "reactjs": "react",
        "node": "node.js",
        "nodejs": "node.js",
        "vue": "vue.js",
        "vuejs": "vue.js",
        "express": "express.js",
        "expressjs": "express.js",
        "postgres": "postgresql",
        "mongo": "mongodb",
    }

    u_expanded = abbreviations.get(u, u)
    r_expanded = abbreviations.get(r, r)

    if u_expanded == r_expanded:
        return True
    if u_expanded == r or u == r_expanded:
        return True

    # SequenceMatcher for fuzzy comparison
    ratio = SequenceMatcher(None, u, r).ratio()
    return ratio >= threshold


def _parse_skills(skills_input):
    """Parse skills from a comma-separated string or list."""
    if isinstance(skills_input, list):
        return [s.strip() for s in skills_input if s.strip()]
    return [s.strip() for s in skills_input.split(",") if s.strip()]


def _find_best_role(user_skills):
    """Find the best matching role for a set of user skills."""
    best_role = None
    best_score = -1

    for role, categories in ROLE_SKILLS.items():
        all_skills = categories["core"] + categories["important"] + categories["nice"]
        matches = 0
        for us in user_skills:
            for rs in all_skills:
                if _fuzzy_match(us, rs):
                    matches += 1
                    break
        if matches > best_score:
            best_score = matches
            best_role = role

    return best_role


def score_skills(user_skills_input, target_role=""):
    """
    Score user skills against a target role.

    Args:
        user_skills_input: Comma-separated skills string or list
        target_role: Target job role (auto-detected if empty)

    Returns:
        dict with: score, matched_skills, missing_skills, suggestions,
                   ai_summary, target_role, skill_breakdown, company_tier
    """
    user_skills = _parse_skills(user_skills_input)

    if not user_skills:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "suggestions": ["Please enter at least one skill to get an analysis."],
            "ai_summary": "No skills were provided for analysis.",
            "target_role": target_role or "General",
            "skill_breakdown": {"core": [], "important": [], "nice": []},
            "company_tier": "entry"
        }

    # Determine or validate target role
    role_key = _normalize(target_role) if target_role else ""

    if role_key not in ROLE_SKILLS:
        # Try fuzzy matching the role name
        for r in ROLE_SKILLS:
            if _fuzzy_match(role_key, r, threshold=0.6):
                role_key = r
                break
        else:
            # Auto-detect best role
            role_key = _find_best_role(user_skills)

    if not role_key or role_key not in ROLE_SKILLS:
        role_key = "software engineer"  # safe default

    role_data = ROLE_SKILLS[role_key]

    # Match skills against each category
    matched = {"core": [], "important": [], "nice": []}
    missing = {"core": [], "important": [], "nice": []}

    for category in ["core", "important", "nice"]:
        for required_skill in role_data[category]:
            found = False
            for user_skill in user_skills:
                if _fuzzy_match(user_skill, required_skill):
                    matched[category].append(required_skill.title())
                    found = True
                    break
            if not found:
                missing[category].append(required_skill.title())

    # Calculate weighted score
    weights = {"core": 3, "important": 2, "nice": 1}
    total_weight = 0
    earned_weight = 0

    for category in ["core", "important", "nice"]:
        total_skills = len(role_data[category])
        matched_count = len(matched[category])
        total_weight += total_skills * weights[category]
        earned_weight += matched_count * weights[category]

    score = round((earned_weight / total_weight) * 100) if total_weight > 0 else 0

    # Flatten for backward compatibility
    all_matched = matched["core"] + matched["important"] + matched["nice"]
    all_missing = missing["core"] + missing["important"] + missing["nice"]

    # Determine company tier
    if score >= 85:
        company_tier = "high"
    elif score >= 55:
        company_tier = "mid"
    else:
        company_tier = "entry"

    # Generate suggestions
    suggestions = _generate_suggestions(matched, missing, score, role_key)

    # Generate AI summary
    ai_summary = _generate_summary(score, role_key, matched, missing)

    return {
        "score": score,
        "matched_skills": all_matched,
        "missing_skills": all_missing,
        "suggestions": suggestions,
        "ai_summary": ai_summary,
        "target_role": role_key.title(),
        "skill_breakdown": {
            "core_matched": matched["core"],
            "core_missing": missing["core"],
            "important_matched": matched["important"],
            "important_missing": missing["important"],
            "nice_matched": matched["nice"],
            "nice_missing": missing["nice"],
        },
        "company_tier": company_tier
    }


def find_best_roles(user_skills_input):
    """
    Score user skills against ALL roles and return ranked matches.

    Args:
        user_skills_input: Comma-separated skills string or list

    Returns:
        list of dicts: [{role, score, matched, missing, total, category}, ...]
        sorted by score descending
    """
    user_skills = _parse_skills(user_skills_input)

    if not user_skills:
        return []

    # Category labels for each role
    role_categories = {
        "mechanical design engineer": "Mechanical Engineering",
        "robotics engineer": "Mechanical Engineering",
        "embedded systems engineer": "Electronics Engineering",
        "vlsi design engineer": "Electronics Engineering",
        "iot engineer": "Electronics Engineering",
        "electrical design engineer": "Electrical Engineering",
        "structural engineer": "Civil Engineering",
        "construction manager": "Civil Engineering",
        "blockchain developer": "IT / Software",
        "game developer": "IT / Software",
        "network engineer": "IT / Networking",
        "database administrator": "IT / Software",
        "technical writer": "IT / Content",
        "biomedical engineer": "Biomedical Engineering",
        "environmental engineer": "Environmental Engineering",
    }

    results = []

    for role_key, role_data in ROLE_SKILLS.items():
        weights = {"core": 3, "important": 2, "nice": 1}
        total_weight = 0
        earned_weight = 0
        matched_count = 0
        total_count = 0

        for category in ["core", "important", "nice"]:
            for required_skill in role_data[category]:
                total_count += 1
                total_weight += weights[category]
                for user_skill in user_skills:
                    if _fuzzy_match(user_skill, required_skill):
                        earned_weight += weights[category]
                        matched_count += 1
                        break

        score = round((earned_weight / total_weight) * 100) if total_weight > 0 else 0

        # Default category for roles not in the map
        category = role_categories.get(role_key, "IT / Software")

        results.append({
            "role": role_key.title(),
            "score": score,
            "matched": matched_count,
            "total": total_count,
            "missing": total_count - matched_count,
            "category": category,
        })

    # Sort by score descending, then by role name
    results.sort(key=lambda x: (-x["score"], x["role"]))

    return results


def _generate_suggestions(matched, missing, score, role):
    """Generate personalized improvement suggestions."""
    suggestions = []
    role_title = role.title()

    # Priority: missing core skills first
    if missing["core"]:
        top_missing = ", ".join(missing["core"][:3])
        suggestions.append(
            f"🔴 Critical: Learn {top_missing} — these are must-have skills for a {role_title}."
        )

    if missing["important"]:
        top_missing = ", ".join(missing["important"][:2])
        suggestions.append(
            f"🟡 Important: Add {top_missing} to strengthen your profile significantly."
        )

    if score < 40:
        suggestions.append(
            f"📚 Consider taking a structured course or bootcamp focused on {role_title} fundamentals."
        )
    elif score < 70:
        suggestions.append(
            "💻 Build 2-3 portfolio projects showcasing your skills to stand out to employers."
        )
    else:
        suggestions.append(
            "🚀 Great foundation! Focus on real-world projects and open-source contributions to reach top-tier level."
        )

    if not matched["nice"] and missing["nice"]:
        bonus_skill = missing["nice"][0]
        suggestions.append(
            f"✨ Bonus: Learning {bonus_skill} would give you an extra edge over other candidates."
        )

    # Always add a general suggestion
    if score < 85:
        suggestions.append(
            "📝 Tailor your resume to highlight skills most relevant to your target role."
        )

    return suggestions[:5]


def _generate_summary(score, role, matched, missing):
    """Generate a human-readable AI verdict."""
    role_title = role.title()
    total_matched = len(matched["core"]) + len(matched["important"]) + len(matched["nice"])
    core_coverage = len(matched["core"]) / max(len(matched["core"]) + len(missing["core"]), 1)

    if score >= 85:
        return (
            f"Excellent profile for {role_title}! You have strong coverage of core and advanced skills. "
            f"You're well-positioned for top-tier companies."
        )
    elif score >= 70:
        return (
            f"Strong profile for {role_title} with {total_matched} relevant skills matched. "
            f"Fill a few skill gaps to reach the next level."
        )
    elif score >= 50:
        if core_coverage >= 0.6:
            return (
                f"Good foundation for {role_title} — core skills are mostly covered. "
                f"Focus on building important complementary skills."
            )
        else:
            return (
                f"Moderate match for {role_title}. Several core skills are missing — "
                f"prioritize learning these to become a competitive candidate."
            )
    elif score >= 30:
        return (
            f"Early-stage profile for {role_title}. You have some relevant skills, "
            f"but need to develop core competencies. Consider structured learning paths."
        )
    else:
        return (
            f"Your current skills have limited overlap with {role_title} requirements. "
            f"Start with foundational skills and build up progressively."
        )


def get_fallback_companies(company_tier, count=5):
    """Get fallback company recommendations based on score tier."""
    companies = COMPANY_TIERS.get(company_tier, COMPANY_TIERS["entry"])
    return companies[:count]


def calculate_company_eligibility(candidate_score, job_title=""):
    """
    Calculate how eligible a candidate is for a specific company/role.

    Uses the candidate's overall score and the job title to determine
    a match percentage. Considers seniority level from the title.

    Args:
        candidate_score: int (0-100), the candidate's skill score
        job_title: str, the job posting title

    Returns:
        int (0-100), eligibility percentage for this company
    """
    title_lower = job_title.lower() if job_title else ""

    # Detect job level from title keywords
    is_intern = any(kw in title_lower for kw in ["intern", "trainee", "apprentice", "fresher"])
    is_junior = any(kw in title_lower for kw in ["junior", "jr", "entry", "associate", "graduate"])
    is_senior = any(kw in title_lower for kw in ["senior", "sr", "lead", "principal", "staff", "architect", "head", "director", "vp"])
    is_mid = not is_intern and not is_junior and not is_senior

    # Calculate eligibility based on how well score matches job level
    if is_intern:
        # Internships: best for low-scoring candidates
        if candidate_score <= 30:
            eligibility = 85 + min(candidate_score, 15)  # 85-100%
        elif candidate_score <= 50:
            eligibility = 70 + (50 - candidate_score)     # 70-90%
        else:
            eligibility = max(50, 90 - candidate_score)    # Overqualified

    elif is_junior:
        # Junior roles: best for 20-50 score range
        if candidate_score <= 20:
            eligibility = 55 + candidate_score             # 55-75%
        elif candidate_score <= 50:
            eligibility = 75 + min((candidate_score - 20), 20)  # 75-95%
        elif candidate_score <= 70:
            eligibility = 85 - (candidate_score - 50)      # Slightly overqualified
        else:
            eligibility = max(40, 75 - candidate_score)     # Overqualified

    elif is_senior:
        # Senior roles: best for 75+ score range
        if candidate_score >= 85:
            eligibility = 85 + min(candidate_score - 85, 15)  # 85-100%
        elif candidate_score >= 70:
            eligibility = 65 + (candidate_score - 70)          # 65-80%
        elif candidate_score >= 50:
            eligibility = 40 + (candidate_score - 50)          # 40-60%
        else:
            eligibility = max(15, candidate_score)              # Too junior

    else:
        # Mid-level (no seniority keyword): best for 40-80 score range
        if candidate_score <= 30:
            eligibility = 40 + candidate_score                  # 40-70%
        elif candidate_score <= 60:
            eligibility = 65 + min((candidate_score - 30), 25)  # 65-90%
        elif candidate_score <= 85:
            eligibility = 80 + min((candidate_score - 60), 15)  # 80-95%
        else:
            eligibility = 90 + min((candidate_score - 85), 10)  # 90-100%

    return max(10, min(100, eligibility))


def extract_skills_from_text(text):
    """
    Extract potential skills from resume/profile text by matching
    against the known skill database.
    """
    if not text:
        return []

    text_lower = text.lower()
    found_skills = set()

    # Collect all known skills
    all_skills = set()
    for role_data in ROLE_SKILLS.values():
        for category in ["core", "important", "nice"]:
            all_skills.update(role_data[category])

    for skill in all_skills:
        # Check if skill appears in the text (word boundary matching)
        skill_lower = skill.lower()
        if skill_lower in text_lower:
            found_skills.add(skill.title())

    return sorted(list(found_skills))
