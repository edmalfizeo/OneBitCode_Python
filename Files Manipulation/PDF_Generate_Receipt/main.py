from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Variables

client = input('Enter the client name: ')
consultant = input('Please specify the type of consultation: ')
value = input('Enter the value of the consultation:\n')
value_msg = f"{value} Reais"
value_ext = num2words(float(value), lang='pt_BR')
value_ext_msg = f"{value_ext} Reais"
data = date.today()
day = data.day
month = data.month
year = data.year


# 2 - Layout of the PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 18)
pdf.image('rec.jpg', x=0, y=0)
pdf.text(162, 45, value_msg)
pdf.text(80, 86, client)
pdf.text(80, 110, value_ext_msg)
pdf.text(80, 137, consultant)
pdf.set_text_color(255, 255, 255)
pdf.text(30, 193, str(day))
pdf.text(50, 193, str(month))
pdf.text(70, 193, str(year))
file_name = f'{client}_{consultant}_{data}.pdf'
pdf.output(file_name)
print('PDF generated successfully!')