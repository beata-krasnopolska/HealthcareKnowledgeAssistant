from pathlib import Path

from app.rag.qa import RagQaService
from app.rag.retriever import RetrieverService
from app.rag.vectorstore import VectorStoreService
from app.rag.ingest import KnowledgeBaseIngestor

def test_rag_qa_returns_answer_and_sources(tmp_path: Path):
    ingestor = KnowledgeBaseIngestor()
    chunks, chunking_result = ingestor.ingest()
    
    vector_store_service = VectorStoreService(persist_directory=str(tmp_path))
    vector_store_service.reset_vector_store()
    vector_store_service.create_vector_store(chunks)
    
    retriever_service = RetrieverService(vector_store_service=vector_store_service)
    rag_qa_service = RagQaService(retriever_service=retriever_service)
    
    response = rag_qa_service.ask("How can I reschedule an appointment?")
    
    assert isinstance(response.answer, str)
    assert response.answer.strip() != ""
    assert len(response.citations) > 0
    assert any(citation.filename == "appointments_and_referrals.md" for citation in response.citations)