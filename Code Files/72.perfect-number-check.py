def is_perfect_number(num):
    """
    Checks if a given number is a perfect number.

    Args:
        num: An integer to be checked.

    Returns:
        True if the number is perfect, False otherwise.
    """
    if num <= 0:
        return False  # Perfect numbers are positive integers

    sum_of_divisors = 0
    for i in range(1, num):  # Iterate from 1 up to (num - 1) to find proper divisors
        if num % i == 0:
            sum_of_divisors += i

    return sum_of_divisors == num

# Example usage:
number_to_check = 28
if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")

number_to_check = 12
if is_perfect_number(number_to_check):
    print(f"{number_to_check} is a perfect number.")
else:
    print(f"{number_to_check} is not a perfect number.")