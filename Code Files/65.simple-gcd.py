import math

def find_gcd_builtin(a, b):
  """
  Calculates the GCD of two numbers using math.gcd().
  """
  return math.gcd(a, b)

# Example usage
num1 = 60
num2 = 48
result = find_gcd_builtin(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")