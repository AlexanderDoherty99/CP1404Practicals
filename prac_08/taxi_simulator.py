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

    elif user_input == "D"
main()