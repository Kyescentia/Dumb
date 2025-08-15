from customUtils import read_isbn9, calculate_checksum, print_isbn10

def main():
    number = read_isbn9()
    checksum = calculate_checksum(number)
    print_isbn10(number, checksum)


main()