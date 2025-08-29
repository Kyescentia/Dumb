from utils.Geometric import GeometricObject
import math

class Circle(GeometricObject):
    def __init__(self, radius=1.0, colour="white", filled=False):
        super().__init__(colour, filled)
        
        self.__radius = float(radius)

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = float(radius)

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    def __str__(self):
        return (f"{super().__str__()}, radius: {self.get_radius():.2f}, "
                f"area: {self.get_area():.2f}, perimeter: {self.get_perimeter():.2f}")