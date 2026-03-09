from app.rag.ingest import KnowledgeBaseIngestor

def test_load_documents_returns_markdown_files():
    ingestor = KnowledgeBaseIngestor()
    
    documents = ingestor.load_documents()
    
    assert len(documents) > 0, "Expected at least one source document"
    assert all(doc.metadata.get("filename", "").endswith(".md") for doc in documents), "All documents should be markdown files"
    
def test_split_documents_creates_chunks():
    ingestor = KnowledgeBaseIngestor(chunk_size=300, chunk_overlap=50)

    documents = ingestor.load_documents()
    chunks = ingestor.split_documents(documents)

    assert len(chunks) > 0
    assert all("chunk_id" in chunk.metadata for chunk in chunks)
    
def test_ingest_returns_chunking_result():
    ingestor = KnowledgeBaseIngestor(chunk_size=300, chunk_overlap=50)

    chunks, result = ingestor.ingest()

    assert len(chunks) == result.chunk_count
    assert result.source_document_count > 0
    assert result.chunk_count > 0