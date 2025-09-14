# Combined example: square only the even numbers
def square(number):
    return number * number

def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

# First, filter for even numbers
even_numbers_filter_object = filter(is_even, numbers)

# Then, map the square function to the filtered even numbers
squared_even_numbers = map(square, even_numbers_filter_object)

# Convert to a list to view the final result
print(list(squared_even_numbers))
# Output: [4, 16, 36]