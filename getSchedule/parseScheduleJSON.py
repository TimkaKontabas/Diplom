import json
from typing import List
from pydantic import BaseModel
from parseGroupData import parseGroupData
from DataTypes import *
from CheckFunc import *


def getSheduleJSON() -> List[list]:
    with open('output.json', encoding='utf-8') as f:
        return json.load(f)
    

def parseScheduleJSON():
    data = getSheduleJSON()
    shedule = Schedule(groups=[], dates=[], data=[])
    shedule.groups = parseGroups(data)
    shedule.dates = parseDates(data)
    shedule.data = parseGroupData(data, shedule.groups)
    return shedule


def parseGroups(data) -> List[int]:
    groups = []
    for row in data:
        for cell in row:
            if isCellGroup(cell):
                group_nomer, _ = cell.split()
                groups.append(int(group_nomer))
    return groups

def parseDates(data) -> List[str]:
    def dates_sort(dates):
        tmp_arr = [
            ((days_of_week[date.split()[0].title()]), date)
            for date in dates
        ]
        tmp_arr.sort(key=lambda x: x[0])
        return [x[1] for x in tmp_arr]
    dates = set()
    for row in data:
        for cell in row:
            if isCellDate(cell):
                dates.add(" ".join(cell.split()))
                break
    dates = list(dates)
    sorted_dates = dates_sort(dates)
    return sorted_dates

shedule = parseScheduleJSON()
with open('shedule.json', 'w', encoding='utf-8') as f:
    print(shedule.model_dump_json(indent=4), file=f)