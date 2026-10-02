import os
import streamlit as st

from src.resume_parser import extract_resume_text
from src.skill_extractor import extract_skills
from src.skill_gap import (
    find_matched_skills,
    find_missing_skills,
    calculate_match_percentage
)


# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)


# Title
st.title("📄 AI Resume Analyzer")

st.write(
    "Compare your resume with a job description "
    "and identify matched and missing skills."
)


# Resume upload
uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)


# Job description
job_description = st.text_area(
    "📄 Paste Job Description",
    height=250,
    placeholder="Paste the job description here..."
)


# Analyze
if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully! ✅")

    if st.button("🔍 Analyze Resume"):

        if not job_description.strip():
            st.warning(
                "Please paste a job description before analyzing."
            )

        else:

            try:
                # Extract resume text
                resume_text = extract_resume_text(file_path)

                # Extract skills
                resume_skills = extract_skills(resume_text)
                job_skills = extract_skills(job_description)

                # Compare skills
                matched_skills = find_matched_skills(
                    resume_skills,
                    job_skills
                )

                missing_skills = find_missing_skills(
                    resume_skills,
                    job_skills
                )

                match_percentage = calculate_match_percentage(
                    resume_skills,
                    job_skills
                )

                # Match percentage
                st.subheader("📊 Skill Match Percentage")

                st.progress(int(match_percentage))

                st.write(
                    f"Your resume matches "
                    f"**{match_percentage}%** "
                    f"of the required job skills."
                )

                # Matched skills
                st.subheader("✅ Matched Skills")

                if matched_skills:

                    for skill in matched_skills:
                        st.write(f"• {skill}")

                else:
                    st.write("No matched skills found.")

                # Missing skills
                st.subheader("⚠️ Missing Skills")

                if missing_skills:

                    for skill in missing_skills:
                        st.write(f"• {skill}")

                else:
                    st.success(
                        "🎉 No required skills are missing!"
                    )

            except Exception as e:

                st.error(
                    f"An error occurred: {e}"
                )