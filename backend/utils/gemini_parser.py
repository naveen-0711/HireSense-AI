import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def parse_resume_with_gemini(resume_text):

    prompt = f"""
    You are an expert ATS resume parser.

    Extract information from the resume.

    Return ONLY valid JSON.

    Format:

    {{
      "name":"",
      "email":"",
      "phone":"",
      "skills":[],
      "education":[],
      "projects":[],
      "experience":[],
      "certifications":[],
      "years_of_experience":0
    }}

    Resume:

    {resume_text}
    """

    try:

        response = model.generate_content(
            prompt
        )

    except Exception as e:

        print(
            f"Gemini Error: {e}"
        )

        return {
            "name": "Parsing Failed",
            "email": "",
            "phone": "",
            "skills": [],
            "education": [],
            "projects": [],
            "experience": [],
            "certifications": [],
            "years_of_experience": 0
        }

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(
        cleaned
    )