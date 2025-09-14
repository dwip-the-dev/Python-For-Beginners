def factorial_for_loop(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Example usage:
number = 5
result = factorial_for_loop(number)
print(f"The factorial of {number} is {result}")