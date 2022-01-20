
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
# get admin

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

######################

@app.post("/admins/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_admin(db=db, admin=admin)


@app.get("/admins/", response_model=list[schemas.Admin])
def read_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    admins = crud.get_admins(db, skip=skip, limit=limit)
    return admins


@app.get("/admins/{admin_id}", response_model=schemas.Admin)
def read_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = crud.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

#######################

@app.post("/experts/", response_model=schemas.Expert)
def create_expert(expert: schemas.ExpertCreate, db: Session = Depends(get_db)):
    db_expert = crud.get_expert_by_email(db, email=expert.email)
    if db_expert:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_expert(db=db, expert=expert)


@app.get("/experts/", response_model=list[schemas.Expert])
def read_experts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    experts = crud.get_experts(db, skip=skip, limit=limit)
    return experts


@app.get("/experts/{expert_id}", response_model=schemas.Expert)
def read_expert(expert_id: int, db: Session = Depends(get_db)):
    db_expert = crud.get_expert(db, expert_id=expert_id)
    if db_expert is None:
        raise HTTPException(status_code=404, detail="Expert not found")
    return db_expert

#########################

@app.post("/learners/", response_model=schemas.Learner)
def create_learner(learner: schemas.LearnerCreate, db: Session = Depends(get_db)):
    db_learner = crud.get_learner_by_email(db, email=learner.email)
    if db_learner:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_learner(db=db, learner=learner)


@app.get("/learners/", response_model=list[schemas.Learner])
def read_learners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    learners = crud.get_learners(db, skip=skip, limit=limit)
    return learners


@app.get("/learners/{learner_id}", response_model=schemas.Learner)
def read_learner(learner_id: int, db: Session = Depends(get_db)):
    db_learner = crud.get_learner(db, learner_id=learner_id)
    if db_learner is None:
        raise HTTPException(status_code=404, detail="Learner not found")
    return db_learner