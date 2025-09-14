def factorial_recursive(n):
  """
  Calculates the factorial of a non-negative integer recursively.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """
  # Base case: Factorial of 0 is 1
  if n == 0:
    return 1
  # Recursive step: n! = n * (n-1)!
  else:
    return n * factorial_recursive(n - 1)

# Example usage
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is {result}")

number_zero = 0
result_zero = factorial_recursive(number_zero)
print(f"The factorial of {number_zero} is {result_zero}")