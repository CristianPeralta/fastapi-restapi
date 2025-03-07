
from fastapi import FastAPI

app = FastAPI()

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