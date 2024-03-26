from abc import ABC, abstractmethod

class GeometricShape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(GeometricShape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(GeometricShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
class Triangle(GeometricShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height
    
class Polygon(GeometricShape):
    def __init__(self, sides, side_lengths):
        self.sides = sides
        self.side_lengths = side_lengths

    def get_area(self):
        # polygon calculation
        pass