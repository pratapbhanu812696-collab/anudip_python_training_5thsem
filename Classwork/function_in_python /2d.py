import math

# Rectangle
def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Square
def square_area(side):
    return side ** 2

def square_perimeter(side):
    return 4 * side

# Circle
def circle_area(radius):
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

# Triangle
def triangle_area(base, height):
    return 0.5 * base * height

def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3
