from prac_06.guitar import Guitar

def main():

    guitars = []
    print("My guitars")
    user_finished = False
    while not user_finished:
        current_guitar = []
        current_guitar.append(str(input("Name:")))
        current_guitar.append(int(input("Year: ")))
        current_guitar.append(float(input("Cost:")))
        guitars.append(current_guitar)
        user_input = input("Add another Guitar? Y/n: ")
        if user_input[0].upper() == "N":
            user_finished = True
main()