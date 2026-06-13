from sklearn.metrics.pairwise import cosine_similarity

from backend.services.embedding_service import (
    generate_embedding
)


def calculate_semantic_score(
    resume_text,
    jd_text
):

    resume_embedding = generate_embedding(
        resume_text
    )

    jd_embedding = generate_embedding(
        jd_text
    )

    score = cosine_similarity(
        [resume_embedding],
        [jd_embedding]
    )[0][0]

    return round(
        score * 100,
        2
    )


def calculate_skill_score(
    resume_skills,
    jd_skills
):

    if not jd_skills:
        return 0

    matched = set(
        skill.lower()
        for skill in resume_skills
    ) & set(
        skill.lower()
        for skill in jd_skills
    )

    return round(
        len(matched)
        /
        len(jd_skills)
        * 100,
        2
    )


def get_missing_skills(
    resume_skills,
    jd_skills
):

    resume_set = {
        skill.lower()
        for skill in resume_skills
    }

    return [
        skill
        for skill in jd_skills
        if skill.lower()
        not in resume_set
    ]


def calculate_project_score(
    projects
):

    if not projects:
        return 0

    return min(
        len(projects) * 20,
        100
    )


def calculate_education_score(
    education
):

    if not education:
        return 0

    return 100


def calculate_experience_score(
    years
):

    if years >= 5:
        return 100

    return min(
        years * 20,
        100
    )


def calculate_certification_score(
    certifications
):

    if not certifications:
        return 0

    return min(
        len(certifications) * 25,
        100
    )