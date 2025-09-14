class Car:
    def __init__(self):
        # Initialize the Car with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Creating an instance using the default constructor
car1 = Car()
car1.display_details()