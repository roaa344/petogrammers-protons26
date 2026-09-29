from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from models import PostType, AnimalType, StatusType, DistrictType

class UserCreate(BaseModel):
    username: str
    email: str
    phone_number: Optional[str] = None
    password: str

class UserResponse(BaseModel):
    user_id: int
    username: str
    email: str
    phone_number: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class PetImageResponse(BaseModel):
    image_id: int
    image_url: str

    class Config:
        from_attributes = True

class CommentCreate(BaseModel):
    content: str

class CommentResponse(BaseModel):
    comment_id: int
    post_id: int
    user_id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True

class PostCreate(BaseModel):
    post_type: PostType
    animal_type: Optional[AnimalType] = None
    breed: Optional[str] = None
    color: Optional[str] = None
    description: Optional[str] = None
    district: Optional[DistrictType] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class PostResponse(BaseModel):
    post_id: int
    user_id: int
    post_type: PostType
    animal_type: Optional[AnimalType]
    breed: Optional[str]
    color: Optional[str]
    description: Optional[str]
    district: Optional[DistrictType]
    latitude: Optional[float]
    longitude: Optional[float]
    status: StatusType
    created_at: datetime
    images: List[PetImageResponse] = []
    comments: List[CommentResponse] = []

    class Config:
        from_attributes = True