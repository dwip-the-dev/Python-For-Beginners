with open("test_example.txt", 'r') as fp:
    lines = len(fp.readlines())
print(f'Total Number of lines: {lines}')