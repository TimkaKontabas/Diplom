from DataTypes import days_of_week


def isCellGroup(cell):
    return type(cell) is str and 'группа' in cell

def isRowGroup(row):
    for cell in row:
        if isCellGroup(cell):
            return True
    return False

def isRowOnlyPoint(row:list):
    for cell in row:
        if type(cell) is str and cell == '.':
            continue
        return False
    return True

def isCellDate(cell):
    if type(cell) is not str:
        return False
    temp_arr = cell.split()
    day_of_week, *_ = temp_arr
    return day_of_week.title() in days_of_week
    
def isPractice(cell):
    return type(cell) is str and 'практика' in cell

def isNormalLesson(cell):
    return type(cell) is str and "(" in cell and ")" in cell

def isCabinet(cell):
    return type(cell) is int or (
        type(cell) is str and (
            cell == "библиот"
            or cell == 'фв'
            or cell.lower() == 'эо'
            or cell.split()[0].isnumeric()
        )
    )