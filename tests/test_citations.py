from langchain_core.documents import Document

from app.rag.citations import build_citations, format_citations

def test_build_citations_returns_expected_metadata():
    documents = [
        Document(
            page_content="Example content",
            metadata={
                "filename": "example_doc.md",
                "chunk_id": 7
            }
        ),
        Document(
            page_content="Another example",
            metadata={
                "filename": "another_doc.md",
                "chunk_id": 3
            }
        )
    ]
    
    citations = build_citations(documents)
    
    assert len(citations) == 2
    assert citations[0].source_number == 1
    assert citations[0].filename == "example_doc.md"
    assert citations[0].chunk_id == 7
    
def test_format_citations_returns_readible_output():
    documents = [
        Document(
            page_content="Example content",
            metadata={
                "filename": "example_doc.md",
                "chunk_id": 7
            }
        )
    ]
    
    citations = build_citations(documents)
    formatted = format_citations(citations)
    
    assert "[1] example_doc.md (chunk_id: 7)" in formatted