# 📄 Careerfit: ATS Resume & Job Match Analyzer

## 📌 Overview

The Resume Parser & Job Match Scoring App is an AI-powered tool that extracts text from resumes, compares them with job descriptions, and calculates a match score based on relevant skills. Built with FastAPI (backend) and Streamlit (frontend), the app helps job seekers and recruiters quickly assess resume-job fit.

## 🚀 Features

- Upload resumes in PDF or DOCX format
- Extracts key skills and experience from resumes
- Parses job descriptions to identify required skills
- Computes a match score between the resume and job description
- Highlights missing and matching skills
- User-friendly Streamlit UI

## 🛠 Tech Stack

- **Backend:** FastAPI
- **Frontend:** Streamlit
- **NLP Model:** spaCy
- **Parsing:** pdfplumber, python-docx
- **Version Control:** Git & GitHub

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/palak126/Resume-Parser-Project.git
cd Resume-Parser-Project
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Download spaCy Model
```sh
python -m spacy download en_core_web_sm
```

## ▶️ Running the Application

### Start the FastAPI Backend
```sh
uvicorn app.main:app --reload
```
Backend will be running at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Start the Streamlit Frontend
```sh
streamlit run frontend/app.py
```
Frontend will be running at: [http://localhost:8501](http://localhost:8501)

## 📡 API Endpoints

| Method | Endpoint        | Description                              |
|--------|----------------|------------------------------------------|
| POST   | /upload-resume/ | Upload and parse a resume               |
| POST   | /match-score/   | Compute match score between resume and job description |
| GET    | /health/        | Check API health                        |

## 🎨 UI Preview

![image](https://github.com/user-attachments/assets/48807b18-41ec-4322-827a-1218da1b816c)

## 🛠 Future Enhancements

- Improve skill extraction using Transformer-based models
- Add support for more file formats
- Provide detailed match explanations
- Implement a database for saving resumes and scores
