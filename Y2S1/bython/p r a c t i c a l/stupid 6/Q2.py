a = []

b = -1
while b != 0:
    c = input("Enter an integer or the 'Q'/'q' to exit: ")
    if c.lower() == 'q':
        print("Thank you!")
        b == 0
        break

    try:
        a.append(int(c))
    except ValueError:
        print("Invalid input. Please enter an integer or 'Q'/'q' to exit.")


print(f"Integers in reversed order: {a[::-1]}")
