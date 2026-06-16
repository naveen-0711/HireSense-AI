from backend.utils.supabase_client import (
    supabase
)

from backend.auth.user_context import (
    get_current_user
)


def save_ats_result(
    data
):

    data["uploaded_by"] = (
        get_current_user()
    )

    supabase.table(
        "ats_results"
    ).insert(
        data
    ).execute()