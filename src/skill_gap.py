def normalize_skills(skills):
    """
    Converts skill names to lowercase and removes duplicates.
    """
    return list(dict.fromkeys(
        skill.strip().lower()
        for skill in skills
        if skill.strip()
    ))


def find_matched_skills(resume_skills, job_skills):
    """
    Finds skills that are present in both
    the resume and the job description.
    """

    resume_skills = normalize_skills(resume_skills)
    job_skills = normalize_skills(job_skills)

    return [
        skill for skill in job_skills
        if skill in resume_skills
    ]


def find_missing_skills(resume_skills, job_skills):
    """
    Finds skills required by the job description
    that are missing from the resume.
    """

    resume_skills = normalize_skills(resume_skills)
    job_skills = normalize_skills(job_skills)

    return [
        skill for skill in job_skills
        if skill not in resume_skills
    ]


def calculate_match_percentage(resume_skills, job_skills):
    """
    Calculates the percentage of job-required skills
    that are present in the resume.
    """

    job_skills = normalize_skills(job_skills)

    if not job_skills:
        return 0

    matched_skills = find_matched_skills(
        resume_skills,
        job_skills
    )

    percentage = (
        len(matched_skills) / len(job_skills)
    ) * 100

    return round(percentage, 2)