from typing import List, Optional, Dict, Any
from app.repositories.user_repository import UserRepository
from app.models.user import User, UserCreate, UserUpdate, UserPublic
from passlib.context import CryptContext


# Password hash configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    """
    Service for user-related business logic
    """
    
    @staticmethod
    def get_password_hash(password: str) -> str:
        """Generate a password hash"""
        return pwd_context.hash(password)
    
    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify if the password matches the hash"""
        return pwd_context.verify(plain_password, hashed_password)
    
    @staticmethod
    async def create_user(user_data: UserCreate) -> UserPublic:
        """Create a new user with a hashed password"""
        user_dict = user_data.model_dump()
        
        # Check if the email already exists
        existing_user = await UserRepository.get_by_email(user_dict["email"])
        if existing_user:
            raise ValueError("The email is already registered")
        
        # Password hash
        user_dict["password"] = UserService.get_password_hash(user_dict["password"])
        
        # Create the user
        user = await UserRepository.create(user_dict)
        
        # Convert to public schema (without password)
        return UserPublic.model_validate(user)
    
    @staticmethod
    async def get_user_by_id(user_id: str) -> Optional[UserPublic]:
        """Get a user by ID"""
        user = await UserRepository.get_by_id(user_id)
        if not user:
            return None
        return UserPublic.model_validate(user)
    
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        """Get a user by email (with password for authentication)"""
        return await UserRepository.get_by_email(email)
    
    @staticmethod
    async def get_users(skip: int = 0, limit: int = 100) -> List[UserPublic]:
        """Get a list of users"""
        users = await UserRepository.get_all(skip, limit)
        return [UserPublic.model_validate(user) for user in users]
    
    @staticmethod
    async def update_user(user_id: str, user_data: UserUpdate) -> Optional[UserPublic]:
        """Update a user"""
        # Filter out None fields
        update_data = {k: v for k, v in user_data.model_dump().items() if v is not None}
        
        if not update_data:
            # No data to update
            user = await UserRepository.get_by_id(user_id)
            if not user:
                return None
            return UserPublic.model_validate(user)
            
        # Update the user
        user = await UserRepository.update(user_id, update_data)
        if not user:
            return None
            
        return UserPublic.model_validate(user)
    
    @staticmethod
    async def delete_user(user_id: str) -> bool:
        """Delete a user"""
        return await UserRepository.delete(user_id)
    
    @staticmethod
    async def get_user_count() -> int:
        """Get the total number of users"""
        return await UserRepository.count()