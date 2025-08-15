from customUtils import readstr, count_words, count_vowel_aeiou, calculate_average_word_length

# Return the number of words in the input_string.

def main():
    text = readstr("Enter a string: ")

    # Count the number of words
    print("\nNo. of words: ", count_words(text))


    # Calculate the average word length
    print("\nAverage word length: {:.2f}".format(calculate_average_word_length(text)))


    # Count the number of each of the vowels (a, e, i, o, u) separately
    for vowel, frequency in count_vowel_aeiou(text).items():
        print("\nNo. of {}: {}".format(vowel, frequency))


main()