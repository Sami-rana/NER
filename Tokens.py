import os
import csv
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
        elif re.search(r'\b(f|ø|fø)\s\w+\s', line):
            regex = r'\b(f|ø|fø)\s(\w+)\s(.+)'
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(match.group(0), ''))
                processed_lines.append(match.group(1) + ' ' + match.group(2))
                processed_lines.append(match.group(3))
            else:
                processed_lines.append(line)
        elif re.match(r'(\d+\s[A-Z]{2,3})\s', line):
            regex = r'(\d+\s[A-Z]{2,3})\s(.*)'
            match = re.match(regex, line)
            if match:
                processed_lines.append(match.group(1))
                processed_lines.append(match.group(2))
            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)

    return processed_lines


# Process all PDF files in a folder
folder_path = '/home/sami/PycharmProjects/pythonProject/single_page'
output_file = 'output.csv'

with open(output_file, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['File Name', 'Processed Text'])

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)

            # Extract text from PDF using pdfminer
            text = extract_text(pdf_path)

            # Condition 1: Remove empty lines
            text = remove_empty_lines(text)

            # Conditions 3, 4, 5, 6, 7, and 8: Process the text
            processed_lines = process_text(text)

            # Write the processed text to the CSV file
            for line in processed_lines:
                writer.writerow([filename, line])
