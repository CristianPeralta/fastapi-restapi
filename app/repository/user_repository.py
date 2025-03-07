from typing import List, Optional, Dict, Any
from datetime import datetime
from app.models.user import User


class UserRepository:
    """
    Repository for user-related database operations  
    Includes all basic CRUD operations plus specific queries
    """
    
    @staticmethod
    async def create(user_data: Dict[str, Any]) -> User:
        """Create a new user"""
        user = User(**user_data)
        await user.insert()
        return user
    
    @staticmethod
    async def get_by_id(user_id: str) -> Optional[User]:
        """Get a user by ID"""
        return await User.get(user_id)
    
    @staticmethod
    async def get_by_email(email: str) -> Optional[User]:
        """Get a user by email"""
        return await User.find_one(User.email == email)
    
    @staticmethod
    async def get_all(skip: int = 0, limit: int = 100) -> List[User]:
        """Get a paginated list of users"""
        users = await User.find_all().skip(skip).limit(limit).to_list()
        return users
    
    @staticmethod
    async def get_active_users(skip: int = 0, limit: int = 100) -> List[User]:
        """Get active users"""
        users = await User.find(User.is_active == True).skip(skip).limit(limit).to_list()
        return users
    
    @staticmethod
    async def update(user_id: str, update_data: Dict[str, Any]) -> Optional[User]:
        """Update a user"""
        user = await UserRepository.get_by_id(user_id)
        if not user:
            return None
            
        # Add update date
        update_data["updated_at"] = datetime.utcnow()
        
        # Update the fields
        for key, value in update_data.items():
            setattr(user, key, value)
            
        await user.save()
        return user
    
    @staticmethod
    async def delete(user_id: str) -> bool:
        """Delete a user by ID"""
        user = await UserRepository.get_by_id(user_id)
        if not user:
            return False
            
        await user.delete()
        return True
        
    @staticmethod
    async def count() -> int:
        """Count the total number of users"""
        return await User.count()