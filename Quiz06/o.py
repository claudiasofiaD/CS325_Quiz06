from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width
    
def main():
    circle = Circle(radius=5)
    square = Square(side_length = 4)
    rectangle = Rectangle(length = 6, width = 3)

    print(f"Circle area: {circle.get_area()}")
    print(f"Square area: {square.get_area()}")
    print(f"Rectangle area: {rectangle.get_area()}")

if __name__ == "__main__":
    main()
    