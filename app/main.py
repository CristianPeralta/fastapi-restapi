from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.settings import get_settings
from app.core.database import init_db
from app.api.endpoints import users

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database connection
    await init_db()
    yield
    # Cleanup code if needed

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version="0.1.0",
    lifespan=lifespan
)

# Include routers
app.include_router(
    users.router,
    prefix=f"{settings.API_V1_STR}/users",
    tags=["users"]
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