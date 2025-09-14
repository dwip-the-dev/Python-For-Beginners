try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")