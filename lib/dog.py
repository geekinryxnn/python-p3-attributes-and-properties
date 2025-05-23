#!/usr/bin/env python3


# lib/dog.py

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Unknown", breed="Mastiff"):
        self.name = name  # Use the property setter
        self.breed = breed  # Use the property setter

    def get_name(self):
        return getattr(self, "_name", None)

    def set_name(self, name):
        if type(name) is str and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return getattr(self, "_breed", None)

    def set_breed(self, breed):
        if breed in self.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)

if __name__ == '__main__':
    my_dog = Dog(name="Buddy", breed="Beagle")
    print(f"Dog's name: {my_dog.name}")
    print(f"Dog's breed: {my_dog.breed}")

    my_dog.name = "Super Long Name That Exceeds Twenty-Five Characters"
    my_dog.breed = "Alien"