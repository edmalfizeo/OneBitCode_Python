from openpyxl import Workbook

# 1 - Importing txt file
file_txt = open('gastos.txt', 'r', encoding='utf-8')
file = file_txt.read()
list_data = file.splitlines()

# 2 - Iterating over the list data
for i in range(0, len(list_data)):
    list_data[i] = list_data[i].split(',')


# 3 - Creating a new Excel file
wb = Workbook()
ws = wb.active

for row in list_data:
    ws.append(row)

wb.save('gastos.xlsx')