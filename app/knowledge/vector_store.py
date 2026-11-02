import chromadb
from app.knowledge.embedding_generator import generate_embeddings
from app.core.config import settings

vector_store = chromadb.PersistentClient(
    path=settings.CHROMA_PERSIST_DIRECTORY
)

knowledge_collection = vector_store.get_or_create_collection(
    name="campaign_knowledge",
    metadata={"hnsw:space": "cosine"},
)

def store_embeddings(
    document_id: str,
    chunks: list[str],
    embeddings,
) -> None:
    knowledge_collection.delete(
        where={"document_id": document_id}
    )

    if not chunks:
        return

    knowledge_collection.upsert(
        ids=[
            f"{document_id}_chunk_{i}"
            for i in range(len(chunks))
        ],
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=[
            {"document_id": document_id}
            for _ in chunks
        ],
    )
    
def search_knowledge(query_embedding: list[float], top_k: int = 3) -> list[str]:
    results = knowledge_collection.query(
    query_embeddings=[query_embedding],
    n_results=top_k,
    include=["documents", "distances"],)

    if not results["documents"] or not results["distances"]:
        return []

    return results["documents"][0] if results["documents"] else []


def retrieve_knowledge(question: str, top_k: int = 3) -> list[str]:
    query_embedding = generate_embeddings([question])[0]
    return search_knowledge(query_embedding.tolist(), top_k)