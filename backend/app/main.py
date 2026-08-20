from fastapi import FastAPI

from backend.app.api.routes import router
from backend.app.api.documents import router as documents_router
from backend.app.core.config import settings
from backend.app.api.embeddings import router as embeddings_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.include_router(router)
app.include_router(documents_router)
app.include_router(embeddings_router)