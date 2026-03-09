from app.services.knowledge_base_service import KnowledgeBaseService

def test_knowledge_base_documents_exists():
    service = KnowledgeBaseService()
    documents = service.list_documents()
    
    assert len(documents) > 0, "Expected at least one document in the knowledge base"
    assert "patient_visit_preparation.md" in documents