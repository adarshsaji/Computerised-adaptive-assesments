import openpyxl

def get_data():
    name = input("Enter your name: ")
    roll_number = int(input("Enter your roll number: "))


    filename = 'stud_detail.xlsx'
    wb = openpyxl.load_workbook(filename)
    sheet = wb['Sheet1']
    c_val = (len(sheet['A']))
    # wb.get_index()

    sheet.cell(row=c_val+1 , column=1 ).value = name
    sheet.cell(row=c_val+1 , column=2 ).value = roll_number

    wb.save(filename)

