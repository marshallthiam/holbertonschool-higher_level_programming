#!/usr/bin/env python3
# task_04_flyingfish.py

class Fish:
    """A class representing a fish."""

    def swim(self):
        """Prints a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message indicating the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Prints a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message indicating the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Prints a message indicating the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message indicating the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mro())
