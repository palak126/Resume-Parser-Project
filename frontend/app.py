import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(to right, #1e3c72, #2a5298);
        color: white;
    }
    
    /* Title */
    .stMarkdown h1 {
        color: white;
        font-size: 32px;
        font-weight: bold;
        text-align: center;
    }
    
    /* Subtext */
    .stMarkdown p {
        color: #dcdcdc;
        font-size: 18px;
        text-align: center;
    }

    /* Upload Box */
    .stFileUploader {
        border: 2px solid #ffffff !important;
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    
    /* Job Description Box */
    .stTextArea textarea {
        border: 2px solid #ffffff !important;
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.1);
        color: #333333 !important; /* Darker text for readability */
    }
    
    /* Section Headings */
    h3 {
        color: white !important; /* Ensures "Upload Resume" and "📝 Job Description" are white */
        font-weight: bold;
    }

    /* Label Fix */
    label {
        color: white !important; /* Forces white color on form labels */
        font-weight: bold;
        font-size: 16px;
    }

    /* Button */
    div.stButton > button {
        background-color: #ff9800;
        color: white;
        border-radius: 10px;
        padding: 12px 20px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #e68900;
    }

    /* Success Message */
    .stAlert[data-baseweb="alert-success"] {
        background-color: #e6f7e6;
        color: #006400;
    }

    /* Warning Message */
    .stAlert[data-baseweb="alert-warning"] {
        background-color: #fff8e1;
        color: #ff9800;
    }

    /* Error Message */
    .stAlert[data-baseweb="alert-error"] {
        background-color: #fbe9e7;
        color: #d32f2f;
    }
    </style>
""", unsafe_allow_html=True)


# Set the title of the app
st.title("📄 Careerfit: ATS Resume & Job Match Analyzer")

# Add a description for context
st.markdown(
    """
    **Upload your resume (PDF or DOCX) and enter a job description.**  
    Our AI-powered tool will analyze and provide a match score based on relevant skills.
    """,
    unsafe_allow_html=True
)

# Layout improvements: Place the file uploader and text area side by side
col1, col2 = st.columns(2)

with col1:
    # Upload Resume
    uploaded_file = st.file_uploader("📂 Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

with col2:
    # Enter Job Description
    job_desc = st.text_area("📝 Job Description", placeholder="Paste job description here...", height=250)

# Add a calculate button
st.markdown("<br>", unsafe_allow_html=True)  # Adds some spacing
if st.button("🚀 Calculate Match Score"):
    if uploaded_file and job_desc:
        # Prepare the resume file to send to FastAPI
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        resume_response = requests.post(f"{FASTAPI_URL}/upload_resume/", files=files)

        if resume_response.status_code == 200:
            resume_text = resume_response.json().get("resume_text", "")
            
            # Get match score and suggestions
            score_response = requests.post(
                f"{FASTAPI_URL}/get_score/", 
                params={"resume": resume_text, "job_desc": job_desc}
            )

            if score_response.status_code == 200:
                result = score_response.json()
                st.success(f"✅ Match Score: {result['match_score']}%")

                # Display missing skills if any
                if result["missing_skills"]:
                    st.warning("⚠️ Missing Skills:")
                    st.write(", ".join(result["missing_skills"]))
            else:
                st.error("❌ Error computing match score.")
        else:
            st.error("❌ Error parsing resume.")
    else:
        st.warning("⚠️ Please upload a resume and enter a job description.")
