class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

def make_animal_speak(animal):
    """
    This function demonstrates polymorphism by accepting any object
    that has a 'speak' method.
    """
    print(animal.speak())

# Create instances of different animal types
my_dog = Dog()
my_cat = Cat()
my_duck = Duck()

# Call the function with different animal objects
make_animal_speak(my_dog)
make_animal_speak(my_cat)
make_animal_speak(my_duck)