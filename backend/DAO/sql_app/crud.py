from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_admin(db: Session, user_id: int):
    return db.query(models.User,models.Admin).filter(models.User.id == models.Admin.user_id).first()


def get_admin_by_email(db: Session, email: str):
    return db.query(models.User,models.Admin).filter((models.User.email == email & models.User.id) == models.Admin.user_id).first()

def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User,models.Admin).filter(models.User.id == models.Admin.user_id).offset(skip).limit(limit).all()

def get_learner(db: Session, user_id: int):
    return db.query(models.User,models.Learner).filter(models.User.id == models.Learner.user_id).first()


def get_learner_by_email(db: Session, email: str):
    return db.query(models.User,models.Learner).filter((models.User.email == email & models.User.id) == models.Learner.user_id).first()

def get_learners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User,models.Learner).filter(models.User.id == models.Learner.user_id).offset(skip).limit(limit).all()

def get_expert(db: Session, user_id: int):
    return db.query(models.User,models.Learner,models.Expert).filter((models.User.id == models.Learner.user_id)==models.Expert.learner_id).first()


def get_expert_by_email(db: Session, email: str):
    return db.query(models.User,models.Expert,models.Expert).filter((models.User.email == email & models.User.id == models.Learner.user_id)==models.Expert.learner_id).first()

def get_experts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User,models.Expert).filter((models.User.id == models.Learner.user_id)==models.Expert.learner_id).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
