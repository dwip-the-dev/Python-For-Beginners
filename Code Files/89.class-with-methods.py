class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        """
        The constructor method, called when a new instance of Dog is created.
        It initializes instance attributes.
        """
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def bark(self):
        """
        An instance method that makes the dog bark.
        It accesses the instance's name.
        """
        return f"{self.name} says Woof!"

    def get_age_in_human_years(self):
        """
        Another instance method that calculates the dog's age in human years.
        """
        return self.age * 7

    @classmethod
    def create_puppy(cls, name):
        """
        A class method (decorated with @classmethod).
        It takes the class itself (cls) as the first argument and
        can be used as a factory method to create new instances.
        """
        return cls(name, 0) # Create a new Dog instance with age 0

    @staticmethod
    def is_dog_species(animal_species):
        """
        A static method (decorated with @staticmethod).
        It does not take self or cls as its first argument and
        behaves like a regular function within the class namespace.
        """
        return animal_species == Dog.species

# Create instances of the Dog class
my_dog = Dog("Buddy", 5)
another_dog = Dog("Lucy", 2)

# Call instance methods
print(my_dog.bark())
print(f"{my_dog.name}'s age in human years: {my_dog.get_age_in_human_years()}")

print(another_dog.bark())
print(f"{another_dog.name}'s species: {another_dog.species}")

# Call a class method
new_puppy = Dog.create_puppy("Max")
print(f"New puppy's name: {new_puppy.name}, age: {new_puppy.age}")

# Call a static method
print(f"Is 'Canis familiaris' a dog species? {Dog.is_dog_species('Canis familiaris')}")
print(f"Is 'Felis catus' a dog species? {Dog.is_dog_species('Felis catus')}")