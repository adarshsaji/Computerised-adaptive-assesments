import xlrd
import openpyxl

filename = 'stud_detail.xlsx'
wb = xlrd.open_workbook(filename, encoding_override="utf-8") 
detailfile = wb.sheet_by_index(0)

Checker = {}
response = []
entries = len(detailfile.col(0))
i = 1
while i < entries:
    indexque = 2
    while indexque <= 30:
        q_no = str(detailfile.cell_value(i,indexque))
        indexque += 3
    indexans = 3
    while indexans <= 32:
        ans = int(detailfile.cell_value(i,indexans))
        indexans += 3

    if(q_no not in Checker.keys()):
        Checker[q_no] = []
        Checker[q_no].append(ans)
    else:
        Checker[q_no].append(ans)

    i += 1
    
         

