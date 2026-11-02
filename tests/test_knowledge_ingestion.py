from pathlib import Path
from app.knowledge.vector_store import knowledge_collection
from app.knowledge.knowledge_ingestion import ingest_pdf
from app.knowledge.vector_store import retrieve_knowledge


def test_ingest_pdf():
    pdf_path = (
        Path(__file__).parents[1]
        / "app"
        / "knowledge"
        / "call-center-scripts.pdf"
    )

    chunks, embeddings = ingest_pdf(pdf_path)

    assert len(chunks) > 0
    assert embeddings.shape == (len(chunks), 384)
    assert knowledge_collection.count() >= len(chunks)



def test_reingestion_replaces_previous_chunks():
    document_id = "sample_update_test"

    from app.knowledge.vector_store import store_embeddings
    import numpy as np

    store_embeddings(
        document_id,
        ["Old chunk"],
        np.array([[0.1] * 384]),
    )

    store_embeddings(
        document_id,
        ["New chunk"],
        np.array([[0.2] * 384]),
    )

    results = knowledge_collection.get(
        where={"document_id": document_id},
        include=["documents"],
    )

    assert results["documents"] == ["New chunk"]

def test_retrieve_knowledge_returns_relevant_chunks():
    results = retrieve_knowledge("What does the campaign script explain?")
    assert len(results) > 0
    assert all(isinstance(chunk, str) for chunk in results)