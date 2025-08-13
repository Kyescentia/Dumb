import random
randomness = 0
inc = -1
all = []
wrong = 0
right = 0
while inc != 0:
    randomness = random.randint(1, 2)
    print(f"DEBUG: {randomness}")
    thing = int(input("Enter your guess as 1 for Head, 2 for Tail, or 0 to exit: "))
    try:
        if thing == 0:
            print("Thank you for playing the game!")
            inc == 0
            break
        else:
            if thing == randomness:
                print("Correct!")
                right += 1
                all.append(f"{'Head' if randomness == 1 else 'Tail'},{'Head' if thing == 1 else 'Tail'},Correct")
            else:
                print("Wrong!")
                wrong += 1
                all.append(f"{'Head' if randomness == 1 else 'Tail'},{'Head' if thing == 1 else 'Tail'},Wrong")
    except:
        print("Please enter 0, 1, or 2.")

print(f"""
RESULTS
==========================
You have made {right} correct guesses and {wrong} wrong guesses.
""")
count = 1
for m in all:
    print(f"Round #{count}")
    count += 1
    i = m.split(",")
    print(f"""
    Answer: {i[0]}
    Guess: {i[1]}
    Result: {i[2]}
    """)
