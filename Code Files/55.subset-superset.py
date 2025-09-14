# Define two sets
set_A = {1, 2, 3, 4, 5, 6}
set_B = {1, 3, 5}
set_C = {1, 7}

# Check if set_A is a superset of set_B
is_superset_AB = set_A.issuperset(set_B)
print(f"Is set_A a superset of set_B? {is_superset_AB}")

# Check if set_A is a superset of set_C
is_superset_AC = set_A.issuperset(set_C)
print(f"Is set_A a superset of set_C? {is_superset_AC}")