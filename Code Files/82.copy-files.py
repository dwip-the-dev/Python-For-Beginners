import shutil

# Define the source and destination file paths
source_file = "source.txt"
destination_file = "destination.txt"

# Create a dummy source file for the example
with open(source_file, "w") as f:
    f.write("This is the content of the source file.")

# Copy the file
try:
    shutil.copyfile(source_file, destination_file)
    print(f"File '{source_file}' copied to '{destination_file}' successfully.")
except FileNotFoundError:
    print(f"Error: Source file '{source_file}' not found.")
except PermissionError:
    print(f"Error: Permission denied when copying to '{destination_file}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
