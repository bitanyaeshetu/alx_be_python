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
    def __init__(self, radius):
        self.radius = radius  # Initializing the radius attribute

    def area(self):
        return math.pi * (self.radius ** 2)  # Area of circle using radius with exponentiation

def main():
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(5, 3)  # Length 5, Width 3
    circle = Circle(4)            # Radius 4

    # List of shapes
    shapes = [rectangle, circle]

    # Calculate and print areas
    for shape in shapes:
        print(f"The area is: {shape.area()}")

if __name__ == "__main__":
    main()
