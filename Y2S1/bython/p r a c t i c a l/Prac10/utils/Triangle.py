from utils.Geometric import GeometricObject
import math

class Triangle(GeometricObject):
    """
    Represents a triangle, extending the GeometricObject class.
    """
    def __init__(self, side1=1.0, side2=1.0, side3=1.0, colour="white", filled=False):
        """
        Constructor for a Triangle object.
        Initializes the three sides and calls the parent constructor.
        """
        # Call the parent class (GeometricObject) constructor
        super().__init__(colour, filled)
        
        # Initialize its own specific data fields
        self.__side1 = float(side1)
        self.__side2 = float(side2)
        self.__side3 = float(side3)

    # Accessor methods for all three data fields
    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    def get_perimeter(self):
        """Calculates and returns the perimeter of the triangle."""
        return self.__side1 + self.__side2 + self.__side3

    def get_area(self):
        """
        Calculates and returns the area of the triangle using Heron's formula.
        Returns 0 if the sides do not form a valid triangle.
        """
        s = self.get_perimeter() / 2
        # Use Heron's formula: Area = sqrt(s(s-a)(s-b)(s-c))
        # The value inside the sqrt can be negative if the sides don't form a
        # valid triangle (i.e., side1 + side2 <= side3). We check for this.
        area_squared = s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)
        if area_squared < 0:
            return 0  # Not a valid triangle
        else:
            return math.sqrt(area_squared)

    def __str__(self):
        """
        Overrides the parent's __str__ method to provide a full
        description of the triangle.
        """
        base_string = super().__str__()
        triangle_string = (f", side1: {self.__side1:.2f}, side2: {self.__side2:.2f}, "
                           f"side3: {self.__side3:.2f}, area: {self.get_area():.2f}, "
                           f"perimeter: {self.get_perimeter():.2f}")
        return base_string + triangle_string

# Helper function for robust user input for the sides
def get_valid_side(prompt):
    """
    Prompts the user for a side and validates the input.
    Ensures the input is a positive floating-point number.
    """
    while True:
        try:
            side = float(input(prompt))
            if side > 0:
                return side
            else:
                # This handles cases like 0 or -9
                print("Error: Wrong input!")
        except ValueError:
            # This handles non-numeric input like 'ty'
            print("Error: Only floating-point numbers are allowed!")
