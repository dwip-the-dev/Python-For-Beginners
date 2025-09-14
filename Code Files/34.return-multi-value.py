def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

data = [10, 20, 30, 40, 50]
sum_val, avg_val, max_val, min_val = calculate_stats(data)

print(f"Sum: {sum_val}")
print(f"Average: {avg_val}")
print(f"Maximum: {max_val}")
print(f"Minimum: {min_val}")