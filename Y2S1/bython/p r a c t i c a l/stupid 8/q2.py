from customUtils import readstr, is_palindrome

def main():
    text = readstr("Enter a string: ")
    print("'{}' {} a palindrome!".format(text, "is" if is_palindrome(text) else "is not"))


main()