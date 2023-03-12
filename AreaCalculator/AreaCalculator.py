
from abc import ABC, abstractmethod
import math

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

class Square(IShape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side

class Triangle(IShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:
    def calculate_area(self, shape: IShape):
        return shape.calculate_area()

    def calculate_total_area(self, shapes: list):
        total_area = 0

        for shape in shapes:
            total_area += shape.calculate_area()

        return total_area

# Prompt the user to choose a shape and input the required data
shape_choice = input("Choose a shape: (1) Rectangle, (2) Circle, (3) Square, (4) Triangle ")
if shape_choice == '1':
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    shape = Rectangle(length, breadth)
elif shape_choice == '2':
    radius = float(input("Enter the radius of the circle: "))
    shape = Circle(radius)
elif shape_choice == '3':
    side = float(input("Enter the length of a side of the square: "))
    shape = Square(side)
elif shape_choice == '4':
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    shape = Triangle(base, height)
else:
    print("Invalid choice. Please choose a number between 1 and 4.")
    exit()

# Calculate and display the area of the chosen shape
area_calculator = AreaCalculator()
area = area_calculator.calculate_area(shape)
print(f"The area of the {type(shape).__name__} is: {area}")
