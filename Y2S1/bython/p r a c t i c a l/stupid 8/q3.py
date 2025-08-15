from customUtils import read_size, read_scores, get_top_two_scores, calculate_average

def main():
    number = read_size()
    scores = read_scores(number)
    first, second = get_top_two_scores(scores)
    print("The highest score     : {:.1f}%".format(first))
    print("The second highest score: {:.1f}%".format(second))
    print("The average score     : {:.1f}%".format(calculate_average(scores)))


main()