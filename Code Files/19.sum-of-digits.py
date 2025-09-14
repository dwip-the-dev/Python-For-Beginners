def sum_of_digits_iterative(number):
    total_sum = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        total_sum += digit
        number //= 10  # Remove the last digit
    return total_sum

# Example usage:
num = 12345
result = sum_of_digits_iterative(num)
print(f"The sum of digits of {num} is: {result}")