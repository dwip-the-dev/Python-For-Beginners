def fibonacci_with_loop(n):
    """
    Generates the Fibonacci sequence up to n terms using a for loop.
    """
    if n <= 0:
        print("Please enter a positive integer.")
        return
    elif n == 1:
        print("Fibonacci sequence:", 0)
        return

    a, b = 0, 1
    print("Fibonacci sequence:")
    print(a, end=" ")  # Print the first term
    print(b, end=" ")  # Print the second term

    for _ in range(2, n):  # Loop from the third term up to n
        next_fib = a + b
        print(next_fib, end=" ")
        a = b
        b = next_fib
    print() # Newline for better formatting

# Example usage:
num_terms = 10
fibonacci_with_loop(num_terms)

num_terms_single = 1
fibonacci_with_loop(num_terms_single)

num_terms_invalid = -5
fibonacci_with_loop(num_terms_invalid)