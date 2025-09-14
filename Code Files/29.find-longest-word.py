words = ["apple", "banana", "kiwi", "grapefruit", "orange"]
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"The longest word is: {longest_word}")