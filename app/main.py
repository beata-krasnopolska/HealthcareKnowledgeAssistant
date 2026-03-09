import logging

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
    
    chat_service = ChatService()
    
    user_question = "Explain in simple words what a healthcare knowledge assistant is."
    logger.info("Sending demo question to chat service: %s", user_question)
    
    response = chat_service.ask(user_question)
    logger.info("Received response: %s", response)

    print(f"{settings.app_name} initialized successfully.")


if __name__ == "__main__":
    main()