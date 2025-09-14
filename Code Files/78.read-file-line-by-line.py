try:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())  # .strip() removes leading/trailing whitespace, including newline characters
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")