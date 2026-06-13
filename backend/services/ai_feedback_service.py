import json
import google.generativeai as genai

def generate_ai_feedback(
    resume_text,
    job_description
):

    prompt = f"""
    You are an expert ATS recruiter.

    Analyze the resume against the job description.

    Return JSON only.

    Format:

    {{
      "strengths": [],
      "weaknesses": [],
      "recommendations": [],
      "hiring_decision": ""
    }}

    Resume:

    {resume_text}

    Job Description:

    {job_description}
    """

    response = (
        genai.GenerativeModel(
            "gemini-2.5-flash"
        ).generate_content(
            prompt
        )
    )

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(
        cleaned
    )