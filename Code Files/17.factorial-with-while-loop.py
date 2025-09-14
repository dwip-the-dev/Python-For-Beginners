def factorial_while_loop(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0:
        return 1
    else:
        fact = 1
        i = 1
        while i <= n:
            fact *= i
            i += 1
        return fact

# Example usage:
number = 7
result = factorial_while_loop(number)
print(f"The factorial of {number} is {result}")