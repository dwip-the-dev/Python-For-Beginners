original_string = "Hello World! Hello Python!"

# Replace all occurrences of "Hello" with "Hi"
new_string_all = original_string.replace("Hello", "Hi")
print(f"After replacing all 'Hello': {new_string_all}")

# Replace only the first occurrence of "Hello" with "Greetings"
new_string_first = original_string.replace("Hello", "Greetings", 1)
print(f"After replacing the first 'Hello': {new_string_first}")

# Replace a substring that does not exist
new_string_no_change = original_string.replace("Java", "C++")
print(f"After trying to replace 'Java': {new_string_no_change}")