def reverse_file_content(input_filename, output_filename):
    """
    Reads the content of input_filename, reverses it as a single string,
    and writes the reversed content to output_filename.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        reversed_content = content[::-1]  # Using string slicing for reversal
        
        with open(output_filename, 'w') as outfile:
            outfile.write(reversed_content)
        print(f"Content of '{input_filename}' reversed and saved to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Create a sample file
with open("sample.txt", "w") as f:
    f.write("This is line one.\n")
    f.write("This is line two.\n")
    f.write("This is line three.")

reverse_file_content("sample.txt", "reversed_sample_content.txt")