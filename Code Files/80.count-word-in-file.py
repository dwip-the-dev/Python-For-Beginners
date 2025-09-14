def count_words_in_file(filename):
    """
    Counts the total number of words in a given text file.

    Args:
        filename (str): The path to the text file.

    Returns:
        int: The total number of words in the file, or 0 if the file is not found.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()  # Splits by any whitespace (spaces, tabs, newlines)
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

# Example usage:
file_path = "example.txt"  # Replace with your file's path

# Create a dummy file for demonstration
with open(file_path, 'w') as f:
    f.write("This is a sample text file.\nIt has several words.")

total_words = count_words_in_file(file_path)
if total_words > 0:
    print(f"Total number of words in '{file_path}': {total_words}")