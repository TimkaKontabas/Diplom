from typing import List
from DataTypes import *
from CheckFunc import *


class ParserGroupData:
    def __init__(self, groups:List[int]):
        self.groups = groups
        count_group = len(groups)
        self.data = [[DayLessons(day=i, data=[]) for i in range(6)] for _ in range(count_group)]
        self.currentGroup = 0 # индекс текущей группы
        self.count_new_group = 0 # Количество новых групп (для обновления индекса)

    def addGroupData(self, day:int, lessons: List[Lesson]):
        """Метод добавляет данные к РАЗНЫМ группам из одной строки расписания"""
        self.count_new_group = len(lessons) if len(lessons) > self.count_new_group else self.count_new_group
        for nomer, lesson in enumerate(lessons):
            try:
                if nomer + self.currentGroup >= len(self.data):
                    break
                dayLessons = self.data[nomer + self.currentGroup][day]
                dayLessons.data.append(lesson)
            except Exception as e:
                print(nomer, self.currentGroup, day, lessons)
                print(e)
                exit()
            
    def updateCurrentGroup(self):
        self.currentGroup += self.count_new_group
        self.count_new_group = 0

    def getGroupData(self) -> List[GroupData]:
        return [GroupData(group=nomer_group, data=group) for nomer_group, group in zip(self.groups, self.data)]

def parseGroupData(data:List[list], count_groups:int) -> List[GroupData]:
    day = -1
    parserGroupData = ParserGroupData(count_groups)
    for row in data:
        if isCellDate(row[0]):
            day += 1
            row = row[1:]
        if isCellGroup(row[0]):
            parserGroupData.updateCurrentGroup()
            day = -1
            continue
        if isRowOnlyPoint(row):
            continue
        lessons = getLessonsInRow(row)
        parserGroupData.addGroupData(day, lessons)
    return parserGroupData.getGroupData()
        
def getLessonsInRow(row:list) -> List[Lesson]:
    new_row = []
    for cell in row:
        new_row.append(cell)
        # if not isCabinet(cell) and not isNormalLesson(cell):
        #     new_row.append("")
    row = new_row
    if len(row) % 2 != 0:
        raise Exception(f"Неправильное количество ячейек в строке.\n {row}")
    lessons = [Lesson(name=str(row[i]), location=str(row[i+1])) for i in range(0, len(row), 2)]
    
    return lessons
