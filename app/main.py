from fastapi import FastAPI
from app.config.settings import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version="0.1.0"
)

@app.get("/", tags=["root"])
async def root():
    """
    Root route that displays basic API information
    """
    return {
        "message": "Welcome to FastAPI Beanie CRUD API",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health", tags=["health"])
async def health_check():
    """
    Endpoint to check the API status
    """
    return {"status": "ok"}