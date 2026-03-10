from langchain_core.documents import Document

from app.core.settings import settings
from app.rag.vectorstore import VectorStoreService

class RetrieverService:
    def __init__(self, vector_store_service: VectorStoreService | None = None) -> None:
        self.vector_store_service = vector_store_service or VectorStoreService()
        
    def retrieve(self, query: str, k: int | None = None) -> list[Document]:
        vector_store = self.vector_store_service.load_vector_store()
        retriever = vector_store.as_retriever(search_kwargs={"k": k or settings.top_k})
        
        return retriever.invoke(query)