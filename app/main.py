import logging

from app.rag.retriever import RetrieverService
from app.rag.vectorstore import VectorStoreService
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
        
    vector_store_service = VectorStoreService()
    vector_store_service.reset_vector_store()
    vector_store_service.create_vector_store(chunks)
    logger.info("Vector store created succesfully")
    
    retriever_service = RetrieverService(vector_store_service)
    
    retrieval_query = "How can I reschedule an appointment?"
    logger.info("Testing retriever with query: %s", retrieval_query)
    retrieved_docs = retriever_service.retrieve(retrieval_query)
    
    logger.info("Retriever returned %s documents", len(retrieved_docs))
    
    for index, doc in enumerate(retrieved_docs, start=1):
        logger.info("Retrieved doc %s | filename: %s | chunk_id: %s | preview: %s",
                    index,
                    doc.metadata.get("filename"),
                    doc.metadata.get("chunk_id"),
                    doc.page_content[:200].replace("\n", " ")
                    )
    
    chat_service = ChatService()
    
    user_question = "Explain in simple words what a healthcare knowledge assistant is."
    logger.info("Sending demo question to chat service: %s", user_question)
    
    response = chat_service.ask(user_question)
    logger.info("Received response: %s", response)

    print(f"{settings.app_name} initialized successfully.")


if __name__ == "__main__":
    main()