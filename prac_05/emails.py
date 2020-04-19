def main():

    emails_dict = {}
    email = "temp"
    while not email == "":
        email = input("Email:")
        username = email.split("@")[0]
        user_name = username.replace(".", " ").title()
        if not user_name == "":
            correct_name_checker = input("Is your name {}? (Y/n)".format(user_name))
            if correct_name_checker[0].upper() == "N":
                user_name = input("Name: ")
            emails_dict[user_name] = email
    for key in emails_dict:
        print("{} ({})".format(key, emails_dict[key]))


main()