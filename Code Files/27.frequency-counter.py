def char_frequency_count_method(input_string):
    frequency = {}
    unique_chars = set(input_string)
    for char in unique_chars:
        frequency[char] = input_string.count(char)
    return frequency

my_string = "hello world"
char_counts = char_frequency_count_method(my_string)
print(char_counts)