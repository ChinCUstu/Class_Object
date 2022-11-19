def parse_number(telephone_number):
    new_number = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for digits in telephone_number:
        if not digits.isdigit():
            if digits in alphabet[0:3]:
                digits = '2'
            elif digits in alphabet[3:6]:
                digits = '3'
            elif digits in alphabet[6:9]:
                digits = '4'
            elif digits in alphabet[9:12]:
                digits = '5'
            elif digits in alphabet[12:15]:
                digits = '6'
            elif digits in alphabet[15:19]:
                digits = '7'
            elif digits in alphabet[19:22]:
                digits = '8'
            elif digits in alphabet[22:26]:
                digits = '9'
        new_number += digits
    print(new_number)