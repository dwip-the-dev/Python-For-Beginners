import math

def is_strong_number(num):
    """
    Checks if a given number is a strong number.

    Args:
        num: An integer to check.

    Returns:
        True if the number is a strong number, False otherwise.
    """
    if num < 0:  # Strong numbers are typically defined for non-negative integers
        return False

    original_num = num
    sum_of_factorials = 0

    while num > 0:
        digit = num % 10  # Get the last digit
        sum_of_factorials += math.factorial(digit)  # Add its factorial
        num //= 10  # Remove the last digit

    return sum_of_factorials == original_num

# Test cases
print(f"Is 145 a strong number? {is_strong_number(145)}")  # Expected: True
print(f"Is 123 a strong number? {is_strong_number(123)}")  # Expected: False
print(f"Is 40585 a strong number? {is_strong_number(40585)}") # Expected: True
print(f"Is 0 a strong number? {is_strong_number(0)}")    # Expected: True (0! = 1, sum of factorials of digits of 0 is 1, not 0)
                                                        # Note: The definition of strong numbers can sometimes be debated for 0.
                                                        # According to the strict definition of sum of factorials of *digits*,
                                                        # 0 has no digits, or if considered as a single digit 0, 0! = 1.
                                                        # Thus, 0 is often not considered a strong number by this implementation.