from sqlalchemy.orm import Session

from . import models, schemas


def get_syllabus(db: Session, syllabus_id: int):
    return db.query(models.Syllabus).filter(models.Syllabus.id == syllabus_id).first()


def get_syllabus_by_title(db: Session, title: str):
    return db.query(models.Syllabus).filter(models.Syllabus.title == title).first()

def get_All_syllabus(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Syllabus).offset(skip).limit(limit).all()


def create_syllabus(db: Session, syllabus: schemas.SyllabusCreate):
    db_syllabus = models.Syllabus(title=syllabus.title, description=syllabus.description)
    db.add(db_syllabus)
    db.commit()
    db.refresh(db_syllabus)
    return db_syllabus

def create_video(db: Session, video: schemas.VideoCreate, syllabus_id: int):
    db_video = models.Video(**video.dict(), owner_id=syllabus_id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video
    