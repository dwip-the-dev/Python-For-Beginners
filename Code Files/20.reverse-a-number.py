def reverse_number_while_loop(num):
    """
    Reverses an integer using a while loop.
    """
    reversed_num = 0
    while num > 0:
        last_digit = num % 10  # Get the last digit
        reversed_num = (reversed_num * 10) + last_digit  # Add it to the reversed number
        num //= 10  # Remove the last digit from the original number
    return reversed_num

# Example usage:
number = 12345
reversed_result = reverse_number_while_loop(number)
print(f"Original number: {number}")
print(f"Reversed number: {reversed_result}")

number_two = 9870
reversed_result_two = reverse_number_while_loop(number_two)
print(f"Original number: {number_two}")
print(f"Reversed number: {reversed_result_two}")