from datetime import datetime
import enum
from sqlalchemy import Column, Integer, String, Text, Enum, Numeric, ForeignKey, DateTime, JSON
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class PostType(str, enum.Enum):
    lost = "lost"
    found = "found"

class AnimalType(str, enum.Enum):
    cat = "cat"
    dog = "dog"

class StatusType(str, enum.Enum):
    ACTIVE = "ACTIVE"
    RESOLVED = "RESOLVED"

class DistrictType(str, enum.Enum):
    miami = "miami"
    asafra = "asafra"
    aboqir = "aboqir"
    sidi_beshr = "sidi beshr"
    sidi_gaber = "sidi gaber"
    elebrahimiya = "elebrahimiya"
    shatby = "shatby"
    alazarita = "alazarita"
    sporting = "sporting"
    moharam_bek = "moharam bek"
    agamy = "agamy"
    fliming = "fliming"
    elraml_station = "elraml station"
    bahary = "bahary"
    elmanshia = "elmanshia"


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="author", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    
    post_type = Column(Enum(PostType), nullable=False)
    animal_type = Column(Enum(AnimalType), nullable=True)
    breed = Column(String(50), nullable=True)
    color = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    district = Column(Enum(DistrictType), nullable=True)
    
    latitude = Column(Numeric(10, 8), nullable=True)
    longitude = Column(Numeric(11, 8), nullable=True)
    status = Column(Enum(StatusType), default=StatusType.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)

    author = relationship("User", back_populates="posts")
    images = relationship("PetImage", back_populates="post", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class PetImage(Base):
    __tablename__ = 'pet_images'

    image_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('posts.post_id', ondelete='CASCADE'), nullable=False)
    image_url = Column(String(255), nullable=False)
    image_vector = Column(JSON, nullable=True)

    post = relationship("Post", back_populates="images")


class Comment(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('posts.post_id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")