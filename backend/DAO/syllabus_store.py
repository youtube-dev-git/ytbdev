from typing import List
from Permanent_Classes.syllabus import Syllabus
from Permanent_Classes.lesson import Lesson
from Permanent_Classes.video import Video


def save_lesson(syllabus_id: int, lesson: Lesson) -> int:
    # Instructions pour sauvegarder une seule lesson
    ...
    
def save_video(lesson_id: int, video: Video):
    # Instructions pour sauvegarder une seule video
    ...
    
def save_syllabus(syllabus: Syllabus) -> int:
    # Instructions pour stocker un syllabus (données de la table syllabus uniquement)
    ...
    
    
def save_lessons(syllabus_id: int, lesson_list: List[Lesson]):
    #Chaque lesson est enregistrée en BD avec pour id du syllabus (clé secondaire) syllabus_id
    for lesson in lesson_list:
        ls_id = save_lesson(syllabus_id, lesson)
        save_videos(ls_id, lesson["videos"])
    
def save_videos(lesson_id: int, video_list: List[Video]):
    #Chaque video est enregistrée en BD avec pour id de la lesson (clé secondaire) lesson_id
    for video in video_list:
        save_video(lesson_id, video)

    

def save_full_syllabus(syllabus: Syllabus):
    sy_id = save_syllabus(syllabus)
    save_lessons(sy_id, syllabus["lessons"])
    