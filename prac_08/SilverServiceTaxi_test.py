from prac_08.SilverServiceTaxi import SilverServiceTaxi


def main():
    taxi2 = SilverServiceTaxi("Prius", 100, 2)
    taxi2.drive(40)
    print(taxi2)
    taxi2.start_fare()
    taxi2.drive(100)
    print(taxi2)
main()