# ||||||||||||||||||||||||||||||||||||||\Count total tags in csv file||||||||||||||||||||||||||||||||||||||
import pandas as pd


def count_tags_in_file(csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Initialize variables to keep track of the counts
    total_count = 0
    current_file = None
    current_count = 0

    # Iterate through the DataFrame
    for index, row in df.iterrows():
        file_name, token, tag = row

        # If the file name has changed, print the count for the previous file
        if file_name != current_file and current_file is not None:
            print(f"File: {current_file}, Total tags: {current_count}")
            total_count += current_count
            current_count = 0

        # Count only the specified tags (B-BESKRIVELSE and I-BESKRIVELSE)
        if tag == "B-BESKRIVELSE" or tag == "I-BESKRIVELSE":
            current_count += 1

        # Update the current_file variable for the next iteration
        current_file = file_name

    # Print the count for the last file in the dataset
    print(f"File: {current_file}, Total tags: {current_count}")
    total_count += current_count

    # Print the overall count across all files
    print(f"Total tags in all files: {total_count}")


# Replace 'your_dataset.csv' with the actual filename of your CSV dataset
count_tags_in_file('inco_dataset_updated_1186.csv')

# #
# import pandas as pd
# import json
# import os
#
#
# def read_json_files(json_folder):
#     json_data = {}
#     for filename in os.listdir(json_folder):
#         if filename.endswith('.json'):
#             with open(os.path.join(json_folder, filename), 'r') as json_file:
#                 data = json.load(json_file)
#                 json_data[filename] = data.get('Beskrivelse', [])
#     return json_data
#
#
# def count_tags_in_files(csv_file, json_data):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(csv_file)
#
#     # Initialize variables to keep track of the counts
#     total_count = 0
#
#     # Iterate through the DataFrame
#     for index, row in df.iterrows():
#         file_name, token, tag = row
#
#         # If the file name exists in the JSON data
#         if file_name in json_data:
#             # Count only the specified tags (B-BESKRIVELSE and I-BESKRIVELSE)
#             if tag == "B-BESKRIVELSE" or tag == "I-BESKRIVELSE":
#                 total_count += 1
#
#             # Remove the item from the JSON list if it exists
#             item = token.strip()  # Remove leading/trailing whitespaces from the token
#             if item in json_data[file_name]:
#                 json_data[file_name].remove(item)
#         # else:
#         #     print(f"File: {file_name} doesn't have matching JSON data!")
#
#     # Print the count for each file and its remaining JSON data
#     for file_name, items in json_data.items():
#         print(f"File: {file_name}, Item Count: {len(items)}, Tag Count: {total_count}")
#
#     # Print the overall count across all files
#     print(f"Total tags in all files: {total_count}")
#
#
# # Replace 'your_dataset.csv' with the actual filename of your CSV dataset
# # Replace 'your_json_folder' with the folder containing the JSON files
# csv_file = '/home/sami/PycharmProjects/pythonProject/inco_dataset.csv'
# json_folder = '/home/sami/PycharmProjects/pythonProject/pdf_json/inco_json_files'
#
# # Read the JSON files and store the data in a dictionary
# json_data = read_json_files(json_folder)
#
# # Count the tags in the CSV file and match with JSON data
# count_tags_in_files(csv_file, json_data)

# #
# import pandas as pd
#
#
# def count_tags_in_file(csv_file):
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(csv_file)
#
#     # Initialize variables to keep track of the counts
#     total_count = 0
#     current_file = None
#     current_count = 0
#
#     # Iterate through the DataFrame
#     for index, row in df.iterrows():
#         file_name, token, tag = row
#
#         # If the file name has changed, print the count for the previous file
#         if file_name != current_file and current_file is not None:
#             print(f"File: {current_file}, Total tags: {current_count}")
#             total_count += current_count
#             current_count = 0
#
#         # Count only the specified tags (B-BESKRIVELSE and I-BESKRIVELSE)
#         if tag == "B-BESKRIVELSE" or tag == "I-BESKRIVELSE":
#             current_count += 1
#
#         # Update the current_file variable for the next iteration
#         current_file = file_name
#
#     # Print the count for the last file in the dataset
#     print(f"File: {current_file}, Total tags: {current_count}")
#     total_count += current_count
#
#     # Print the overall count across all files
#     print(f"Total tags in all files: {total_count}")
#
#     # Count total tags in the entire CSV file
#     total_tags_in_csv = df[df['Tags'].isin(['B-BESKRIVELSE', 'I-BESKRIVELSE'])].shape[0]
#     print(f"Total tags in the CSV file: {total_tags_in_csv}")
#
#
# # Replace 'your_dataset.csv' with the actual filename of your CSV dataset
# count_tags_in_file('inco_dataset (1).csv')
# #
# import os
# import json
#
#
# def count_items_in_json_lists(folder_path):
#     """
#     Counts the number of items in the 'Beskrivelse' list for each JSON file in the specified folder.
#
#     Args:
#         folder_path (str): Path to the folder containing JSON files.
#
#     Returns:
#         dict: A dictionary with filenames as keys and the count of 'Beskrivelse' items as values.
#     """
#     result = {}
#
#     # Check if the folder path is valid
#     if not os.path.isdir(folder_path):
#         raise ValueError("Invalid folder path. Please provide a valid path to the folder containing JSON files.")
#
#     # Iterate through all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#
#         # Check if the file is a JSON file
#         if os.path.isfile(file_path) and filename.lower().endswith('.json'):
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     data = json.load(file)
#
#                 # Check if the 'Beskrivelse' key exists in the JSON data
#                 if 'Beskrivelse' in data and isinstance(data['Beskrivelse'], list):
#                     result[filename] = len(data['Beskrivelse'])
#
#             except (IOError, json.JSONDecodeError) as e:
#                 # Handle exceptions like file reading error or JSON decoding error
#                 print(f"Error processing {filename}: {str(e)}")
#
#     return result
#
#
# if __name__ == "__main__":
#     folder_path = "/home/sami/PycharmProjects/pythonProject/pdf_json/inco_json_files"  # Replace with the actual folder path
#     result = count_items_in_json_lists(folder_path)
#
#     for filename, count in result.items():
#         print(f"{filename}: {count} items in 'Beskrivelse' list.")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||COUNT total ITEMS FROM JSON||||||||||||||||||||||||||||||||||||||
#
# import os
# import json
#
#
# def count_items_in_json_lists(folder_path):
#     """
#     Counts the number of items in the 'Beskrivelse' list for each JSON file in the specified folder.
#
#     Args:
#         folder_path (str): Path to the folder containing JSON files.
#
#     Returns:
#         dict: A dictionary with filenames as keys and the count of 'Beskrivelse' items as values.
#         int: Total count of items in the 'Beskrivelse' lists across all JSON files.
#     """
#     result = {}
#     total_items = 0
#
#     # Check if the folder path is valid
#     if not os.path.isdir(folder_path):
#         raise ValueError("Invalid folder path. Please provide a valid path to the folder containing JSON files.")
#
#     # Iterate through all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#
#         # Check if the file is a JSON file
#         if os.path.isfile(file_path) and filename.lower().endswith('.json'):
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     data = json.load(file)
#
#                 # Check if the 'Beskrivelse' key exists in the JSON data
#                 if 'Beskrivelse' in data and isinstance(data['Beskrivelse'], list):
#                     item_count = len(data['Beskrivelse'])
#                     result[filename] = item_count
#                     total_items += item_count
#
#             except (IOError, json.JSONDecodeError) as e:
#                 # Handle exceptions like file reading error or JSON decoding error
#                 print(f"Error processing {filename}: {str(e)}")
#
#     return result, total_items
#
#
# if __name__ == "__main__":
#     folder_path = "/home/sami/PycharmProjects/pythonProject/inco_vendor_dataset/inco_json_files"  # Replace with the actual folder path
#     result, total_items = count_items_in_json_lists(folder_path)
#
#     for filename, count in result.items():
#         print(f"{filename}: {count} items in 'Beskrivelse' list.")
#
#     print(f"Total items in 'Beskrivelse' lists across all files: {total_items}")
#

# ||||||||||||||||||||||||||||||||||||||||FIND MISMATCH TAGS||||||||||||||||||||||||||||||||||||||||||||||||
# import os
# import json
# import pandas as pd
#
#
# def check_json_items_in_csv(folder_path, csv_file_path):
# """ Checks if JSON list items exist in the 'Tokens' column
# of CSV file for rows with Tags 'B-BESKRIVELSE' and 'I-BESKRIVELSE'.
#
#     Args:
#         folder_path (str): Path to the folder containing JSON files.
#         csv_file_path (str): Path to the CSV file.
#
#     Returns:
#         list: A list of file names where at least one item doesn't match the 'Tokens' column in CSV.
#     """
#     mismatched_files = []
#
#     # Check if the folder path is valid
#     if not os.path.isdir(folder_path):
#         raise ValueError("Invalid folder path. Please provide a valid path to the folder containing JSON files.")
#
#     # Check if the CSV file path is valid
#     if not os.path.isfile(csv_file_path):
#         raise ValueError("Invalid CSV file path. Please provide a valid path to the CSV file.")
#
#     # Read the CSV file using pandas
#     df = pd.read_csv(csv_file_path)
#
#     # Filter rows with Tags 'B-BESKRIVELSE' and 'I-BESKRIVELSE'
#     filtered_df = df[df['Tags'].isin(['B-BESKRIVELSE', 'I-BESKRIVELSE'])]
#
#     # Iterate through all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#
#         # Check if the file is a JSON file
#         if os.path.isfile(file_path) and filename.lower().endswith('.json'):
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     data = json.load(file)
#
#                 # Check if the 'Beskrivelse' key exists in the JSON data
#                 if 'Beskrivelse' in data and isinstance(data['Beskrivelse'], list):
#                     for item in data['Beskrivelse']:
#                         # Check if the item exists in the 'Tokens' column of filtered_df
#                         if item not in filtered_df['Processed Text'].values:
#                             mismatched_files.append(filename)
#                             break
#
#             except (IOError, json.JSONDecodeError) as e:
#                 # Handle exceptions like file reading error or JSON decoding error
#                 print(f"Error processing {filename}: {str(e)}")
#
#     return mismatched_files
#
#
# if __name__ == "__main__": folder_path = "/home/sami/PycharmProjects/pythonProject/pdf_json/inco_json_files"  #
# Replace with the actual folder path csv_file_path = "/home/sami/Downloads/inco_dataset (1).csv"  # Replace with the
# actual CSV file path
#
#     mismatched_files = check_json_items_in_csv(folder_path, csv_file_path)
#
# if mismatched_files: print("Mismatched files:") for filename in mismatched_files: print(filename) else: print("All
# items in JSON lists match the 'Tokens' column in CSV for rows with Tags 'B-BESKRIVELSE' and 'I-BESKRIVELSE'.")

#
# import os
# import json
# import pandas as pd
#
#
# def count_items_in_json_lists(folder_path, csv_file_path):
#     """
#     Counts the number of items in the 'Beskrivelse' list for each JSON file and counts the occurrences of
#     tags 'B-BESKRIVELSE' and 'I-BESKRIVELSE' in the CSV file.
#
#     Args:
#         folder_path (str): Path to the folder containing JSON files.
#         csv_file_path (str): Path to the CSV file.
#
#     Returns:
#         dict: A dictionary with filenames as keys and the count of 'Beskrivelse' items as values.
#         dict: A dictionary with tags as keys and their count in the CSV file as values.
#     """
#     result = {}
#     tags_count = {'B-BESKRIVELSE': 0, 'I-BESKRIVELSE': 0}
#
#     # Check if the folder path is valid
#     if not os.path.isdir(folder_path):
#         raise ValueError("Invalid folder path. Please provide a valid path to the folder containing JSON files.")
#
#     # Check if the CSV file path is valid
#     if not os.path.isfile(csv_file_path):
#         raise ValueError("Invalid CSV file path. Please provide a valid path to the CSV file.")
#
#     # Read the CSV file using pandas
#     df = pd.read_csv(csv_file_path)
#
#     # Iterate through all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#
#         # Check if the file is a JSON file
#         if os.path.isfile(file_path) and filename.lower().endswith('.json'):
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     data = json.load(file)
#
#                 # Check if the 'Beskrivelse' key exists in the JSON data
#                 if 'Beskrivelse' in data and isinstance(data['Beskrivelse'], list):
#                     item_count = len(data['Beskrivelse'])
#                     result[filename] = item_count
#
#                 # Count occurrences of tags 'B-BESKRIVELSE' and 'I-BESKRIVELSE' in the CSV file
#                 file_tags_count = df[df['File Name'] == filename]['Tags'].value_counts().to_dict()
#                 for tag, count in file_tags_count.items():
#                     if tag in tags_count:
#                         tags_count[tag] += count
#
#             except (IOError, json.JSONDecodeError) as e:
#                 # Handle exceptions like file reading error or JSON decoding error
#                 print(f"Error processing {filename}: {str(e)}")
#
#     return result, tags_count
#
#
# if __name__ == "__main__":
#     folder_path = "/home/sami/PycharmProjects/pythonProject/inco_vendor_dataset/inco_json_files"  # Replace with the actual folder path
#     csv_file_path = "dataset_1.csv"  # Replace with the actual CSV file path
#
#     items_count, tags_count = count_items_in_json_lists(folder_path, csv_file_path)
#
#     print("Items count for each file:")
#     for filename, count in items_count.items():
#         print(f"{filename}: {count} items in 'Beskrivelse' list.")
#
#     print("\nTags count in the CSV file:")
#     for tag, count in tags_count.items():
#         print(f"{tag}: {count} occurrences.")
#
# import os
# import json
# import pandas as pd
#
#
# def count_items_in_json_lists(folder_path, csv_file_path):
#     """
#     Counts the number of items in the 'Beskrivelse' list for each JSON file and counts the occurrences of
#     tags 'B-BESKRIVELSE' and 'I-BESKRIVELSE' in the CSV file.
#
#     Args:
#         folder_path (str): Path to the folder containing JSON files.
#         csv_file_path (str): Path to the CSV file.
#
#     Returns:
#         dict: A dictionary with filenames as keys and the count of 'Beskrivelse' items as values.
#         dict: A dictionary with tags as keys and their count in the CSV file as values.
#     """
#     result = {}
#     tags_count = {'B-BESKRIVELSE': 0, 'I-BESKRIVELSE': 0}
#
#     # Check if the folder path is valid
#     if not os.path.isdir(folder_path):
#         raise ValueError("Invalid folder path. Please provide a valid path to the folder containing JSON files.")
#
#     # Check if the CSV file path is valid
#     if not os.path.isfile(csv_file_path):
#         raise ValueError("Invalid CSV file path. Please provide a valid path to the CSV file.")
#
#     # Read the CSV file using pandas
#     df = pd.read_csv(csv_file_path)
#
#     # Iterate through all files in the folder
#     for filename in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, filename)
#
#         # Check if the file is a JSON file
#         if os.path.isfile(file_path) and filename.lower().endswith('.json'):
#             try:
#                 with open(file_path, 'r', encoding='utf-8') as file:
#                     data = json.load(file)
#
#                 # Check if the 'Beskrivelse' key exists in the JSON data
#                 if 'Beskrivelse' in data and isinstance(data['Beskrivelse'], list):
#                     item_count = len(data['Beskrivelse'])
#                     result[filename] = item_count
#
#                 # Count occurrences of tags 'B-BESKRIVELSE' and 'I-BESKRIVELSE' in the CSV file
#                 file_tags_count = df[df['File Name'] == filename]['Tags'].value_counts().to_dict()
#                 for tag, count in file_tags_count.items():
#                     if tag in tags_count:
#                         tags_count[tag] += count
#
#             except (IOError, json.JSONDecodeError) as e:
#                 # Handle exceptions like file reading error or JSON decoding error
#                 print(f"Error processing {filename}: {str(e)}")
#
#     return result, tags_count
#
#
# if __name__ == "__main__":
#     folder_path = "/home/sami/PycharmProjects/pythonProject/inco_vendor_dataset/inco_json_files"  # Replace with the actual folder path
#     csv_file_path = "/home/sami/PycharmProjects/pythonProject/dataset_1.csv"  # Replace with the actual CSV file path
#
#     items_count, tags_count = count_items_in_json_lists(folder_path, csv_file_path)
#
#     print("Items count for each file:")
#     for filename, count in items_count.items():
#         print(f"{filename}: {count} items in 'Beskrivelse' list.")
#
#     print("\nTags count in the CSV file:")
#     for tag, count in tags_count.items():
#         print(f"{tag}: {count} occurrences.")
