try:
    with open("example.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")