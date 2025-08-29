from utils.Circle import *

circles = [
    Circle(radius=4.5),
    Circle(radius=7.7)
]

for i, circ in enumerate(circles, start=1):
    print(f"Circle {i}")
    print(circ)
    print()