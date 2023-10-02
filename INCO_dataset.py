import os
import csv
import re
import json
from pdfminer.high_level import extract_text


def remove_empty_lines(text):
    lines = text.split("\n")
    non_empty_lines = [line for line in lines if line.strip()]
    return "\n".join(non_empty_lines)


def process_text(text):
    lines = text.split("\n")
    processed_lines = []

    for line in lines:
        if " f " in line:
            regex = r" f (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(" f " + match.group(1), ""))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif line.startswith("f "):
            regex = r"f (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append("")
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif line.startswith("ø "):
            regex = r"ø (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append("")
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif line.startswith("fø "):
            regex = r"fø (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append("")
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif re.search(r"\s(?:f|ø|fø)\s", line):
            regex = r"\s(?:f|ø|fø)\s(.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(match.group(0), ""))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif re.search(r"^\d+\s[A-Z]+\s", line):
            regex = r"^(\d+\s[A-Z]+\s)(.*)"
            match = re.search(regex, line)
            if match:
                processed_lines.append(match.group(1))
                processed_lines.append(match.group(2))
            else:
                processed_lines.append(line)
        elif " ÆSK " in line:
            regex = r" ÆSK (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(" ÆSK " + match.group(1), ""))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        elif " SÆK " in line:
            regex = r" SÆK (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append(line.replace(" SÆK " + match.group(1), ""))
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        else:
            processed_lines.append(line)

    return processed_lines


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
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                processed_text = process_pdf_file(pdf_path)
                print(processed_text)
                print("\n" + "=" * 20 + "\n")  # Add a separator between files


# Process all PDF files in a folder
pdf_folder_path = "/home/sami/PycharmProjects/pythonProject/inco_1400/pdf"
json_folder_path = (
    "/home/sami/PycharmProjects/pythonProject/inco_1400/json"
)
output_file = (
    "/home/sami/PycharmProjects/pythonProject/inco_1400/aquarium.csv"
)

keywords = []

# Read the keywords from the JSON files
for filename in os.listdir(json_folder_path):
    if filename.endswith(".json"):
        json_path = os.path.join(json_folder_path, filename)
        with open(json_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
            if "Beskrivelse" in data:
                keywords.extend(data["Beskrivelse"])
                # print(keywords)
                # print("-------------------------------------------------------------------------------------")

with open(output_file, "w", newline="", encoding="utf-8-sig") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["File Name", "Processed Text", "Tags"])

    for filename in os.listdir(pdf_folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder_path, filename)

            # Extract text from PDF using pdfminer
            text = extract_text(pdf_path)

            # Condition 1: Remove empty lines
            text = remove_empty_lines(text)

            # Conditions 3, 4, 5, 6, 7, and 8: Process the text
            processed_lines = process_text(text)
            # print(processed_lines)
            processed_lines = [
                line.strip() for line in processed_lines if line.strip()
            ]  # Remove leading/trailing spaces and empty lines
            # print(processed_lines)
            # Now, 'tags' list contains the generated sequence of tags.

            tags = []
            match_found = False
            for i, line in enumerate(processed_lines):
                if line in keywords:
                    if not match_found:
                        tags.append('B-BESKRIVELSE')
                        match_found = True
                    else:
                        tags.append('I-BESKRIVELSE')
                elif "OPDRÆT (Opdrættet i)" in line or "Indespærringsnoter og løftenet" in line or "island" in line or "Solea senegalensis" in line:
                    tags.append('O')
                else:
                    tags.append('O')

            # Write the processed text and tags to the CSV file
            for line, tag in zip(processed_lines, tags):
                writer.writerow([filename, line, tag])