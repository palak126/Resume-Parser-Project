from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
from fastapi import UploadFile

def extract_text(file: UploadFile):
    """Extracts text from a PDF or DOCX resume"""
    file_extension = file.filename.split(".")[-1].lower()
    
    if file_extension == "pdf":
        text = extract_pdf_text(file.file)
    elif file_extension == "docx":
        doc = Document(file.file)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        text = file.file.read().decode("utf-8")  # TXT files

    return text.strip()
