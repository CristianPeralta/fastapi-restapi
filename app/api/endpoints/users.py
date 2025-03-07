from typing import List, Optional
from fastapi import APIRouter, HTTPException, status, Query, Path, Body
from app.models.user import UserCreate, UserUpdate, UserPublic
from app.services.user_service import UserService

# Create router
router = APIRouter()


@router.post("/", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate = Body(...)):
    """
    Create a new user
    """
    try:
        user = await UserService.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.get("/", response_model=List[UserPublic])
async def read_users(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=100, description="Number of records to return")
):
    """
    Get a paginated list of users
    """
    users = await UserService.get_users(skip, limit)
    return users


@router.get("/count", response_model=int)
async def count_users():
    """
    Return the total number of users
    """
    count = await UserService.get_user_count()
    return count


@router.get("/{user_id}", response_model=UserPublic)
async def read_user(
    user_id: str = Path(..., description="ID of the user to retrieve")
):
    """
    Get a user by ID
    """
    user = await UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user


@router.put("/{user_id}", response_model=UserPublic)
async def update_user(
    user_id: str = Path(..., description="ID of the user to update"),
    user_data: UserUpdate = Body(...)
):
    """
    Update a user
    """
    user = await UserService.update_user(user_id, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: str = Path(..., description="ID of the user to delete")
):
    """
    Delete a user
    """
    deleted = await UserService.delete_user(user_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return None