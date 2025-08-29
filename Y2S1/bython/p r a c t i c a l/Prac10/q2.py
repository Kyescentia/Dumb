from utils.Geometric import *
from utils.Triangle import *


print("Enter the 3 sides of a triangle.")
s1 = get_valid_side("Enter a side: ")
s2 = get_valid_side("Enter a side: ")
s3 = get_valid_side("Enter a side: ")
    
colour = input("Enter a colour: ")

while True:
    filled_input = input("Is the triangle filled? Yes (y) or No (n)?\n").lower().strip()
    if filled_input in ['y', 'yes']:
        is_filled = True
        break
    elif filled_input in ['n', 'no']:
        is_filled = False
        break
    else:           
        print("Error: Wrong input!")
        print("Enter either y (Yes) or n (No): ", end="")

triangle = Triangle(side1=s1, side2=s2, side3=s3, colour=colour, filled=is_filled)
    
print("\nTriangle")
print(triangle)