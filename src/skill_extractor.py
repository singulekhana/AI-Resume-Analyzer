import re


# Canonical skill names and common ways they may appear
SKILL_ALIASES = {
    "python": ["python"],
    "java": ["java"],
    "c++": ["c++", "cpp"],
    "c": ["c"],
    "sql": ["sql"],
    "excel": ["excel", "microsoft excel"],
    "power bi": ["power bi", "powerbi", "microsoft power bi"],
    "tableau": ["tableau"],
    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "java script"],
    "react": ["react", "react.js", "reactjs"],
    "django": ["django"],
    "flask": ["flask"],
    "fastapi": ["fastapi"],
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "data analysis": ["data analysis", "data analytics"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "git": ["git"],
    "github": ["github", "git hub"],
    "mongodb": ["mongodb", "mongo db"],
    "mysql": ["mysql", "my sql"],
    "statistics": ["statistics", "statistical analysis"],
    "api testing": ["api testing"],
    "selenium": ["selenium"],
    "automation testing": ["automation testing", "test automation"],
    "manual testing": ["manual testing"],
    "software testing": ["software testing"],
    "sdlc": ["sdlc", "software development life cycle"],
    "stlc": ["stlc", "software testing life cycle"],
}


def contains_skill(text, skill_name, aliases):
    """
    Checks whether a skill appears as a complete word/phrase.
    Prevents accidental matches such as C inside 'computer'.
    """

    for alias in aliases:
        pattern = r"(?<![a-zA-Z0-9+#])" + re.escape(alias) + r"(?![a-zA-Z0-9+#])"

        if re.search(pattern, text, re.IGNORECASE):
            return True

    return False


def extract_skills(text):
    """
    Extracts recognized technical skills from text.
    Returns canonical skill names.
    """

    if not text:
        return []

    text = text.lower()

    found_skills = []

    for skill, aliases in SKILL_ALIASES.items():
        if contains_skill(text, skill, aliases):
            found_skills.append(skill)

    return found_skills