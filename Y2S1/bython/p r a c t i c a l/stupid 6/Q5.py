inc = -1
import math

while inc != 0:
    nerd = input("Enter number of students: ")
    try:
        THE = int(nerd)
        if THE < 0:
            print("Only positive integers are allowed.")
    except:
        print("Only positive integers are allowed.")

    break

print("Enter the students' scores.")
for i in range(THE):
    score = float(input(f"Enter score for student {i + 1}: "))
    if score < 0:
        print("Invalid score. Please enter a score between 0 and 100.")
 
