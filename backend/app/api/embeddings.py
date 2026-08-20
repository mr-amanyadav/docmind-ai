from fastapi import APIRouter

from backend.app.services.embedding_service import create_embedding


router = APIRouter(
    prefix="/api/embeddings",
    tags=["Embeddings"],
)


@router.post("/test")
async def test_embedding(text: str):
    embedding = create_embedding(text)

    return {
        "text": text,
        "dimensions": len(embedding),
        "embedding": embedding,
    }