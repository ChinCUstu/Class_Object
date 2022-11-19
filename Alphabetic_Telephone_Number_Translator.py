import parse_number


def main():
    telephone_number = input("Enter a 10-character telephone number(XXX-XXX-XXXX): ")
    parse_number.parse_number(telephone_number.upper())


main()
