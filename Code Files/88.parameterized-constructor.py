class Car:
    def __init__(self, make, model, year):
        # Initialize the Car with specific attributes
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Creating instances using the parameterized constructor
car2 = Car("Honda", "Civic", 2022)
car3 = Car("Ford", "Mustang", 2024)

car2.display_details()
car3.display_details()