from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.app.services.pdf_service import (
    extract_text_from_pdf,
    get_pdf_metadata,
)

from backend.app.services.document_service import create_document_chunks
from backend.app.services.vector_store import save_chunks



router = APIRouter(prefix="/api/documents", tags=["Documents"])

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided."
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    document_id = str(uuid4())
    safe_filename = Path(file.filename).name
    saved_filename = f"{document_id}_{safe_filename}"

    destination = UPLOAD_DIR / saved_filename

    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty."
        )

    destination.write_bytes(content)

    return {
        "document_id": document_id,
        "filename": safe_filename,
        "saved_as": saved_filename,
        "size_bytes": len(content),
        "status": "uploaded"
    }


@router.get("/{document_id}/chunks")
async def get_document_chunks(document_id: str):
    matches = list(UPLOAD_DIR.glob(f"{document_id}_*.pdf"))

    if not matches:
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    pdf_path = matches[0]

    pages = extract_text_from_pdf(pdf_path)

    chunks = create_document_chunks(
        document_id=document_id,
        pages=pages,
    )
    save_chunks(chunks)
    return {
        "document_id": document_id,
        "chunk_count": len(chunks),
        "chunks": chunks,
    }