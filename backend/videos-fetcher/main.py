from fastapi import FastAPI
from classes.syllabus import Syllabus


app = FastAPI()

s = Syllabus("test", 12)
print(s.lessons)

# print(globals())