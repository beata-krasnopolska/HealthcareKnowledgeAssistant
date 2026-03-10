from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.core.settings import settings
from app.rag.embeddings import get_embedding_model

class VectorStoreService:
    def __init__(self, persist_directory: str | None =None) -> None:
        self.persist_directory = persist_directory or settings.vector_store_dir
        self.embedding_model = get_embedding_model()
        
    def ensure_directory(self) -> None:
        Path(self.persist_directory).mkdir(parents=True, exist_ok=True)
        
    def create_vector_store(self, documents: list[Document]) -> Chroma:
        self.ensure_directory()
        
        return Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )
        
    def load_vector_store(self) -> Chroma:
        self.ensure_directory()
        
        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model
        )
        
    def reset_vector_store(self) -> None:
        path = Path(self.persist_directory)
        
        if not path.exists():
            return
        
        for item in path.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                import shutil
                
                shutil.rmtree(item)
                