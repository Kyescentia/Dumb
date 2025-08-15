"""
GLOBAL UTILS
"""
import random
from configs import *

def readstr(prompt):
    return input(prompt.strip())

def count_words(input_string):
    return len(input_string.split())

"""
QUESTION 1 UTILS
"""

# Return the number of vowels in the input_string.
def count_vowels(input_string):
    return len([character for character in input_string if character.lower() in ['a', 'e','i', 'o', 'u']])

# Return the number of vowel 'a', 'e', 'i', 'o' and 'u' separately.
def count_vowel_aeiou(input_string):
    input_string = input_string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']

    a = input_string.count("a")
    e = input_string.count("e")
    i = input_string.count("i")
    o = input_string.count("o")
    u = input_string.count("u")
    frequency = [a, e, i, o, u]

    return dict(zip(vowels, frequency))

"""
QUESTION 2 UTILS
"""

# Return the average of word length in the input_string.
def calculate_average_word_length(input_string):
    total = 0
    for token in input_string.split():
        total += len(token)
    return (total / len(input_string.split()))

# Remove irrelevant contents from the input_string.
def remove_noise(input_string):
    return "".join([letter if letter.isalpha() else "" for letter in input_string])


# Convert all elements in the input_string to a consistent case.
def normalize_case(input_string):
    return input_string.lower()


# Return true if the input_string is a palindrome.
def is_palindrome(input_string):
    input_string = normalize_case(remove_noise(input_string))
    return input_string == input_string[::-1]

"""
QUESTION 3 UTILS
"""

# Remove the number of students from user input.
def read_size():
    while True:
        number = input("Enter the number of students: ")
        if number.isdigit():
            number = int(number)
            if number > 0 and number <= 10**10:
                return number
            else:
                print("Error: Only positive integer is allowed!\n")
        else:
            print("Error: Only integer is allowed!\n")


# Read a list of scores from user input.
def read_scores(loop):
    floats = []
    count = 0
    while True:
        try:
            number = input("Enter a score: ")
            number = float(number)
            if number >= 0 and number <= float('inf'):
                floats.append(number)
                count += 1
                if count == loop:
                    return floats
            else:
                print("Error: Only positive value or 0 is allowed!\n")
        except ValueError:
            print("Error: Only floating-point number is allowed!\n")


# Return the highest and the second highest scores from a list of scores.
def get_top_two_scores(scores):
    scores.sort(reverse=True)
    return scores[:2]


# Return the average of all scores contained in a list of scores.
def calculate_average(scores):
    return sum(scores) / len(scores)


# Return the appropriate ordinal suffix for a given number.
def get_ordinal_suffix(number):
    if number >= 11 and number <= 13:
        return "th"
    else:
        match (number % 10):
            case 1:
                return "st"
            case 2:
                return "nd"
            case 3:
                return "rd"
            case _:
                return "th"
            
"""
QUESTION 4 UTILS
"""

# Return a lists of integers from user input.
def read_inputs():
    integers = []
    count = 0
    while True:
        integer = input("Enter an integer or 0 to exit: ")
        if integer.lower() == '0':
            return integers
        try:
            integers.append(int(integer))
        except ValueError:
            print("Error: Only integer is allowed!\n")


# Return the sum of all numbers
def calculate_sum(numbers):
    return sum(numbers)


# Return the average of all numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


# Return the number of positive and negative numbers
def count_positive_negative(numbers):
    pos, neg = 0, 0
    for number in numbers:
        if number > 0:
            pos += 1
        else:
            neg += 1
    return (pos, neg)


# Print the number of positive and negative numbers, and the sum and average of all number
def print_summary(numbers):
    pos, neg = count_positive_negative(numbers)
    print("No. of positive numbers: {:d}".format(pos))
    print("No. of negative numbers: {:d}".format(neg))
    print("Sum of all numbers      : {:d}".format(calculate_sum(numbers)))
    print("Average of all numbers  : {:.2f}".format(calculate_average(numbers)))

"""
QUESTION 5 UTILS
"""


# Return a saving amount from user input.
def read_base():
    while True:
        try:
            base = float(input("Enter the base amount: "))
            if base <= 0:
                print("Error: Only positive number greater than 0 is allowed!\n")
            else:
                return base
        except:
            print("Error: Only number is allowed!\n")

# Return the number of months from user input.
def read_month():
    while True:
        month = input("Enter the no. of months: ")
        if month.isdigit():
            month = int(month)
            if month <= 0:
                print("Error: Only positive integer greater than 0 is allowed!\n")
            else:
                return month
        else:
            print("Error: Only positive integer is allowed!\n")

# Return the amount of monthly saving.
def calculate_monthly_saving(base, total, monthlyrate):
    return (base + total) * (1 + monthlyrate)

# Return the appropriate ordinal suffix for a given number.
def get_ordinal_suffix(number):
    if number >= 11 and number <= 13:
        return str(number) + "th"
    else:
        match (number % 10):
            case 1:
                return str(number) + "st"
            case 2:
                return str(number) + "nd"
            case 3:
                return str(number) + "rd"
            case _:
                return str(number) + "th"

# Print the amount of monthly saving for quantity number of months.
def print_monthly_savings(base, quantity, monthly):
    print("\n{:<12s}{:>12s}".format("Month", "Total"))
    total = 0.
    for count in range(1, quantity + 1):
        total = calculate_monthly_saving(base, total, monthly)
        print("{:<12s}{:>10.2f}".format(get_ordinal_suffix(count), total))

"""
QUESTION 6 UTILS
"""
from configs import *

# Return the amount of working hours from user input
def read_work_hours():
    while True:
        try:
            number = float(input("Enter working hours: "))
            if number <= 0:
                print("Error: Only positive number is allowed!\n")
            else:
                return number
        except:
            print("Error: Only number is allowed!\n")

# Return the amount of total wage.
def calculate_total_wage(hours):
    return calculate_regular_pay(hours) + calculate_OT_pay(hours)

# Return the amount of regular pay.
def calculate_regular_pay(hours):
    if hours <= HOURLY_RATE_LIMIT:
        return hours * HOURLY_RATE
    else:
        return HOURLY_RATE_LIMIT * HOURLY_RATE

# Return the total amount of OT.
def calculate_OT_pay(hours):
    return calculate_regular_OT_pay(hours) + calculate_excess_OT_pay(hours)

# Return the amount of regular OT.
def calculate_regular_OT_pay(hours):
    if hours <= HOURLY_RATE_LIMIT:
        return 0
    elif hours <= (HOURLY_RATE_LIMIT + REGULAR_RATE_LIMIT):
        return (hours - HOURLY_RATE_LIMIT) * OT_REGULAR_RATE
    else:
        return REGULAR_RATE_LIMIT * OT_REGULAR_RATE

# Return the amount of excessive OT.
def calculate_excess_OT_pay(hours):
    if hours <= (HOURLY_RATE_LIMIT + REGULAR_RATE_LIMIT):
        return 0
    else:
        return (hours - HOURLY_RATE_LIMIT - REGULAR_RATE_LIMIT) * OT_EXCESS_RATE
"""
QUESTION 7 UTILS
"""
# Return a score from user input.
def read_score():
    while True:
        try:
            score = float(input("Enter a score: "))
            if score < 0 or score > 100:
                print("Error: Invalid score!\n")
            else:
                return score
        except:
            print("Error: Only number is allowed!\n")


# Return the appropriate article for a given grade.
def get_article(grade):
    match grade:
        case 'A' | 'F':
            return "an"
        case 'B' | 'C' | 'D':
            return "a"


# Return a grade based on the provided score.
def get_grade(score):
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

"""
QUESTION 8 UTILS
"""
# Return a lists of integers from user input.
def read_inputs():
    integers = []
    count = 0

    while True:
        integer = input("Enter an integer or 'q' to exit: ")
        if integer.lower() == 'q':
            return integers

        try:
            integers.append(int(integer))
        except ValueError:
            print("Error: Only integer is allowed!\n")


# Return a reversed version of a list of numbers.
def reverse(numbers):
    return numbers[::-1]


# Print a list of numbers in the same line.
def print_numbers(numbers):
    for num in numbers:
        print(num, end=" ")

"""
QUESTION 9 UTILS
"""

# Read the first 9 digits of an ISBN-10 number from user input.
def read_isbn9():
    while True:
        number = input("Enter the first 9 digits of an ISBN-10: ").strip()
        if number.isdigit() and len(number) == 9:
            return int(number)
        else:
            print("Error: Only positive 9-digits integer are allowed!\n")


# Return the checksum of 9 digits of the ISBN-10 number.
def calculate_checksum(number):
    checksum = 0
    counter = 9
    while counter != 0:
        checksum += ((number % 10) * counter)
        counter -= 1
        number = number // 10
    return checksum % 11


# Print the complete ISBN-10 number.
def print_isbn10(number, checksum):
    print("The ISBN-10 number is:", str(number) + (str(checksum) if checksum != 10 else "X"))

"""
QUESTION 10 UTILS
"""

answers = []
guesses = []
results = []

# Return a random number to simulate heads and tails.
def generate_random_number():
    return random.randint(1, 2)

# Return a guess as a number from user input.
def read_guess():
    while True:
        number = input("Enter 1 for a head, 2 for a tail, or 0 to exit: ")
        if number.isdigit():
            number = int(number)
            if number >= 0 and number <= 2:
                return number
            else:
                print("Error: Only 0, 1 and 2 are allowed!\n")
        else:
            print("Error: Only 0, 1 and 2 are allowed!\n")

# Return True to indicate a correct guess, otherwise, return False
def win_or_lose(answer, guess):
    if answer == guess:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

# Record the details of a single game round.
def record_game(answer, guess, result):
    answers.append(answer)
    guesses.append(guess)
    results.append(result)

# Return the total number of correct guesses.
def count_correct():
    return len([result for result in results if result])

# Return the total number of incorrect guesses.
def count_incorrect():
    return len([result for result in results if not result])

# Print the details of all game rounds
def print_records():
    print("\n---")
    print("RESULTS")
    print("---")
    print("You have made {:d} correct guess{}.".format(count_correct(), "es" if count_correct() > 1 else ""))
    print("and {:d} incorrect guess{}.".format(count_incorrect(), "es" if count_incorrect() > 1 else ""))

    for i in range(len(answers)):
        print("\nRound #{:d}".format(i + 1))
        print("Answer: {:s}".format("Head" if answers[i] == 1 else "Tail"))
        print("Guess : {:s}".format("Head" if guesses[i] == 1 else "Tail"))
        print("Result: {:s}".format("Correct" if results[i] else "Wrong"))

"""
QUESTION 11 UTILS
"""

from configs import STATE_CAPITAL

# Return a shuffled list of dictionary's keys.
def shuffling():
    keys = list(STATE_CAPITAL.keys())
    random.shuffle(keys)
    return keys

# Return a capital from user input.
def read_capital(state):
    return input("\nEnter the capital of {:16}: ".format(state)).strip()
