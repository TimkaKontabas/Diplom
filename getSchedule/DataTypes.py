from typing import List, Set
from pydantic import BaseModel

class Lesson(BaseModel):
    name: str
    location: str

class DayLessons(BaseModel):
    day: int
    data: List[Lesson]

class GroupData(BaseModel):
    group: int
    data: List[DayLessons]

class Schedule(BaseModel):
    groups: List[int]
    dates: List[str]
    data: List[GroupData]

days_of_week = {
    'Понедельник': 1,
    'Вторник': 2,
    'Среда': 3,
    'Четверг': 4,
    'Пятница': 5,
    'Суббота': 6,
    'Воскресенье': 7
}