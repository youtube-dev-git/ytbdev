
from typing import List
# from winreg import QueryReflectionKey
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from Permanent_Classes.syllabus import Syllabus
from Permanent_Classes.users import Admin, Learner, Expert
from DAO.DAOObjects import MainDAO
from Types import TypeUser, TypeSyllabus, TypeLogin
from videos_fetcher.system import System


@app.get("/")
def index():
    return { "data" : "Hello World"}

@app.post("/register", status_code = status.HTTP_201_CREATED)
def index(query : TypeUser):
    user = None
    # return {
    #     "data" : "registration working"
    # }
    if(query.status == "admin"):
        user = Admin(**vars(query.user))
    elif(query.status == "learner"):
        user = Learner(**vars(query.user))
    elif(query.status == "expert"):
        user = Expert(**vars(query.user))
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail= "Invalid status")
    # print(user)
    new_user = user.register()
    print(new_user)
    if not new_user :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail= "The user already exists in the site")
    return new_user

@app.post("/login", status_code=status.HTTP_200_OK)
def index(request: TypeLogin):
    # return {
    #     "data" : "login working"
    # }
    user = MainDAO.connect_user(request.email, request.password)
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= "User not found")
    return user

# @app.get("/login", status_code=status.HTTP_200_OK)
# def index():
#     return {
#         "data" : "get worked"
#     }

@app.post("/syllabus")
def saveTraining(query : TypeSyllabus):
    System.save_and_build_syllabus(query.expert_id, query.syllabus)
    return {
        "response" : "Insertion success"
    }

@app.get("/syllabus")
def listTrainings() -> List[Syllabus]:
    return [
                {
                    "id" : 1,
                    "title": "Formation HTML CSS pour les nuls",
                    "lessons": [
                        {
                            "title": "Utilisation des divs",
                            "videos": [
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                },
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                },
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id" : 2,
                    "title": " HTML CSS JS de A à Z",
                    "lessons": [
                        {
                            "title": "Utilisation des divs",
                            "videos": [
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                },
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                },
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                }
                            ]
                        }
                    ]
                },
                {
                    "id" : 3,
                    "title": "FastAPI, le backend manière Fast",
                    "lessons": [
                        {
                            "title": "Utilisation des divs",
                            "videos": [
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                },
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                },
                                {
                                    "video_id": "9TycLR0TqFA",
                                    "title": "Why I didn't ate my father",
                                    "viewCount": 256,
                                    "description": "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
                                    "published_at": "12/12/12",
                                    "thumbnails_medium": "https://jfkdsq",
                                    "channel_id": "fjjfiodsqpjf"
                                }
                            ]
                        }
                    ]
                }
            ]

    return MainDAO.list_trainings()

@app.get("/syllabus/{id}")
def listTrainings(expert_id : int) -> List[Syllabus]:
    return MainDAO.list_expert_trainings(expert_id)