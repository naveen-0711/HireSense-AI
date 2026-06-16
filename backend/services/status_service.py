from backend.utils.supabase_client import (
    supabase
)

from backend.auth.user_context import (
    get_current_user
)


def save_candidate_status(
    data
):

    data["uploaded_by"] = (
        get_current_user()
    )

    response = (
        supabase
        .table(
            "candidate_status"
        )
        .insert(
            data
        )
        .execute()
    )

    return response