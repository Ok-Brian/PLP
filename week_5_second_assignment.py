# Base class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")


# Subclasses with their own move() implementations
class Dog(Animal):
    def move(self):
        print("Running ")


class Bird(Animal):
    def move(self):
        print("Flying")


class Fish(Animal):
    def move(self):
        print("Swimming ")


class Horse(Animal):
    def move(self):
        print("Galloping ")


# --- Main Program ---
animals = [Dog(), Bird(), Fish(), Horse()]

for a in animals:
    a.move()   # Now directly prints instead of returning
