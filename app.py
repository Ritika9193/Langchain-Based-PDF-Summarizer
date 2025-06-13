import streamlit as st
import requests
import PyPDF2
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text

def summarize_text(text):
    """Generate a summary using Google Gemini API via HTTP request and format the response."""
    if not API_KEY:
        return "Error: API key is missing. Please set it in the .env file."
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": text}]}]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        json_response = response.json()
        raw_summary = json_response.get("candidates", [{}])[0].get("content", "No summary available.")
        
        # Extract text and remove unnecessary formatting
        if isinstance(raw_summary, dict) and "parts" in raw_summary:
            summary_text = "\n".join([part.get("text", "") for part in raw_summary["parts"]])
        else:
            summary_text = raw_summary
        
        return summary_text
    else:
        return "Error: Unable to generate summary."

def main():
    st.title("LangChain-Based PDF Summarizer with Google Gemini")
    st.write("Upload a PDF to generate an AI-driven summary.")
    
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    
    if uploaded_file is not None:
        with st.spinner("Extracting text..."):
            text = extract_text_from_pdf(uploaded_file)
            
        if text:
            with st.spinner("Generating summary..."):
                summary = summarize_text(text)
                
            st.subheader("Summary:")
            st.write(summary)
        else:
            st.error("Could not extract text from the uploaded PDF.")

if __name__ == "__main__":
    main()
