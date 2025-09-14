def find_gcd_euclidean(a, b):
  """
  Calculates the GCD of two numbers using the iterative Euclidean algorithm.
  """
  while b:
    a, b = b, a % b
  return a

# Example usage
num1 = 100
num2 = 30
result = find_gcd_euclidean(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")