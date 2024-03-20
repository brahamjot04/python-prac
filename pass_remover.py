from PyPDF2 import PyPDF2


def remove_password_from_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            pdf_reader.pages[page_num].decrypt(password)
            pdf_writer.add_page(pdf_reader.pages[page_num])

        pdf_writer.write(output_file)


# Usage example
input_path = 'path/to/input.pdf'
output_path = 'path/to/output.pdf'
password = 'your_password'

remove_password_from_pdf(input_path, output_path, password)
