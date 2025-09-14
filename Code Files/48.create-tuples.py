# An empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# A tuple with mixed data types
my_tuple = ("apple", 10, 3.14, True)
print(f"Mixed data type tuple: {my_tuple}")

# A tuple with a single element (note the comma)
single_element_tuple = ("banana",)
print(f"Single element tuple: {single_element_tuple}")
print(f"Type of single_element_tuple: {type(single_element_tuple)}")

# A tuple created without parentheses (tuple packing)
another_tuple = 1, 2, "three"
print(f"Tuple created by packing: {another_tuple}")

my_tuple = ("apple", 10, 3.14, True)

# Accessing by positive index
first_element = my_tuple[0]
print(f"First element: {first_element}")

# Accessing by negative index
last_element = my_tuple[-1]
print(f"Last element: {last_element}")

# Slicing a tuple
subset_tuple = my_tuple[1:3]
print(f"Subset of tuple: {subset_tuple}")

