import logging
from langchain_core.messages import HumanMessage, SystemMessage
from app.llm.providers import get_chat_model

logger = logging.getLogger(__name__)

class ChatService:
    def __init__(self) -> None:
        self.model = get_chat_model()
        
    def ask(self, user_question: str) -> str:
        logger.info("Received user question: %s", user_question)
        
        messages = [
            SystemMessage(
                content=(
                    "You are a helpful healthcare knowledge assistant. "
                    "Provide clear, concise, safe, and non-diagnostic answers. "
                    "Answer in professional but friendly tone."
                    "Do not pretend to be a doctor."
                )
            ),
            HumanMessage(content=user_question)
        ]
        
        response = self.model.invoke(messages)
        
        logger.info("Received response from model")
        return response.content