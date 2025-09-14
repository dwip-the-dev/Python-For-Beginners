def is_armstrong_number(number):
    """
    Checks if a given number is an Armstrong number.
    """
    # Convert the number to a string to easily get its digits and length
    str_number = str(number)
    num_digits = len(str_number)
    
    sum_of_powers = 0
    for digit_char in str_number:
        digit = int(digit_char)
        sum_of_powers += digit ** num_digits
        
    return sum_of_powers == number

# Example usage:
num1 = 153
if is_armstrong_number(num1):
    print(f"{num1} is an Armstrong number.")
else:
    print(f"{num1} is not an Armstrong number.")

num2 = 1634
if is_armstrong_number(num2):
    print(f"{num2} is an Armstrong number.")
else:
    print(f"{num2} is not an Armstrong number.")

num3 = 123
if is_armstrong_number(num3):
    print(f"{num3} is an Armstrong number.")
else:
    print(f"{num3} is not an Armstrong number.")