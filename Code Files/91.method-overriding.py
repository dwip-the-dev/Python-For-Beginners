class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create objects of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Call the make_sound method on each object
animal.make_sound()
dog.make_sound()
cat.make_sound()