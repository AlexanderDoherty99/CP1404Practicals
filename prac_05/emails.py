def main():


    user_input = "temp"
    while not user_input == "":
        user_input = input("Email:")
        username = user_input.split("@")[0]
        user_name = username.replace(".", " ").title()
        print("Is your name {}?".format(user_name))

main()