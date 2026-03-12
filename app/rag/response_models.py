from dataclasses import dataclass

@dataclass
class Citation:
    source_number: int
    filename: str
    chunk_id: int | str
    
    
@dataclass
class RagAnswer:
    answer: str
    citations: list[Citation]