from backend.utils.supabase_client import (
    supabase
)

from backend.auth.user_context import (
    get_current_user
)


def save_candidate(
    candidate,
    resume_text
):

    data = {

        "name":
            candidate.get("name"),

        "email":
            candidate.get("email"),

        "phone":
            candidate.get("phone"),

        "skills":
            candidate.get("skills"),

        "education":
            candidate.get("education"),

        "projects":
            candidate.get("projects"),

        "experience":
            candidate.get("experience"),

        "certifications":
            candidate.get("certifications"),

        "years_of_experience":
            candidate.get(
                "years_of_experience"
            ),

        "resume_text":
            resume_text,

        "uploaded_by":
            get_current_user()
    }

    result = (
        supabase
        .table(
            "candidates"
        )
        .insert(
            data
        )
        .execute()
    )

    return result