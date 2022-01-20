from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    name = Column(String(50), unique=True, index=True)
   # password = Column(String(50), unique=True, index=True)
    photo = Column(String(50))
    gender = Column(String(1))
    phone = Column(String(15))
    status = Column(Integer,index=True)
    
    hashed_password = Column(String(50))
    is_active = Column(Boolean, default=True)
    

   # items = relationship("Item", back_populates="owner")

class Admin(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    users = relationship("Admin", back_populates="Users")
    
class Learner(Base):
    __tablename__ = "learner"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    users = relationship("users", back_populates="Learner")
    
class Expert(Base):
    __tablename__ = "expert"

    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("learner.id"))
    
    leaner = relationship("learner", back_populates="expert")

class Syllabus(Base):
    __tablename__ = "syllabus"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    
class Lesson(Base):
    __tablename__ = "lesson"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    syllabus_id = Column(Integer, ForeignKey("syllabus.id"))
    
    syllabus = relationship("syllabus", back_populates="lesson")
    
class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    viewCount = Column(Integer, index=True)
    description = Column(String(150), index=True)
    publishedAt = Column(String(50), index=True)
    thumbnails = Column(String(50), index=True)
    channel_id = Column(String(50), index=True)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    
    lesson = relationship("lesson", back_populates="video")
    
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    videoid = Column(String, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")