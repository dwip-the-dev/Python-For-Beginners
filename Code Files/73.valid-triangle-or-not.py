def is_valid_triangle(a, b, c):
  """
  Checks if three given side lengths can form a valid triangle.

  Args:
    a: The length of the first side.
    b: The length of the second side.
    c: The length of the third side.

  Returns:
    True if the side lengths can form a valid triangle, False otherwise.
  """
  if (a + b > c) and (a + c > b) and (b + c > a):
    return True
  else:
    return False

# Example usage:
side1 = 7
side2 = 10
side3 = 5

if is_valid_triangle(side1, side2, side3):
  print(f"The sides {side1}, {side2}, and {side3} can form a valid triangle.")
else:
  print(f"The sides {side1}, {side2}, and {side3} cannot form a valid triangle.")

side4 = 3
side5 = 4
side6 = 8

if is_valid_triangle(side4, side5, side6):
  print(f"The sides {side4}, {side5}, and {side6} can form a valid triangle.")
else:
  print(f"The sides {side4}, {side5}, and {side6} cannot form a valid triangle.")