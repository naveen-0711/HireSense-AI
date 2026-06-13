from backend.services.embedding_service import generate_embedding

v = generate_embedding("Machine Learning Engineer")

print(len(v))
print(min(v))
print(max(v))