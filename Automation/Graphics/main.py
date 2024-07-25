from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, series

wb = Workbook()
ws = wb.active

data = [
    ['Year', 'Profit', 'Loss'],
    [2010, 100, 50],
    [2011, 150, 75],
    [2012, 200, 100],
    [2013, 250, 125],
    [2014, 300, 150],
    [2015, 350, 175],
]

for row in data:
    ws.append(row)

# Create a chart
chart = AreaChart()
chart.title = 'Profit x Loss'
chart.style = 12
chart.x_axis.title = 'Year'
chart.y_axis.title = 'Porcentage'

categories = Reference(ws, min_col=1, min_row=1, max_row=7)

data = Reference(ws, min_col=2, min_row=1, max_col=3, max_row=7)

chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
ws.add_chart(chart, 'A10')

wb.save('chart.xlsx')

