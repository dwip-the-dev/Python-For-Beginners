# Open the first file in read mode
with open('file1.txt', 'r') as f1:
    content1 = f1.read()

# Open the second file in read mode
with open('file2.txt', 'r') as f2:
    content2 = f2.read()

# Open a new file in write mode to store the merged content
with open('merged_file.txt', 'w') as merged_f:
    # Write content from file1
    merged_f.write(content1)
    # Add a newline for separation if desired
    merged_f.write('\n') 
    # Write content from file2
    merged_f.write(content2)

print("Files merged successfully into 'merged_file.txt'")