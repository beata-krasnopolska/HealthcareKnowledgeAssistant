from langchain_openai import ChatOpenAI
from app.core.settings import settings

def get_chat_model() -> ChatOpenAI:
    return ChatOpenAI(
        model=settings.model_name,
        api_key=settings.openai_api_key,
        temperature=0,
    )