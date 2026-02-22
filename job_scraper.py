"""
Job Scraper for CarrierIQ.
Fetches real job postings from LinkedIn (public scraping) and Adzuna (free API).
Returns top companies currently hiring for the candidate's skills.
"""

import os
import re
import json
import time
import random
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# ========== CONFIG ==========
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID", "")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY", "")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
]


def _get_headers():
    """Get randomized request headers to avoid detection."""
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }


def _build_search_query(target_role, skills, score=50):
    """
    Build a search query tailored to the candidate's score tier.

    - Score 0-39:  Search for "junior" or "intern" + role (entry-level)
    - Score 40-69: Search for the role directly (mid-level)
    - Score 70-84: Search for role directly (strong candidates)
    - Score 85+:   Search for "senior" + role (top-tier)
    """
    if target_role:
        role = target_role
    elif skills:
        role = " ".join(skills[:3])
    else:
        return "software developer"

    if score < 40:
        # Entry-level: search for junior/intern positions
        return f"junior {role}"
    elif score >= 85:
        # Top-tier: search for senior positions
        return f"senior {role}"
    else:
        # Mid-level: search for the role directly
        return role


def scrape_linkedin_jobs(skills, target_role="", location="India", max_results=5, score=50):
    """
    Scrape LinkedIn's public job search page for matching jobs.
    Search query is tailored based on candidate's score tier.

    Args:
        skills: List of skill strings
        target_role: Target job role
        location: Job location
        max_results: Max number of company results
        score: Candidate's skill score (0-100) for filtering

    Returns:
        List of dicts with: company, title, location, url, source
    """
    results = []

    try:
        # Build score-adjusted search query
        query = _build_search_query(target_role, skills, score)

        encoded_query = quote_plus(query)
        encoded_location = quote_plus(location)

        url = (
            f"https://www.linkedin.com/jobs/search/"
            f"?keywords={encoded_query}"
            f"&location={encoded_location}"
            f"&trk=public_jobs_jobs-search-bar_search-submit"
            f"&position=1&pageNum=0"
        )

        response = requests.get(url, headers=_get_headers(), timeout=10)

        if response.status_code != 200:
            print(f"[Job Scraper] LinkedIn returned status {response.status_code}")
            return results

        soup = BeautifulSoup(response.text, "html.parser")

        # LinkedIn public job cards
        job_cards = soup.find_all("div", class_="base-card")

        if not job_cards:
            # Try alternative selectors
            job_cards = soup.find_all("li", class_=re.compile(r"result-card"))

        seen_companies = set()

        for card in job_cards:
            if len(results) >= max_results:
                break

            try:
                # Extract job title
                title_el = card.find("h3", class_=re.compile(r"base-search-card__title"))
                title = title_el.get_text(strip=True) if title_el else ""

                # Extract company name
                company_el = card.find("h4", class_=re.compile(r"base-search-card__subtitle"))
                company = company_el.get_text(strip=True) if company_el else ""

                # Extract location
                loc_el = card.find("span", class_=re.compile(r"job-search-card__location"))
                loc = loc_el.get_text(strip=True) if loc_el else location

                # Extract URL
                link_el = card.find("a", class_=re.compile(r"base-card__full-link"))
                job_url = link_el["href"] if link_el and link_el.get("href") else ""

                if company and company not in seen_companies:
                    seen_companies.add(company)
                    results.append({
                        "company": company,
                        "title": title,
                        "location": loc,
                        "url": job_url.split("?")[0] if job_url else "",  # Clean URL
                        "salary": "",
                        "source": "LinkedIn"
                    })

            except Exception as e:
                print(f"[Job Scraper] Error parsing LinkedIn card: {e}")
                continue

    except requests.exceptions.Timeout:
        print("[Job Scraper] LinkedIn request timed out")
    except Exception as e:
        print(f"[Job Scraper] LinkedIn scraping error: {e}")

    return results


def fetch_adzuna_jobs(skills, target_role="", location="india", max_results=5, score=50):
    """
    Fetch job listings from Adzuna's free API.
    Search query is tailored based on candidate's score tier.

    Args:
        skills: List of skill strings
        target_role: Target job role
        location: Country for job search
        max_results: Max number of results
        score: Candidate's skill score (0-100) for filtering

    Returns:
        List of dicts with: company, title, location, url, salary, source
    """
    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        return []

    results = []

    try:
        # Build score-adjusted search query
        query = _build_search_query(target_role, skills, score)

        # Map common location names to Adzuna country codes
        country_map = {
            "india": "in",
            "united states": "us",
            "usa": "us",
            "uk": "gb",
            "united kingdom": "gb",
            "canada": "ca",
            "australia": "au",
            "germany": "de",
            "france": "fr",
        }
        country = country_map.get(location.lower().strip(), "in")

        url = (
            f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"
            f"?app_id={ADZUNA_APP_ID}"
            f"&app_key={ADZUNA_APP_KEY}"
            f"&results_per_page={max_results}"
            f"&what={quote_plus(query)}"
            f"&content-type=application/json"
        )

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"[Job Scraper] Adzuna returned status {response.status_code}")
            return results

        data = response.json()
        seen_companies = set()

        for job in data.get("results", []):
            company = job.get("company", {}).get("display_name", "Unknown")

            if company in seen_companies:
                continue
            seen_companies.add(company)

            # Format salary
            salary = ""
            salary_min = job.get("salary_min")
            salary_max = job.get("salary_max")
            if salary_min and salary_max:
                salary = f"${int(salary_min):,} - ${int(salary_max):,}"
            elif salary_min:
                salary = f"From ${int(salary_min):,}"

            results.append({
                "company": company,
                "title": job.get("title", ""),
                "location": job.get("location", {}).get("display_name", ""),
                "url": job.get("redirect_url", ""),
                "salary": salary,
                "source": "Adzuna"
            })

            if len(results) >= max_results:
                break

    except requests.exceptions.Timeout:
        print("[Job Scraper] Adzuna request timed out")
    except Exception as e:
        print(f"[Job Scraper] Adzuna error: {e}")

    return results


def search_jobs(skills, target_role="", location="India", max_results=5, score=50):
    """
    Search for jobs across all available sources.
    Merges results from LinkedIn and Adzuna, deduplicating by company name.
    Results are tailored to the candidate's score tier.

    Args:
        skills: List of skill strings or comma-separated string
        target_role: Target job role
        location: Job location
        max_results: Max total results
        score: Candidate's skill score (0-100) for tier-based filtering

    Returns:
        List of dicts with: company, title, location, url, salary, source
    """
    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(",") if s.strip()]

    all_results = []
    seen_companies = set()

    # Source 1: LinkedIn (score-adjusted query)
    try:
        linkedin_results = scrape_linkedin_jobs(
            skills, target_role, location, max_results=max_results, score=score
        )
        for job in linkedin_results:
            if job["company"].lower() not in seen_companies:
                seen_companies.add(job["company"].lower())
                all_results.append(job)
    except Exception as e:
        print(f"[Job Scraper] LinkedIn source failed: {e}")

    # Source 2: Adzuna (if configured, also score-adjusted)
    if len(all_results) < max_results:
        try:
            adzuna_results = fetch_adzuna_jobs(
                skills, target_role, location,
                max_results=max_results - len(all_results),
                score=score
            )
            for job in adzuna_results:
                if job["company"].lower() not in seen_companies:
                    seen_companies.add(job["company"].lower())
                    all_results.append(job)
        except Exception as e:
            print(f"[Job Scraper] Adzuna source failed: {e}")

    return all_results[:max_results]
