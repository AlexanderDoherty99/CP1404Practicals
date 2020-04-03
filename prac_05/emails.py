def main():

    emails_dict = {}
    email = "temp"
    while not email == "":
        email = input("Email:")
        username = email.split("@")[0]
        user_name = username.replace(".", " ").title()
        correct_name_checker = input("Is your name {}? (Y/n)".format(user_name))
        if correct_name_checker[0].upper() == "N"
            user_name = input("Name: ")
        emails_dict[user_name] = email


main()