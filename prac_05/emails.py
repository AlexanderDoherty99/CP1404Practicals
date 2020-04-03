def main():


    user_input = "temp"
    while not user_input == "":
        user_input = input("Email:")
        user_name = user_input.split("@")[0]
        print("Is your name {}?".format(user_name))

main()