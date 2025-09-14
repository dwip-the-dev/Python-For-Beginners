# Get input from the user for the number
try:
    number = int(input("Enter a number to display its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

print(f"\nMultiplication table for {number}:")

# Generate and print the multiplication table using a for loop
for i in range(1, 11):  # Loop from 1 to 10
    product = number * i
    print(f"{number} x {i} = {product}")