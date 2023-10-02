import os
import tabula
import pandas as pd


def extract_tables(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables


def process_pdf_files(folder_path):
    # Iterate over PDF files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)

            # Extract tables from the PDF file
            tables = extract_tables(pdf_path)

            if tables:
                print(f"Tables extracted from {filename}:")
                for i, table in enumerate(tables):
                    df = pd.DataFrame(table)
                    print(f"Table {i + 1}:")
                    print(df)
                    print("-" * 50)
            else:
                print(f"No tables found in {filename}")
            print()


# Provide the folder path containing the PDF files
folder_path = "/home/sami/PycharmProjects/pythonProject/multi_page/pages"

# Call the function to process PDF files
process_pdf_files(folder_path)
