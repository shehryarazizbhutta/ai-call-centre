from app.knowledge.embedding_generator import generate_embeddings


def test_chunks_can_be_embedded():
    chunks = [
        "Customers can cancel an order before it ships.",
        "Orders are shipped within three business days.",
    ]

    embeddings = generate_embeddings(chunks)

    assert embeddings.shape == (2, 384)