import openpyxl
import json
from CheckFunc import isRowOnlyPoint


def getSheduleSheet():
    wb = openpyxl.load_workbook('schedule.xlsx')
    return wb['Лист2']

def isFilledCell(cell, is_can_empty:bool):
    return (
        (cell.value is not None and (
        (
            type(cell.value) is str and cell.value.strip() != ''
        ) or (
            type(cell.value) is int and cell.value > 10
        )))
        or is_can_empty
    )

def printSheet():
    sheet = getSheduleSheet()

    table = []
    for row in sheet.iter_rows():
        filtered_row = [cell.value if cell.value is not None else "." for nomer, cell in enumerate(row) if isFilledCell(cell, 1 < nomer < 10)]
        if len(filtered_row) > 0 and not isRowOnlyPoint(filtered_row):
            table.append(filtered_row)
    table = table[1:-2]
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(table, f, ensure_ascii=False, indent=4)
                

printSheet()