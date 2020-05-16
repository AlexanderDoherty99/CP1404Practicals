from prac_08.taxi import Taxi
from prac_08.SilverServiceTaxi import SilverServiceTaxi

def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!\n q)uit, c)hoose taxi, d)rive")
    user_input = input(">>>").upper()
    if user_input == "Q":
        exit()
    elif user_input == "C":
        current_taxi == choose_taxi(taxis)
    elif user_input == "D":
        if current_taxi is None:
            print("No Taxi selected!")
        else:
            desired_distance = input("Drive how far? ")
            taxis[current_taxi].drive(desired_distance)
            print("Your {} trip cost you ${}".format(taxis[current_taxi].name, taxis[current_taxi].get_fare()))

def choose_taxi(taxis):
    print("Taxis available:")
    for i in range(len(taxis)):
        print("{} - {}".format(i, taxis[i]))
    return input("Choose taxi: ")

main()