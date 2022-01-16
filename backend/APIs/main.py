from fastapi import FastAPI
from .user import User
from ..DAO.DAOObject import DAOObject

app = FastAPI()
db = DAOObject()

@app.post("/register")
def index(status: str, user : User):
    db.save_expert(user)
    pass