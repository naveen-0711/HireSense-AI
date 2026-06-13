from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "mixedbread-ai/mxbai-embed-large-v1"
)

def generate_embedding(text):

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()