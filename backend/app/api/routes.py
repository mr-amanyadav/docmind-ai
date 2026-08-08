from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {
        "project": "DocMind AI",
        "message": "Backend is running successfully 🚀",
        "version": "0.1.0"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }