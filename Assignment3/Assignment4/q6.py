class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


rectangle = Rectangle("Rectangle", 5, 10)
circle = Circle("Circle", 7)
triangle = Triangle("Triangle", 6, 8)

print("Area of", rectangle.name, ":", rectangle.area())
print("Area of", circle.name, ":", circle.area())
print("Area of", triangle.name, ":", triangle.area())