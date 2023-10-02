import fitz
import os
import re
import argparse
import json


def process_text(text):
    lines = text.split("\n")
    # print(text)
    processed_lines = []

    for line in lines:

        line = re.sub(r'\s+', ' ', line)

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
        # Add more conditions here...
        # elif "ø " in line:
        #     regex = r"ø (.+)"
        #     match = re.search(regex, line)
        #     if match:
        #         processed_lines.append("")
        #         processed_lines.append(match.group(1))
        #     else:
        #         processed_lines.append(line)
        elif re.match(r"^\s*ø (.+)", line):
            regex = r"ø (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append(match.group(1))


        elif "fø " in line:
            regex = r"fø (.+)"
            match = re.search(regex, line)
            if match:
                processed_lines.append("")
                processed_lines.append(match.group(1))
            else:
                processed_lines.append(line)
        # Add more conditions here...
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
        # Skip lines starting with numeric value and space, or containing only uppercase text
        elif re.match(r"^\d+\s[A-ZÆØÅÉÆØÅa-z0-9\s\-!@#$%^&*()_+=[\]{}|;:'\",.<>?/\\]+", line):
            continue
        # Skip lines containing only numeric values with length less than 4
        elif line.isdigit() and len(line) < 4:
            continue
        # Skip lines starting with numeric value containing dot, comma, or both
        elif re.match(r"^-?\d+[,.]\d+", line):
            continue
        # Skip lines starting with "D-mærke"
        elif line.startswith("D-mærke"):
            continue
        elif line in ["D", "f", "ø", "fø"]:
            continue
        elif re.match(r"^-", line):
            continue
        elif "Subtotal" == line:
            continue
        elif re.match(r"^\.\s*\.\s*\.\s*\.\s*\.\s*\.\s*\.\s*\.$", line):
            continue
        else:
            processed_lines.append(line)
    return processed_lines


def extract_lines_with_condition(lines):
    processed_lines = []
    start_extraction = False

    for line in lines:
        if "Varenr." in line:
            start_extraction = True
        if start_extraction and "subtotal" in line:
            break
        if start_extraction and re.match(r"^-?\d+\s[A-Z]+", line):
            continue
        if re.match(r"^[A-ZÆØÅÉ]+$", line):
            continue
        if start_extraction:
            processed_lines.append(line)

    return processed_lines


def extract_products(lines):
    processed_lines = []
    extract_next_line = False
    start_extraction = False

    for line in lines:
        if not line.strip():  # Skip empty lines
            continue
        if re.match(r"^\d{4,6}$", line) and '.' not in line and ',' not in line:
            extract_next_line = True
        elif extract_next_line:
            processed_lines.append(line)
            extract_next_line = False
    return processed_lines


def split_text_into_lines(text):
    lines = text.splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    return non_empty_lines


def pdf_to_model_predictions(pdf_path):
    full_processed_text = ""
    with fitz.open(pdf_path) as pdf:
        for page_number in range(pdf.page_count):
            page = pdf.load_page(page_number)
            page_text = page.get_text()

            page_text_cleaned = page_text.replace("�", " ")
            processed_text = process_text(page_text_cleaned)
            trimmed_text = extract_lines_with_condition(processed_text)
            products = extract_products(trimmed_text)
            # processed_text_as_string = "\n".join(trimmed_text)
            processed_text_as_string = "\n".join(products)

            full_processed_text += processed_text_as_string + "\n"

            # full_processed_text += page_text + "\n"

    return full_processed_text


def create_json_files(folder_path, pdf_filename, list_of_products):
    json_folder = os.path.join(folder_path, "json_files")
    os.makedirs(json_folder, exist_ok=True)

    json_filename = pdf_filename.replace(".pdf", ".json")
    json_path = os.path.join(json_folder, json_filename)

    data = {"Beskrivelse": list_of_products}

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def process_folder(folder_path):
    count = 1
    for filename in os.listdir(folder_path):
        count += 1
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            print(f"{count}- Processing: {pdf_path}")
            text = pdf_to_model_predictions(pdf_path)
            list_of_products = split_text_into_lines(text)
            count_products = len(list_of_products)
            print(list_of_products)

            # create_json_files(folder_path, filename, list_of_products)  # Add this line

            print(text)
            print("=" * 40)

    return count_products


def main():
    parser = argparse.ArgumentParser(description="Process PDF files in a folder.")
    parser.add_argument("folder_path", help="Path to the folder containing PDF files")
    args = parser.parse_args()

    process_folder(args.folder_path)


if __name__ == "__main__":
    main()
