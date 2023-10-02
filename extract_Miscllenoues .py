# import os
# import fitz
#
#
# def extract_pdf_data(folder_path):
#     files_without_data = 0  # Counter for files without desired words
#
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             if file.endswith(".pdf"):
#                 file_path = os.path.join(root, file)
#                 print("File name:", file)
#                 print("Folder path:", root)
#
#                 with fitz.open(file_path) as doc:
#                     text = ""
#                     for page in doc:
#                         text += page.get_text()
#
#                     # Find the start and end positions of the desired data
#                     start_index = text.find("Kundenr.")
#                     end_index = text.find("Rabat:")
#
#                     if start_index != -1 and end_index != -1:
#                         data = text[start_index + len("Kundenr."):end_index].strip()
#                         data_list = data.split("\n")
#                         print("Extracted data:")
#                         print(data_list)
#                     else:
#                         end_index = text.find("Rabat ialt denne faktura")
#                         if end_index != -1:
#                             data = text[start_index + len("Kundenr."):end_index].strip()
#                             data_list = data.split("\n")
#                             print("Extracted data:")
#                             print(data_list)
#                         else:
#                             print("Data not found between 'Kundenr.' and 'Rabat:' or 'Rabat ialt denne faktura'")
#                             print("Full text:")
#                             print(text)
#                             files_without_data += 1
#
#                 print("-" * 50)
#
#     print("Number of files without data:", files_without_data)
#
#
# # Provide the folder path where the PDF files are located
# folder_path = "/home/sami/PycharmProjects/pythonProject/inco Aarhus/inco Aarhus"
#
# # Call the function to extract data from PDF files
# extract_pdf_data(folder_path)

# **********************************************************************

import os
import fitz
import shutil


def extract_pdf_data(folder_path):
    files_without_data = 0  # Counter for files without desired words
    output_folder = os.path.join(folder_path, "Files_without_data")
    os.makedirs(output_folder, exist_ok=True)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                print("File name:", file)
                print("Folder path:", root)

                with fitz.open(file_path) as doc:
                    text = ""
                    for page in doc:
                        text += page.get_text()

                    # Find the start and end positions of the desired data
                    start_index = text.find("Varenr.")
                    end_index = text.find("Rabat:")

                    if start_index != -1 and end_index != -1:
                        data = text[start_index + len("Varenr."):end_index].strip()
                        data_list = data.split("\n")
                        print("Extracted data:")
                        print(data_list)
                    else:
                        end_index = text.find("Rabat ialt denne faktura")
                        if end_index != -1:
                            data = text[start_index + len("Varenr."):end_index].strip()
                            data_list = data.split("\n")
                            print("Extracted data:")
                            print(data_list)
                        else:
                            print("Data not found between 'Varenr.' and 'Rabat:' or 'Rabat ialt denne faktura'")
                            print("Full text:")
                            # print(text)
                            files_without_data += 1
                            destination_path = os.path.join(output_folder, file)
                            shutil.move(file_path, destination_path)

                print("-" * 50)

    print("Number of files without data:", files_without_data)


# Provide the folder path where the PDF files are located
folder_path = "/home/sami/PycharmProjects/pythonProject/inco Aarhus/inco Aarhus"

# Call the function to extract data from PDF files
extract_pdf_data(folder_path)
