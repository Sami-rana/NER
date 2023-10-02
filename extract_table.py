# import os
# import tabula
# import pandas as pd
# import shutil
#
#
# def extract_tables(pdf_path):
#     tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
#     return tables
#
#
# def process_pdf_files(folder_path):
#     # Create a directory to store PDF files without tables
#     no_table_directory = os.path.join(folder_path, "no_table")
#     os.makedirs(no_table_directory, exist_ok=True)
#
#     # Variables for tracking PDF files without tables
#     files_without_table = []
#     files_without_table_count = 0
#
#     # Iterate over PDF files in the folder
#     for filename in os.listdir(folder_path):
#         if filename.endswith(".pdf"):
#             pdf_path = os.path.join(folder_path, filename)
#
#             # Extract tables from the PDF file
#             tables = extract_tables(pdf_path)
#
#             if tables:
#                 print(f"Tables extracted from {filename}:")
#                 for i, table in enumerate(tables):
#                     df = pd.DataFrame(table)
#                     print(f"Table {i + 1}:")
#                     print(df)
#                     print("-" * 50)
#             else:
#                 # Move PDF file to the "no_table" directory
#                 files_without_table.append(filename)
#                 files_without_table_count += 1
#                 new_path = os.path.join(no_table_directory, filename)
#                 shutil.move(pdf_path, new_path)
#                 print(f"No tables found in {filename}. Moved to 'no_table' directory.")
#             print()
#
#     print("PDF files without tables:")
#     for file in files_without_table:
#         print(file)
#
#     print("Total PDF files without tables:", files_without_table_count)
#
#
# # Provide the folder path containing the PDF files
# folder_path = "/home/sami/PycharmProjects/pythonProject/multi_page/pages"
#
# # Call the function to process PDF files
# process_pdf_files(folder_path)
# **************************************************************

import os
import tabula
import pandas as pd
import shutil


def extract_tables(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables


def process_pdf_files(folder_path):
    # Create a directory to store PDF files without tables
    no_table_directory = os.path.join(folder_path, "no_table")
    os.makedirs(no_table_directory, exist_ok=True)

    # Variables for tracking PDF files without tables
    files_without_table = []
    files_without_table_count = 0

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

                    # Create a separate CSV file for each table
                    # csv_filename = f"{os.path.splitext(filename)[0]}_table{i + 1}.csv"
                    # csv_path = os.path.join(folder_path, csv_filename)
                    # df.to_csv(csv_path, index=False)
                    # print(f"CSV file created: {csv_filename}")
                    # print()
            else:
                # Move PDF file to the "no_table" directory
                files_without_table.append(filename)
                files_without_table_count += 1
                new_path = os.path.join(no_table_directory, filename)
                shutil.move(pdf_path, new_path)
                print(f"No tables found in {filename}. Moved to 'no_table' directory.")
            print()

    print("PDF files without tables:")
    for file in files_without_table:
        print(file)

    print("Total PDF files without tables:", files_without_table_count)


# Provide the folder path containing the PDF files
folder_path = "/home/sami/PycharmProjects/pythonProject/multi_page/pages"

# Call the function to process PDF files
process_pdf_files(folder_path)
