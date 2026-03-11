import logging

from langchain_core.messages import HumanMessage, SystemMessage

from app.llm.providers import get_chat_model
from app.rag.context_formatter import format_documents_for_prompt
from app.rag.retriever import RetrieverService

logger = logging.getLogger(__name__)

class RagQaService:
    def __init__(self, retriever_service: RetrieverService | None = None) -> None:
        self.model = get_chat_model()
        self.retriever_service = retriever_service or RetrieverService()
        
    def ask(self, question: str) -> tuple[str, list]:
        logger.info("Running RAG retrieval for question: %s", question)
        
        retrieved_docs = self.retriever_service.retrieve(question)
        formatted_context = format_documents_for_prompt(retrieved_docs)
        
        logger.info("Retrieved %s documents for RAG context", len(retrieved_docs))
        
        messages = [
            SystemMessage(
                content=(
                    "You are a helpful healthcare knowledge assistant."
                    "Answer using only the provided context."
                    "If the answer is not in the context, say you don't know. "
                    "Do not provide diagnostic answers or pretend to be a doctor."
                    "Be clear, consise, safe and professional but friendly in tone."
                )
            ),
            HumanMessage(
                content=(
                    f"User question: {question}\n\n"
                    f"Context: {formatted_context}\n\n"
                    "Answer the question based on the context above."
                )
            ),
        ]
        
        response = self.model.invoke(messages)
        
        logger.info("Generated RAG answer successfully")
        return response.content, retrieved_docs
        