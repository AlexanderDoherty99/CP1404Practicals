from prac_08.SilverServiceTaxi import SilverServiceTaxi


def main():
    taxi2 = SilverServiceTaxi("Prius", 100, 2)
    taxi2.drive(18)
    print(taxi2)
    print("Fare of ${}".format(taxi2.get_fare()))

main()