# Create a file with some initial content (if it doesn't exist)
with open("my_file.txt", "w") as file:
    file.write("This is the original content.\n")
    file.write("Second line of original content.\n")

# Open the file in append mode and add new content
with open("my_file.txt", "a") as file:
    file.write("This line is appended.\n")
    file.write("Another appended line.\n")

# Read and print the entire content of the file to verify
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)