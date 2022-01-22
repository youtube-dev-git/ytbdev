from typing import List
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class DAOObjects2(BaseModel):
    @app.post("/syllabus/", response_model=schemas.Syllabus)
    def create_syllabus(syllabus: schemas.SyllabusCreate, db: Session = Depends(get_db)):
        db_syllabus = crud.get_syllabus_by_title(db, title=syllabus.title)
        if db_syllabus:
            raise HTTPException(status_code=400, detail="Syllabus already registered")
        return crud.create_syllabus(db=db, syllabus=syllabus)


    @app.get("/syllabus/", response_model=List[schemas.Syllabus])
    def read_All_syllabus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        syllabus = crud.get_All_syllabus(db, skip=skip, limit=limit)
        return syllabus


    @app.get("/syllabus/{syllabus_id}", response_model=schemas.Syllabus)
    def read_syllabus(syllabus_id: int, db: Session = Depends(get_db)):
        db_syllabus = crud.get_syllabus(db, syllabus_id=syllabus_id)
        if db_syllabus is None:
            raise HTTPException(status_code=404, detail="Syllabus not found")
        return db_syllabus

    @app.post("/syllabus/{syllabus_id}/lessons/" , response_model=schemas.Lesson)
    def create_syllabus_lessons(syllabus_id: int, lessons: schemas.LessonCreate, db: Session = Depends(get_db)
    ):
        return crud.create_lesson(db=db, lessons=lessons, syllabus_id=syllabus_id)


    @app.post("/syllabus/{lessons_id}/video/" , response_model=schemas.Video)
    def create_video_lesson(lessons_id: int, video: schemas.VideoCreate, db: Session = Depends(get_db)
    ):
        return crud.create_video(db=db, video=video, lessons_id=lessons_id)