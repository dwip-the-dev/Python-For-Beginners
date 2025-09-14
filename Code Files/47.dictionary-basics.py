# 1. Creating a dictionary
# Keys must be immutable (strings, numbers, tuples), values can be any data type.
student_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": [90, 85, 92]
}
print(f"Initial dictionary: {student_info}")

# 2. Accessing values
# Access values using their corresponding keys in square brackets.
print(f"Student's name: {student_info['name']}")
print(f"Student's age: {student_info['age']}")

# Using .get() method to access values safely (returns None or a default if key not found)
print(f"Student's city (using .get()): {student_info.get('city', 'Not specified')}")

# 3. Modifying values
# Assign a new value to an existing key.
student_info["age"] = 21
print(f"Updated age: {student_info['age']}")

# 4. Adding new key-value pairs
# Assign a value to a new key.
student_info["university"] = "State University"
print(f"Dictionary after adding university: {student_info}")

# 5. Removing key-value pairs
# Using del keyword
del student_info["grades"]
print(f"Dictionary after removing grades: {student_info}")

# Using .pop() method (removes and returns the value)
major = student_info.pop("major")
print(f"Removed major: {major}")
print(f"Dictionary after popping major: {student_info}")

# 6. Iterating through a dictionary
print("Iterating through keys:")
for key in student_info:
    print(key)

print("Iterating through values:")
for value in student_info.values():
    print(value)

print("Iterating through key-value pairs:")
for key, value in student_info.items():
    print(f"{key}: {value}")