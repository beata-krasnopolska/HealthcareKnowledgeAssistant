import logging

from app.rag.ingest import KnowledgeBaseIngestor
from app.core.logging import configure_logging
from app.core.settings import settings
from app.services.chat_service import ChatService
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
    
    if chunks:
        logger.info("First chunk source: %s", chunks[0].metadata.get("filename"))
        logger.info("First chunk id: %s", chunks[0].metadata.get("chunk_id"))
        logger.info("First chunk preview: %s", chunks[0].page_content[:200])
    
    chat_service = ChatService()
    
    user_question = "Explain in simple words what a healthcare knowledge assistant is."
    logger.info("Sending demo question to chat service: %s", user_question)
    
    response = chat_service.ask(user_question)
    logger.info("Received response: %s", response)

    print(f"{settings.app_name} initialized successfully.")


if __name__ == "__main__":
    main()