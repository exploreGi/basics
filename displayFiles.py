import os

# Get the current directory
current_directory = os.getcwd()

# Loop through all files in the current directory
for filename in os.listdir(current_directory):
    # Check if the file has a .md extension
    if filename.endswith('.md'):
        # Construct the full file path
        file_path = os.path.join(current_directory, filename)
        
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            print(f"Contents of {filename}:\n")
            print(file.read())
            print("\n" + "="*40 + "\n")  # Separator between files
