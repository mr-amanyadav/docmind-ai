from uuid import uuid4

from backend.app.services.chunking_service import split_text


def create_document_chunks(
    document_id: str,
    pages: list[dict],
) -> list[dict]:
    chunks = []

    for page in pages:
        page_number = page["page_number"]
        text = page["text"]

        page_chunks = split_text(
            text,
            chunk_size=1000,
            chunk_overlap=150,
        )

        for chunk_index, chunk_text in enumerate(page_chunks):
            chunks.append(
                {
                    "chunk_id": str(uuid4()),
                    "document_id": document_id,
                    "page_number": page_number,
                    "chunk_index": chunk_index,
                    "text": chunk_text,
                }
            )

    return chunks