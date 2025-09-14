file_name = "example.txt"
content_to_write = "Hello, Python!\nThis is a new line of text."

with open(file_name, "w") as file:
    file.write(content_to_write)

print(f"Content written to '{file_name}' (overwriting existing content if any).")