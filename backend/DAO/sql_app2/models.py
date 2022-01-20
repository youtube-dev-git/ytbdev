from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Syllabus(Base):
    __tablename__ = "syllabus"

    id=Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description= Column(String, unique=True, index=True)

    videos= relationship("Video", back_populates="owner")
   


class  Video(Base):
    __tablename__ ="videos"

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String)
    Meta=Column(String, unique=True, index=True)
    owner_id= Column(Integer, ForeignKey=("Syllabus.id"))

    owner=relationship("Syllabus", back_populates="videos")
