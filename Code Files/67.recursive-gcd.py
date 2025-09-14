def find_gcd_recursive(a, b):
  """
  Calculates the GCD of two numbers using the recursive Euclidean algorithm.
  """
  if b == 0:
    return a
  else:
    return find_gcd_recursive(b, a % b)

# Example usage
num1 = 18
num2 = 12
result = find_gcd_recursive(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")