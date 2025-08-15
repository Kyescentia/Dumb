from customUtils import read_score, get_grade, get_article

def main():
    while True:
        score = read_score()
        grade = get_grade(score)
        print("You got {} {} for the test!".format(get_article(grade), grade))
        while True:
            repeat = input("Continue? (Y/N): ").lower()
            if repeat == 'n':
                print("Thank you!")
                return
            elif repeat == 'y':
                break
            else:
                print("Wrong input!")

main()