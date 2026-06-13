import chromadb

client = chromadb.PersistentClient(
    path="chromadb_store"
)

collection = client.get_or_create_collection(
    name="candidates",
    metadata={
        "hnsw:space": "cosine"
    }
)

def store_candidate_embedding(
    candidate_id,
    candidate_name,
    resume_text,
    embedding
):

    if not candidate_id:
        raise ValueError(
            "Candidate ID cannot be empty"
        )

    collection.add(
        ids=[str(candidate_id)],
        documents=[resume_text],
        embeddings=[embedding],
        metadatas=[
            {
                "name": candidate_name
            }
        ]
    )


def search_candidates(
    query_embedding,
    top_k=5
):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results