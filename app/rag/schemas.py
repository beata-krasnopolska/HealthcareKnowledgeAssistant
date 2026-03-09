from dataclasses import dataclass

@dataclass
class ChunkingResult:
    source_document_count: int
    chunk_count:  int