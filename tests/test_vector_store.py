from app.knowledge.vector_store import knowledge_collection


def test_knowledge_collection_is_available():
    assert knowledge_collection.name == "campaign_knowledge"