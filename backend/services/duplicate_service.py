from backend.services.chroma_service import (
    search_candidates
)

def check_duplicate(
    embedding
):

    results = search_candidates(
        embedding,
        top_k=1
    )

    if not results["distances"][0]:
        return False, None

    distance = results["distances"][0][0]

    similarity = (
        1 / (1 + distance)
    ) * 100

    if similarity > 95:

        return True, similarity

    return False, similarity