from fastapi import FastAPI, UploadFile, File
from app.parser import extract_text
from .scoring import compute_match_score

app = FastAPI()

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    """Extracts text from uploaded resume"""
    resume_text = extract_text(file)
    return {"resume_text": resume_text}

@app.post("/get_score/")
async def get_score(resume: str, job_desc: str):
    """Compares resume and job description, then gives a match score"""
    result = compute_match_score(resume, job_desc)
    return {
        "match_score": result["match_score"],
        "missing_skills": result["missing_skills"]
    }
