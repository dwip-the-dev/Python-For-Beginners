# Sorting numbers in ascending order
numbers = [4, 2, 1, 3, 5]
numbers.sort()
print(f"Sorted ascending: {numbers}")

# Sorting numbers in descending order
numbers = [4, 2, 1, 3, 5]
numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}")

# Sorting strings alphabetically
fruits = ["banana", "apple", "orange", "kiwi"]
fruits.sort()
print(f"Sorted alphabetically: {fruits}")

# Sorting with a custom key (by string length)
fruits = ["banana", "apple", "orange", "kiwi", "mango"]
fruits.sort(key=len)
print(f"Sorted by length: {fruits}")