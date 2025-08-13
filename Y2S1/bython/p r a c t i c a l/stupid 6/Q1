inc = -1
while inc != 0:
    thein = input("Enter a score or 'Q'/'q' to exit: ")
    if thein.lower() == 'q':
        print("Thank you!")
        inc == 0
        break
    
    try:
        score = float(thein)

        if score >= 0 and score <= 100:
            if score <= 100:
                yes = 'A'
            if score <= 89:
                yes = 'B'
            if score <= 79:
                yes = 'C'
            if score <= 69:
                yes = 'D'
            if score < 60:
                yes = 'F'

            match yes:
                case 'A' | 'F':
                    grammar = 'an'
                case _:
                    grammar = 'a'
                    
            print(f"You got {grammar} {yes} for the test!")
        else:
            print("Invalid input. Please enter a score between 0 and 100.")
    except:
        print("Invalid input. Please enter a numeric score or 'Q'/'q' to exit.")
    
    
