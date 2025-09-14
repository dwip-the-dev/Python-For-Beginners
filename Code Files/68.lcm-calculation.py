import math

def calculate_lcm(num1, num2):
  """
  Calculates the Least Common Multiple (LCM) of two numbers.

  Args:
    num1: The first integer.
    num2: The second integer.

  Returns:
    The LCM of num1 and num2.
  """
  # LCM can be calculated using the formula: LCM(a, b) = |a * b| / GCD(a, b)
  # where GCD is the Greatest Common Divisor.
  # Python's math module provides a gcd function.
  
  # Ensure positive numbers for LCM calculation, though the formula handles negative inputs correctly
  # by taking the absolute value of the product.
  lcm_result = abs(num1 * num2) // math.gcd(num1, num2)
  return lcm_result

# Example usage:
number1 = 12
number2 = 15

lcm = calculate_lcm(number1, number2)
print(f"The LCM of {number1} and {number2} is {lcm}")

# Another example:
number3 = 4
number4 = 6
lcm2 = calculate_lcm(number3, number4)
print(f"The LCM of {number3} and {number4} is {lcm2}")