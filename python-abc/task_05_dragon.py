#!/usr/bin/env python3
# task_05_dragon.py

class SwimMixin:
    """Mixin class to add swimming ability."""

    def swim(self):
        """Prints a message indicating the creature can swim."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying ability."""

    def fly(self):
        """Prints a message indicating the creature can fly."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon, inheriting swimming
      and flying abilities."""

    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")


if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
