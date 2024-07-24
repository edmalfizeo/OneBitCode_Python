from openpyxl import Workbook

# 1 - Create a new workbook
wb = Workbook()
name = 'new_workbook.xlsx'

# 2 - Use the workbook
ws1 = wb.active
ws1.title = 'Sheet1'

# 3 - Add data to the workbook
data = [
    ['Year', 'Profit', 'Cost'],
    [2020, '25%', '75%'],
    [2021, '30%', '70%'],
    [2022, '35%', '65%'],
    [2023, '40%', '60%'],
    [2024, '45%', '55%'],
]

for row in data:
    ws1.append(row)

ws2 = wb.create_sheet(title='Pi')
ws2['D2'] = 3.14159

# 4 - Save the workbook
wb.save(filename=name)

