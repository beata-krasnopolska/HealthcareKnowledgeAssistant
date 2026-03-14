import logging

from app.tools.registry import ToolRegistry
from app.rag.citations import format_citations
from app.rag.qa import RagQaService
from app.rag.vectorstore import VectorStoreService
from app.rag.ingest import KnowledgeBaseIngestor
from app.core.logging import configure_logging
from app.core.settings import settings
from app.services.knowledge_base_service import KnowledgeBaseService


def main() -> None:
    configure_logging()

    logger = logging.getLogger(__name__)
    logger.info("Starting application: %s", settings.app_name)
    logger.info("Model configured: %s", settings.model_name)
    logger.info("Embedding model configured: %s", settings.embedding_model)
    logger.info("Vector store directory: %s", settings.vector_store_dir)
    
    knowledge_base_service = KnowledgeBaseService()
    documents = knowledge_base_service.list_documents()
    logger.info("Knowledge base documents found: %s", documents)
    
    ingestor = KnowledgeBaseIngestor()
    chunks, result = ingestor.ingest()
    logger.info("Loaded source documents: %s", result.source_document_count)
    logger.info("Created chunks: %s", result.chunk_count)
        
    vector_store_service = VectorStoreService()
    vector_store_service.reset_vector_store()
    vector_store_service.create_vector_store(chunks)
    logger.info("Vector store created succesfully")
    
    rag_qa_service = RagQaService()
    
    user_question = "How can I reschedule an appointment?"
    logger.info("Asking RAG QA service: %s", user_question)
    
    rag_response = rag_qa_service.ask(user_question)
    
    print("\nRAG answer:\n")
    print(rag_response.answer)
    
    print("\nCitations:\n")
    print(format_citations(rag_response.citations))
    
    tool_registry = ToolRegistry()
    
    print("\nGlossary tool demo:\n")
    print(tool_registry.glossary_tool.lookup_term("referral"))
    
    print("\nContact lookup tool demo:\n")
    print(tool_registry.contact_lookup_tool.lookup_department("privacy office"))
    


if __name__ == "__main__":
    main()