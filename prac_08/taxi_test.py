from prac_08.taxi import Taxi


def main():
    taxi1 = Taxi("Prius", 100)
    taxi1.drive(40)
    print("Name: {} Fuel: {} Fare: ${} Price per KM: {} Total KM: {}".format
          (taxi1.name, taxi1.fuel, taxi1.get_fare(), taxi1.price_per_km, taxi1.current_fare_distance))
    taxi1.start_fare()
    taxi1.drive(100)
    print("Name: {} Fuel: {} Fare: ${} Price per KM: {} Total KM: {}".format
          (taxi1.name, taxi1.fuel, taxi1.get_fare(), taxi1.price_per_km, taxi1.current_fare_distance))


main()