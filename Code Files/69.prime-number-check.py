import math

def is_prime(number):
    """
    Checks if a given number is a prime number.

    A prime number is a natural number greater than 1 that has no positive divisors
    other than 1 and itself.
    """
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for divisibility from 2 up to the square root of the number.
    # We only need to check up to the square root because if a number 'n' has a divisor
    # greater than its square root, it must also have a divisor smaller than its square root.
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False  # If divisible, it's not prime

    return True  # If no divisors found, it's prime

# Example usage:
num1 = 29
num2 = 10
num3 = 1

if is_prime(num1):
    print(f"{num1} is a prime number.")
else:
    print(f"{num1} is not a prime number.")

if is_prime(num2):
    print(f"{num2} is a prime number.")
else:
    print(f"{num2} is not a prime number.")

if is_prime(num3):
    print(f"{num3} is a prime number.")
else:
    print(f"{num3} is not a prime number.")