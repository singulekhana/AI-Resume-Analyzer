from src.resume_parser import extract_resume_text
from src.skill_extractor import extract_skills
from src.skill_gap import find_missing_skills 

def main():
    print("AI Resume Analyzer")
    print("------------------")

    file_path = input("Enter resume file path: ")

    try:
        resume_text = extract_resume_text(file_path)

        skills = extract_skills(resume_text)
        print("\nSkills Found:")
        for skill in skills:
            print("-", skill)

        missing_skills = find_missing_skills(skills)

        print("\nMissing Skills:")
        for skill in missing_skills:
            print("-", skill)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()