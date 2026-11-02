from pathlib import Path
from app.knowledge.vector_store import store_embeddings
from app.knowledge.pdf_text_extractor import extract_text_from_pdf
from app.knowledge.text_chunker import chunk_text
from app.knowledge.embedding_generator import generate_embeddings

def ingest_pdf(pdf_path: str | Path):
    pdf_path = Path(pdf_path)

    text = extract_text_from_pdf(pdf_path)
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    document_id = pdf_path.stem
    store_embeddings(document_id, chunks, embeddings)

    return chunks, embeddings