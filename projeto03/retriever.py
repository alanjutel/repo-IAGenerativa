import numpy as np
from sentence_transformers import SentenceTransformer

# Modelo leve e eficiente
model = SentenceTransformer("all-MiniLM-L6-v2")

knowledge_chunks = []
knowledge_embeddings = []


def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks


def load_conhecimento():
    global knowledge_chunks, knowledge_embeddings

    with open("projeto03/conhecimento/conhecimento.txt", "r", encoding="utf-8") as f:
        content = f.read()

    knowledge_chunks = chunk_text(content)

    print("Gerando embeddings locais...")
    knowledge_embeddings = model.encode(knowledge_chunks, convert_to_numpy=True)

    print("Embeddings gerados com sucesso.")

    return knowledge_chunks


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def similarity_search(query, top_k=3):
    query_embedding = model.encode([query], convert_to_numpy=True)[0]

    similarities = []
    for i, emb in enumerate(knowledge_embeddings):
        score = cosine_similarity(query_embedding, emb)
        similarities.append((score, knowledge_chunks[i]))

    similarities.sort(reverse=True, key=lambda x: x[0])

    top_chunks = [chunk for _, chunk in similarities[:top_k]]

    return "\n\n".join(top_chunks)