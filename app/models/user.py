from beanie import Document, Indexed
from pydantic import EmailStr, Field, BaseModel
from typing import Annotated, Optional
from datetime import datetime
import uuid


class User(Document):
    """
    User model using Beanie Document
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: Annotated[EmailStr, Indexed(unique=True)]
    password: str
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    
    class Settings:
        name = "users"  # Collection name in MongoDB
        use_revision = True  # Enable revision history
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "password": "password123",
                "is_active": True,
                "is_admin": False
            }
        }


# Schemas for operations
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    is_admin: bool = False


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None


class UserPublic(BaseModel):
    id: str
    name: str
    email: EmailStr
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True