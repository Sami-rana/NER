# from pdfminer.high_level import extract_text
#
#
# def extract_data_from_pdf(pdf_path):
#     extracted_text = extract_text(pdf_path)
#     lines = extracted_text.split('\n')
#     filtered_lines = []
#
#     for line in lines:
#         # Condition 1
#         if line.startswith('f') or line.startswith('ø') or line.startswith('fø'):
#             line = line.replace('f', '').replace('ø', '').replace('fø', '')
#
#         # Condition 2
#         elif len(line) >= 4 and line[0].isdigit() and line[1].isspace() and line[2].isupper() and line[3] in (
#         'f', 'ø', 'fø'):
#             continue
#         else:
#             line = line.split(' ', 3)[-1]  # Keep the data after the first 3 spaces
#
#         filtered_lines.append(line.strip())
#
#     extracted_data = '\n'.join(filtered_lines)
#     return extracted_data
#
#
# pdf_path = "/home/sami/PycharmProjects/pythonProject/single_page/inv-0ocM2-1670392968.pdf"
# extracted_data = extract_data_from_pdf(pdf_path)
# print(extracted_data)
#

# from pdfminer.high_level import extract_text
# import re
#
# def extract_data_from_pdf(pdf_path):
#     extracted_text = extract_text(pdf_path)
#     lines = extracted_text.split('\n')
#     filtered_lines = []
#
#     for line in lines:
#         # Condition 1
#         if line.startswith('f') or line.startswith('ø') or line.startswith('fø'):
#             line = line.replace('f', '').replace('ø', '').replace('fø', '')
#
#         # Condition 2
#         elif re.match(r'^\d\s[A-Z][^\s]*\s', line):
#             line = re.sub(r'^\d\s[A-Z][^\s]*\s', '', line)
#
#         filtered_lines.append(line.strip())
#
#     extracted_data = '\n'.join(filtered_lines)
#     return extracted_data
#
#
# pdf_path = "/home/sami/PycharmProjects/pythonProject/single_page/inv-0ocM2-1670392968.pdf"
# extracted_data = extract_data_from_pdf(pdf_path)
# print(extracted_data)

#
# from pdfminer.high_level import extract_text
# import re
#
#
# def extract_data_from_pdf(pdf_path):
#     extracted_text = extract_text(pdf_path)
#     lines = extracted_text.split('\n')
#     filtered_lines = []
#
#     for line in lines:
#         # Condition 1
#         if line.startswith(('f', 'ø', 'fø')):
#             continue
#
#         # Condition 2
#         match = re.match(r'^(\d)\s([A-Z].*)$', line)
#         if match:
#             numeric_value = match.group(1)
#             remaining_text = match.group(2)
#             if remaining_text.find(' ') >= 0:
#                 line = remaining_text.split(' ', 1)[1]
#             else:
#                 line = remaining_text
#
#         filtered_lines.append(line.strip())
#
#     extracted_data = '\n'.join(filtered_lines)
#     return extracted_data
#
#
# pdf_path = "/home/sami/PycharmProjects/pythonProject/single_page/inv-0ocM2-1670392968.pdf"
# extracted_data = extract_data_from_pdf(pdf_path)
# print(extracted_data)


# import re
# from pdfminer.high_level import extract_text
# import os
#
# def process_text(text):
#     # Condition 1: Remove empty lines
#     text = re.sub(r'\n\s*\n', '\n', text)
#
#     # Condition 2, 3, 4, 5: Split lines based on conditions
#     lines = text.split('\n')
#     processed_lines = []
#     for line in lines:
#         line = line.strip()
#         if line.startswith(('f', 'ø', 'fø')):
#             # Condition 3: Break the line after 'f', 'ø', or 'fø'
#             line = re.sub(r'(f|ø|fø)\s', r'\1\n', line)
#             processed_lines.append(line)
#         elif re.match(r'\d+\s[A-Z]{2,3}\s(f|ø|fø)', line):
#             # Condition 4: Shift line after numeric value + uppercase letters + 'f', 'ø', or 'fø'
#             match = re.match(r'(\d+\s[A-Z]{2,3})\s(f|ø|fø)(.*)', line)
#             shifted_line = match.group(1) + '\n' + match.group(2) + match.group(3)
#             processed_lines.append(shifted_line)
#         elif re.match(r'\d+\s[A-Z]{2,3}\s', line):
#             # Condition 5: Shift line after numeric value + uppercase letters
#             match = re.match(r'(\d+\s[A-Z]{2,3})(.*)', line)
#             shifted_line = match.group(1) + '\n' + match.group(2)
#             processed_lines.append(shifted_line)
#         else:
#             processed_lines.append(line)
#
#     processed_text = '\n'.join(processed_lines)
#     return processed_text
#
#
# folder_path = '/home/sami/PycharmProjects/pythonProject/single_page'
# Specify the path to the folder containing the PDF files
#
# # Iterate over the PDF files in the folder
# for filename in os.listdir(folder_path):
#     if filename.endswith('.pdf'):
#         file_path = os.path.join(folder_path, filename)
#
#         # Extract the text from the PDF file
#         text = extract_text(file_path)
#
#         # Process the extracted text
#         processed_text = process_text(text)
#
#         # Print or save the processed text
#         print(processed_text)
#         # You can save the processed text to a file using:
#         # with open('processed_text.txt', 'w') as f:
#         #     f.write(processed_text)

import re
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    text_stream = StringIO()
    laparams = LAParams()
    device = TextConverter(resource_manager, text_stream, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    with open(pdf_path, 'rb') as pdf_file:
        for page in PDFPage.get_pages(pdf_file):
            interpreter.process_page(page)

    text = text_stream.getvalue()
    device.close()
    text_stream.close()

    return text


def process_text(text):
    # Condition 1: Remove empty lines
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    text = '\n'.join(non_empty_lines)

    # Condition 2: Process product names

    # Condition 3: Shift data after "f" surrounded by spaces
    text = re.sub(r'\s+f\s+', r'\n', text)

    # Condition 4: Shift data after "f" at line start
    text = re.sub(r'^f\s+', r'\n', text, flags=re.MULTILINE)

    # Condition 5: Shift data after "ø" at line start
    text = re.sub(r'^ø\s+', r'\n', text, flags=re.MULTILINE)

    # Condition 6: Shift data after "fø" at line start
    text = re.sub(r'^fø\s+', r'\n', text, flags=re.MULTILINE)

    # Condition 7: Shift data after two spaces
    text = re.sub(r'(\d+)\s{2}', r'\1\n', text)

    # Condition 8: Shift data after "f" or "ø"
    text = re.sub(r'([fø])\s+', r'\n', text)

    return text


# Example usage
pdf_path = '/home/sami/PycharmProjects/pythonProject/single_page/inv-0ocM2-1670392968.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
processed_text = process_text(extracted_text)

print(processed_text)
