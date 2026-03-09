from pathlib import Path

class KnowledgeBaseService:
    def __init__(self, knowledge_base_dir: str = "./data/knowledge_base") -> None:
        self.knowledge_base_dir = Path(knowledge_base_dir)
        
    def list_documents(self) -> list[str]:
        if not self.knowledge_base_dir.exists():
            return []
        
        return sorted(
            [file.name for file in self.knowledge_base_dir.iterdir() if file.is_file()]
        )