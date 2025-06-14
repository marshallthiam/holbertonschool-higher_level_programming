#!/usr/bin/env python3
# task_01_duck_typing.py

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method for calculating the area of a shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for calculating the perimeter of a shape."""
        pass


class Circle(Shape):
    """Circle class inherits from Shape."""

    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.__radius = abs(radius)  # Make sure the radius is positive

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    """Rectangle class inherits from Shape."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Print the area and perimeter of the shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    # Testing the functionality
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
