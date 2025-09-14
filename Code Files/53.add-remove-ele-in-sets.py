my_set = {1, 2, 3}
my_set.add(4)
print(f"After adding 4: {my_set}")

my_set.update([5, 6])
print(f"After updating with [5, 6]: {my_set}")

my_set.remove(2)
print(f"After removing 2: {my_set}")

my_set.discard(10) # No error, 10 is not in the set
print(f"After discarding 10: {my_set}")

popped_element = my_set.pop()
print(f"Popped element: {popped_element}, Set after pop: {my_set}")

my_set.clear()
print(f"After clearing: {my_set}")