from sentence_transformers import SentenceTransformer

from app.core.config import settings

model = SentenceTransformer(settings.EMBEDDING_MODEL)


def generate_embeddings(chunks: list[str]):
    return model.encode(chunks)