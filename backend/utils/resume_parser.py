import re

def extract_email(text):

    email = re.findall(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    return email[0] if email else "Not Found"


def extract_phone(text):

    phone = re.findall(
        r'\+?\d[\d\s\-]{8,15}',
        text
    )

    return phone[0] if phone else "Not Found"


def extract_name(text):

    lines = text.split("\n")

    for line in lines[:5]:

        if len(line.split()) >= 2:
            return line.strip()

    return "Not Found"


def extract_skills(text):

    skills_db = [
        "Python",
        "Java",
        "C++",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "AWS",
        "Docker",
        "Kubernetes",
        "FastAPI",
        "Flask",
        "Streamlit",
        "Power BI",
        "Tableau",
        "Pandas",
        "NumPy"
    ]

    found_skills = []

    for skill in skills_db:

        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills