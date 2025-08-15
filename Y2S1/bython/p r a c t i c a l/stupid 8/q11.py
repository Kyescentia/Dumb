from customUtils import shuffling, read_capital, STATE_CAPITAL

# Simulate the quiz of guessing the capital cities of different states.
def guess_capitals_quiz():
    keys = shuffling()
    count = 0
    print("Identify the capital of following states:")
    for i in range(len(keys)):
        capital = read_capital(keys[i])
        if capital.lower() == STATE_CAPITAL[keys[i]].lower():
            print("Correct")
            count += 1
        else:
            print("Wrong")
    print("\nYou answered {:d} {:s} correctly!".format(count, "questions" if count > 1 else "question"))


guess_capitals_quiz()