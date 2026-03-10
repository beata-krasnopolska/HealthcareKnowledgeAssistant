from pathlib import Path

from app.rag.ingest import KnowledgeBaseIngestor
from app.rag.retriever import RetrieverService
from app.rag.vectorstore import VectorStoreService

def test_vector_store_creation_and_query(tmp_path: Path):
    ingestor = KnowledgeBaseIngestor()
    chunks, _ = ingestor.ingest()
    
    vector_store_service = VectorStoreService(persist_directory=str(tmp_path))
    vector_store_service.reset_vector_store()
    vector_store_service.create_vector_store(chunks)
    
    retriever_service = RetrieverService(vector_store_service=vector_store_service)
    results = retriever_service.retrieve("How can I cancel or reschedule an appointment?", k=2)
    
    assert len(results) > 0, "Expected at least one retrieved document"
    assert any("appointment" in doc.page_content.lower() for doc in results)