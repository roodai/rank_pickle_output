import os
import json
import sys

# Load the JSON file
json_file_path = sys.argv[1]
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    
# Get the directory containing the JSON file
json_dir = os.path.dirname(json_file_path)

# Get the list of filenames from the "order" entry
order = data.get("order", [])
if not isinstance(order, list):
    print("'order' entry should be a list in the JSON.")

# Rename the files
for index, filename in enumerate(order):
    if not isinstance(filename, str):
        print(f"Invalid filename at index {index}: {filename}")
        continue

    # Construct the new filename

    old_filepath = os.path.join(json_dir, "result_"+filename)
    old_filepath = old_filepath+".pkl"
    new_filename = f"ranked_{index}_results.pkl"
    file_extension = os.path.splitext(filename)[1]
    new_filename_with_extension = new_filename + file_extension
    new_filepath = os.path.join(json_dir, new_filename_with_extension)
    # Rename the file
    try:
        os.rename(old_filepath, new_filepath)
        print(f"Renamed '{old_filepath}' to '{new_filepath}'")
    except OSError as e:
        print(f"Error renaming '{old_filepath}': {e}")

print("File renaming completed.")