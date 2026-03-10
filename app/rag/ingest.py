from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.schemas import ChunkingResult

class KnowledgeBaseIngestor:
    def __init__(
        self,
        knowledge_base_dir: str = "./data/knowledge_base",
        chunk_size: int = 500,
        chunk_overlap: int =100,
    ) -> None:
        self.knowledge_base_dir = Path(knowledge_base_dir)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
    def load_documents(self) -> list[Document]:
        if not self.knowledge_base_dir.exists():
            return []
        
        documents: list[Document] = []
        
        for file_path in sorted(self.knowledge_base_dir.glob("*.md")):
            content = file_path.read_text(encoding="utf-8")
            
            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "source": str(file_path),
                        "filename": file_path.name
                    }
                )
            )
            
        return documents
    
    def split_documents(self, documents: list[Document]) -> list[Document]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,            
        )
        
        splited_docs = text_splitter.split_documents(documents)
        
        for index, doc in enumerate(splited_docs):
            doc.metadata["chunk_id"]= index
            
        return splited_docs
    
    def ingest(self) -> tuple[list[Document], ChunkingResult]:
        documents = self.load_documents()
        splitted_docs = self.split_documents(documents)
        
        result = ChunkingResult(
            source_document_count=len(documents),
            chunk_count=len(splitted_docs)
        )
        
        return splitted_docs, result