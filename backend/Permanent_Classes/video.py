
from typing import Any
from pydantic.main import BaseModel


class Video(BaseModel):
    videoId : str 
    title : str
    viewCount: int
    description : str 
    published_at : str 
    thumbnails_medium : str
    channel_id : str 
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

# videoJSON = {
#     "items" : {
#         "id" : "1fds45Fj",
#         "snippet" : {
#             "title" : "Why I didn't ate my father",
#             "channelId" : "fjjfiodsqpjf",
#             "description" : "lorem ipsum dolor est jfdksmlq jfdqsjfdmklsqjfdklsqjfmklqs jfkoqsd jmkl fjmklqsd jfkl jqmfj qsdjfmkl dsqmlk jkdsq jmkljf d",
#             "publishedAt" : "12/12/12",
#             "thumbnails" : {
#                 "medium" : {
#                     "url" : "https://jfkdsq"
#                 }
#             }
#         },
#         "statistics" : {
#             "viewCount" : 256
#         }
#     }
# }
