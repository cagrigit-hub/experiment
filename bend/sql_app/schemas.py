from typing import List, Union

from pydantic import BaseModel


class LectureBase(BaseModel):
    id: int
    title: str
   
class LectureCreate(LectureBase):
    pass

class Lecture(LectureBase):
    id: int
    title: str
    class Config:
        orm_mode = True

