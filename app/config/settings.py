from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    """
    Application settings,
    loaded from environment variables or default values
    """
    # MongoDB Configuration
    MONGODB_URL: str = "mongodb://localhost:27017"
    MONGODB_DB_NAME: str = "fastapi_beanie_db"
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    APP_NAME: str = "FastAPI Beanie CRUD"
    APP_DESCRIPTION: str = "RESTful API with FastAPI and Beanie ODM for MongoDB"
    
    # JWT Configuration (for possible future authentication)
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """
    Returns the application settings using cache
    to improve performance
    """
    return Settings()