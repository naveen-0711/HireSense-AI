from backend.services.embedding_service import (
    generate_embedding
)

vector = generate_embedding(
    "Python ML AWS"
)

print(len(vector))