# AI Resume Analyzer

An AI-powered resume analysis web application that compares a candidate's resume with a job description and identifies matched and missing skills.

## Features

- Upload resume in PDF format
- Paste a job description
- Extract skills from resume and job description
- Identify matched skills
- Identify missing skills
- Calculate skill match percentage
- Simple and user-friendly Streamlit interface

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- NLP / Regex-based skill extraction
- HTML/CSS through Streamlit

## Project Structure

AI-Resume-Analyzer/
│
├── src/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   └── skill_gap.py
│
├── uploads/
├── data/
├── app.py
├── web_app.py
├── requirements.txt
├── README.md
└── .gitignore

## How It Works

Resume PDF + Job Description
        ↓
Text Extraction
        ↓
Skill Extraction
        ↓
Skill Comparison
        ↓
Matched Skills + Missing Skills
        ↓
Match Percentage

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt