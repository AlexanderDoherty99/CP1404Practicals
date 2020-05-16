from prac_08.taxi import Taxi


def main():
    taxi1 = Taxi("Prius", 100, 1.23)
    taxi1.drive(40)
    print("Name: {} Fuel: {} Fare: ${}".format(taxi1.name, taxi1.fuel, taxi1.get_fare()))
    taxi1.start_fare()
    taxi1.drive(100)
    print("Name: {} Fuel: {} Fare: ${}".format(taxi1.name, taxi1.fuel, taxi1.get_fare()))

main()