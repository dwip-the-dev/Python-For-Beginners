class LandAnimal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking on land.")

class WaterAnimal:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(f"{self.name} is swimming in water.")

class AmphibiousAnimal(LandAnimal, WaterAnimal):
    def __init__(self, name):
        # Initialize both parent classes
        LandAnimal.__init__(self, name)
        WaterAnimal.__init__(self, name)

    def live_in_both(self):
        print(f"{self.name} can live in both land and water.")

# Create an object of the AmphibiousAnimal class
frog = AmphibiousAnimal("Frog")

# Access methods from both parent classes
frog.walk()
frog.swim()

# Access method specific to the child class
frog.live_in_both()