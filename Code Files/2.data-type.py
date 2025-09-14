# variables_and_data_types.py

# 🔥 Basic Types
integer_num = 42
float_num = 3.14159
complex_num = 2 + 3j
string_data = "Dwip the Dev"
boolean_val = True
none_val = None

print("Integer:", integer_num, type(integer_num))
print("Float:", float_num, type(float_num))
print("Complex:", complex_num, type(complex_num))
print("String:", string_data, type(string_data))
print("Boolean:", boolean_val, type(boolean_val))
print("NoneType:", none_val, type(none_val))

# 🔥 Sequence Types
list_data = [1, 2, 3, "hello", 3.14]
tuple_data = (1, "tuple", False, 99.9)
range_data = range(5)

print("\nList:", list_data, type(list_data))
print("Tuple:", tuple_data, type(tuple_data))
print("Range:", list(range_data)), print(type(range_data))

# 🔥 Mapping Type
dict_data = {
    "name": "Dwip",
    "age": 16,
    "coder": True,
    "skills": ["Python", "HTML", "JS"]
}
print("\nDictionary:", dict_data, type(dict_data))

# 🔥 Set Types
set_data = {1, 2, 2, 3, 4}
frozenset_data = frozenset([5, 6, 6, 7, 8])
print("Set:", set_data, type(set_data))
print("Frozenset:", frozenset_data, type(frozenset_data))

# 🔥 Binary Types
bytes_data = b"hello"
bytearray_data = bytearray(b"mutable")
memoryview_data = memoryview(b"bytes")

print("\nBytes:", bytes_data, type(bytes_data))
print("Bytearray:", bytearray_data, type(bytearray_data))
print("Memoryview:", memoryview_data, type(memoryview_data))

# 🔥 Advanced Shit: Dynamic typing
var = 100
print("\nInitially:", var, type(var))
var = "Now I'm a string 💀"
print("After reassignment:", var, type(var))
var = [1, 2, 3]
print("After changing again:", var, type(var))

# 🔥 Demonstrating mutability
immutable_str = "python"
mutable_list = [1, 2, 3]

try:
    immutable_str[0] = "P"  # ❌ will fail
except TypeError as e:
    print("\nImmutable Example:", e)

mutable_list[0] = 99
print("Mutable Example:", mutable_list)

# 🔥 Show truthy & falsy values
truthy = [1, "string", [0]]
falsy = [0, "", [], None, False]

print("\nTruthy values:", [bool(x) for x in truthy])
print("Falsy values:", [bool(x) for x in falsy])