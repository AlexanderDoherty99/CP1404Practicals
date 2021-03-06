
MIN_LENGTH = 2
MAX_LENGTH = 6

def main():

    password = get_password()
    while not password_checker(password):
        print("Invalid password!")
        main()
    print(string_length_to_character_converter(password))


def get_password():
    print("Please input a password that is between {} and {} characters long".format(MIN_LENGTH, MAX_LENGTH))
    password = input(">>> ")
    return password


def string_length_to_character_converter(string_to_convert):
    converted_string = ""
    for i in range(len(string_to_convert)):
        converted_string += "*"
    return converted_string


def password_checker(password):
    return MIN_LENGTH <= len(password) <= MAX_LENGTH


main()

