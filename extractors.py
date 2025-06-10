import re
from dateutil import parser as date_parser
from datetime import datetime
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group() if match else "Not Found"

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3})?\s*[\(]?\d{3}[\)]?[\s\-]?\d{3}[\s\-]?\d{4}', text)
    return match.group() if match else "Not Found"

def extract_name(text):
    
   # Split into lines and clean
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Keywords to skip (common degree/edu words)
    skip_keywords = ['computer science', 'bachelor', 'master', 'university', 'degree', 'education', 'profile', 'summary', 'email']
    
    # Regex for simple full name: 2-3 words starting with capital letters
    name_pattern = re.compile(r'^([A-Z][a-z]+)(\s[A-Z][a-z]+){1,2}$')

    for line in lines[:10]:  # Check first 10 lines only (top of resume)
        lower_line = line.lower()
        if any(word in lower_line for word in skip_keywords):
            continue
        if name_pattern.match(line):
            return line
    
    # fallback: return first line if no match found
    return lines[0] if lines else None

def extract_skills(text, skill_list):
    found_skills = set()
    text_lower = text.lower()
    for skill in skill_list:
        if skill.lower() in text_lower:
            found_skills.add(skill)
    return (found_skills) if found_skills else "Not Found"

def extract_experience(text):
   
    match = re.search(r'(Work Experience|Professional Experience|Employment History)', text, re.I)
    if not match:
        return "0 years"

    start = match.end()
    # Stop at next section heading if present
    end_match = re.search(r'(Education|Skills|Projects|Certifications)', text[start:], re.I)
    end = start + end_match.start() if end_match else len(text)

    work_text = text[start:end]

    # Regex to find all date ranges like "January 2015 - current" or "April 2012 to January 2015"
    date_ranges = re.findall(r'(\w+\s+\d{4})\s*[-–to]+\s*(\w+\s+\d{4}|present|current)', work_text, re.I)

    total_days = 0

    for start_str, end_str in date_ranges:
        try:
            start_date = date_parser.parse(start_str, fuzzy=True)
        except Exception:
            continue

        end_str = end_str.lower()
        if end_str in ['present', 'current']:
            end_date = datetime.now()
        else:
            try:
                end_date = date_parser.parse(end_str, fuzzy=True)
            except Exception:
                continue

        if end_date > start_date:
            total_days += (end_date - start_date).days

    # Convert total days into years and months
    years = total_days // 365
    months = (total_days % 365) // 30

    # Formatting output string
    year_str = f"{int(years)} year{'s' if years != 1 else ''}" if years else ""
    month_str = f"{int(months)} month{'s' if months != 1 else ''}" if months else ""

    if years and months:
        return f"{year_str} and {month_str}"
    elif years:
        return year_str
    elif months:
        return month_str
    else:
        return "0 months"
