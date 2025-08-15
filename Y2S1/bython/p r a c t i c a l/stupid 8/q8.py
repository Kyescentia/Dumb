from customUtils import read_inputs, reverse, print_numbers

def main():
    numbers = reverse(read_inputs())
    print("\nIntegers in reversed order:", end=" ")
    print_numbers(numbers)


main()