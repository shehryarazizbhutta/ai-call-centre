from app.knowledge.knowledge_ingestion import ingest_pdf
from app.knowledge.vector_store import retrieve_knowledge


def test_retrieve_knowledge_from_pdf():
    ingest_pdf("app/knowledge/call-center-scripts.pdf")

    results = retrieve_knowledge(
        "What information should a customer service agent provide?",
        top_k=3,
    )

    assert len(results) > 0
    assert all(isinstance(result, str) for result in results)