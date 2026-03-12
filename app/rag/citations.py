from langchain_core.documents import Document

from app.rag.response_models import Citation


def build_citations(documents: list[Document]) -> list[Citation]:
    citations: list[Citation] = []
    
    for index, doc in enumerate(documents, start =1):
        citations.append(
            Citation(
                source_number=index,
                filename=doc.metadata.get("filename", "unknown"),
                chunk_id=doc.metadata.get("chunk_id", "unknown")
            )
        )
    return citations

def format_citations(citations: list[Citation]) -> str:
    if not citations:
        return "No citations available."
    
    return "\n".join(
        [
            f"[{citation.source_number}] {citation.filename} (chunk_id: {citation.chunk_id})"
            for citation in citations
        ]
    )