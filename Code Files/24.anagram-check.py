def are_anagrams(str1, str2):
    # Convert strings to lowercase to handle case-insensitivity
    str1 = str1.lower()
    str2 = str2.lower()

    # Check if the lengths are different; if so, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    return sorted_str1 == sorted_str2

# Example Usage:
string1 = "Listen"
string2 = "Silent"
if are_anagrams(string1, string2):
    print(f"'{string1}' and '{string2}' are anagrams.")
else:
    print(f"'{string1}' and '{string2}' are not anagrams.")

string3 = "Hello"
string4 = "World"
if are_anagrams(string3, string4):
    print(f"'{string3}' and '{string4}' are anagrams.")
else:
    print(f"'{string3}' and '{string4}' are not anagrams.")