import PyPDF2 as pdf
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
import os
from PIL import Image


def get_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        info = reader.metadata
        return info


def extract_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = pdf.PdfReader(file)
        results = []
        for page in range(0, len(reader.pages)):
            selected_page = reader.pages[page]
            text = selected_page.extract_text()
            results.append(text)
        return ' '.join(results)


def split_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = pdf.PdfReader(file)
        for page in range(0, len(reader.pages)):
            selected_page = reader.pages[page]
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            new_filename = f'../files/{filename}_page_{page}.pdf'
            with open(new_filename, 'wb') as new_file:
                writer.write(new_file)
            print(f'PDF created with the name {new_filename}')


def split_pdf_page(pdf_path, start_page: int = 0, end_page: int = 0):
    with(open(pdf_path, 'rb')) as file:
        reader = pdf.PdfReader(file)
        writer = PdfWriter()
        for page in range(start_page, end_page):
            selected_page = reader.pages[page]
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            new_filename = f'../files/{filename}_from_{start_page + 1}_to_{end_page}.pdf'
            with open(new_filename, 'wb') as new_file:
                writer.write(new_file)


def fetch_all_pdf_files(parent_folder):
    pdf_files = []
    for file in os.listdir(parent_folder):
        if file.endswith('.pdf'):
            pdf_files.append(os.path.join(parent_folder, file))
    return pdf_files


def merge_pdf(list_pdfs, output_pdf='../files/final_pdf.pdf'):
    merger = PdfMerger()
    with open(output_pdf, 'wb') as file:
        for pdf_file in list_pdfs:
            merger.append(pdf_file)
        merger.write(file)
        print(f'PDFs merged into {output_pdf}')


def rotate_pdf(pdf_path, page_number: int, rotation: int = 90):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_number])
        writer.pages[page_number].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        new_filename = f'../files/{filename}_rotated_{rotation}.pdf'
        with open(new_filename, 'wb') as new_file:
            writer.write(new_file)
        print(f'PDF rotated and saved as {new_filename}')


def extrac_images_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            for image_obj in selected_page.images:
                with open(f'../files/image_{image_obj.name}.jpg', 'wb') as image_file:
                    image_file.write(image_obj.data)


def convert_img_pdf(img_path):
    image = Image.open(img_path)
    img = image.convert('RGB')
    filename = f'{os.path.splitext(img_path)[0]}.pdf'
    img.save(filename)


# 1 - extract metadata and text from pdf
# print(get_pdf_metadata('../files/sample.pdf'))
# print(get_pdf_metadata('../files/sample2.pdf'))
# print(extract_text('../files/sample.pdf'))
# print(extract_text('../files/sample2.pdf'))

# 2 - Divide the pdf into multiple pdfs
# split_pdf('../files/sample4.pdf')

# 3 - Divide the pdf into multiple pdfs with a range of pages
# split_pdf_page('../files/sample4.pdf', 0, 2)

# 4 - Fetch all pdf files from a folder
# print(fetch_all_pdf_files('../files'))
# pdf_list = fetch_all_pdf_files('../files')
# merge_pdf(pdf_list)

# 5 - Rotate a pdf
# rotate_pdf('../files/sample4.pdf', 0)

# 6 - Extract images from a pdf
# extrac_images_from_pdf('../files/pdf_image.pdf')

# 7 - Convert an image to pdf
convert_img_pdf('../files/image_I1.jpg.jpg')
