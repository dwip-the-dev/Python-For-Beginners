def fibonacci_recursive(n):
  """
  Calculates the nth Fibonacci number using recursion.

  Args:
    n: The index of the Fibonacci number to calculate (non-negative integer).

  Returns:
    The nth Fibonacci number.
  """
  if n <= 0:
    return 0  # Base case: The 0th Fibonacci number is 0
  elif n == 1:
    return 1  # Base case: The 1st Fibonacci number is 1
  else:
    # Recursive case: Fn = F(n-1) + F(n-2)
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage:
print(f"The 0th Fibonacci number is: {fibonacci_recursive(0)}")
print(f"The 1st Fibonacci number is: {fibonacci_recursive(1)}")
print(f"The 5th Fibonacci number is: {fibonacci_recursive(5)}")
print(f"The 10th Fibonacci number is: {fibonacci_recursive(10)}")