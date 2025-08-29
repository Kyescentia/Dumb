from utils.Rectangle import *
from utils.Geometric import *

rectangles = [
    Rectangle(width=4, height=40, colour="red", filled=False),
    Rectangle(width=3.5, height=35.7, colour="yellow", filled=True)
    ]


for i, rect in enumerate(rectangles, start=1):          
    print(f"Rectangle {i}")
    print(rect)
    print()