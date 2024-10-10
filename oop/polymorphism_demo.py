# polymorphism_demo.py

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Area of rectangle

class Circle(Shape):
    def __init_
