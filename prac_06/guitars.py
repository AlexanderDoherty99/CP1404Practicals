from prac_06.guitar import Guitar

def main():

    guitars = []
    print("My guitars")
    # user_finished = False
    # while not user_finished:
    #     current_guitar = []
    #     current_guitar.append(str(input("Name:")))
    #     current_guitar.append(int(input("Year: ")))
    #     current_guitar.append(float(input("Cost:")))
    #     guitars.append(Guitar(current_guitar[0], current_guitar[1], current_guitar[2]))
    #     user_input = input("Add another Guitar? Y/n: ")
    #     if user_input[0].upper() == "N":
    #         user_finished = True
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    i = 0
    for guitar in guitars:
        vintage_string = " (vintage)" if guitar.is_vintage() >= True else ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
        i += 1

main()
