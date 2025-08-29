from utils.Geometric import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, width=1, height=1, colour="white", filled=False):
        super().__init__(colour, filled)
        
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def __str__(self):
        return f"{super().__str__()}, width: {self.__width:.2f}, height: {self.__height:.2f}"