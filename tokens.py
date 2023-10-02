import os
import re
from pdfminer.high_level import extract_text


def remove_empty_lines(text):
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    return '\n'.join(non_empty_lines)


def process_text(text):
    lines = text.split('\n')
    processed_lines = []

    for line in lines:
        if ' f ' in line:
            regex = r' f (.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(' f ' + match.group(1), ''))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif line.startswith('f '):
            regex = r'f (.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append('')
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif line.startswith('ø '):
            regex = r'ø (.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append('')
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif line.startswith('fø '):
            regex = r'fø (.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append('')
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif re.search(r'\s(?:f|ø|fø)\s', line):
            regex = r'\s(?:f|ø|fø)\s(.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(match.group(0), ''))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif re.search(r'^\d+\s[A-Z]+\s', line):
            regex = r'^(\d+\s[A-Z]+\s)(.*)'
            match = re.search(regex, line)
            if match:
                processed_lines.append(match.group(1))
                processed_lines.append(match.group(2))
            else:
                processed_lines.append(line)
        elif ' ÆSK ' in line:
            regex = r' ÆSK (.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(' ÆSK ' + match.group(1), ''))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif ' SÆK ' in line:
            regex = r' SÆK (.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(' SÆK ' + match.group(1), ''))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)

    return '\n'.join(processed_lines)


def process_pdf_file(pdf_path):
    text = extract_text(pdf_path)
    # Condition 1: Remove empty lines
    text = remove_empty_lines(text)
    # Conditions 3, 4, 5, 6, 7, 8, 9, and 10: Process the text
    processed_text = process_text(text)
    return processed_text


def process_pdf_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                processed_text = process_pdf_file(pdf_path)
                print(processed_text)
                print('\n' + '=' * 20 + '\n')  # Add a separator between files
                print(file)


# Replace 'path/to/your/pdf_folder' with the actual path to your PDF folder
pdf_folder_path = '/home/sami/PycharmProjects/pythonProject/inco_vendor_dataset/inco_pdf_files'
process_pdf_folder(pdf_folder_path)
