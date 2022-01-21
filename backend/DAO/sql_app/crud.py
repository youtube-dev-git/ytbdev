from sqlalchemy.orm import Session

from . import models, schemas


def get_admin(db: Session, admin_id: int):
    return db.query(models.Admin).filter(models.Admin.id == admin_id).first()


def get_admin_by_email(db: Session, email: str):
    return db.query(models.Admin).filter(models.Admin.email == email).first()

def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Admin).offset(skip).limit(limit).all()


def create_admin(db: Session, admin: schemas.AdminCreate):
    fake_hashed_password = admin.password + "notreallyhashed"
    db_admin = models.Admin(email=admin.email, hashed_password=fake_hashed_password, name =admin.name, photo=admin.photo, phone=admin.phone,gender=admin.gender,statut=admin.statut)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_expert(db: Session, expert_id: int):
    return db.query(models.Expert).filter(models.Expert.id == expert_id).first()


def get_expert_by_email(db: Session, email: str):
    return db.query(models.Expert).filter(models.Expert.email == email).first()

def get_experts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Expert).offset(skip).limit(limit).all()


def create_expert(db: Session, expert: schemas.ExpertCreate):
    fake_hashed_password = expert.password + "notreallyhashed"
    db_expert = models.Expert(email=expert.email, hashed_password=fake_hashed_password, name =expert.name, photo=expert.photo, phone=expert.phone,gender=expert.gender,statut=expert.statut)
    db.add(db_expert)
    db.commit()
    db.refresh(db_expert)
    return db_expert

def get_learner(db: Session, learner_id: int):
    return db.query(models.Learner).filter(models.Learner.id == learner_id).first()


def get_learner_by_email(db: Session, email: str):
    return db.query(models.Learner).filter(models.Learner.email == email).first()

def get_learners(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Learner).offset(skip).limit(limit).all()


def create_learner(db: Session, learner: schemas.LearnerCreate):
    fake_hashed_password = learner.password + "notreallyhashed"
    db_learner = models.Learner(email=learner.email, hashed_password=fake_hashed_password, name =learner.name, photo=learner.photo, phone=learner.phone,gender=learner.gender,statut=learner.statut)
    db.add(db_learner)
    db.commit()
    db.refresh(db_learner)
    return db_learner