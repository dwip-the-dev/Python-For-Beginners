import math

def is_prime(num):
    """
    Checks if a given number is prime.
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # If divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors found, it's prime

def generate_primes(limit):
    """
    Generates a list of prime numbers up to a specified limit.
    """
    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

# Example usage:
limit_value = 30
prime_numbers_list = generate_primes(limit_value)
print(f"Prime numbers up to {limit_value}: {prime_numbers_list}")

limit_value_2 = 10
prime_numbers_list_2 = generate_primes(limit_value_2)
print(f"Prime numbers up to {limit_value_2}: {prime_numbers_list_2}")