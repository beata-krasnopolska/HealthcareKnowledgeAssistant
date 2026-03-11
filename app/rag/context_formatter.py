from langchain_core.documents import Document

def format_documents_for_prompt(documents: list[Document]) -> str:
    if not documents:
        return "No relevant information found in the knowledge base."
    
    formatted_chunks: list[str] = []
    
    for index, doc in enumerate(documents, start=1):
        filename = doc.metadata.get("filename", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")
        
        formatted_chunks.append(
            f"[Source {index} | filename: {filename} | chunk_id: {chunk_id}\n{doc.page_content}"
        )
        
    return "\n\n".join(formatted_chunks)
        