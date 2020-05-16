from prac_08.SilverServiceTaxi import SilverServiceTaxi


def main():
    taxi2 = SilverServiceTaxi("Prius", 100, 2)
    taxi2.drive(40)
    print("Name: {}, Fuel: {}, Fare: ${}, Price per KM: {}, Total KM: {},".format
          (taxi2.name, taxi2.fuel, taxi2.get_fare(), taxi2.price_per_km, taxi2.current_fare_distance))
    taxi2.start_fare()
    taxi2.drive(100)
    print("Name: {}, Fuel: {}, Fare: ${}, Price per KM: {}, Total KM: {},".format
          (taxi2.name, taxi2.fuel, taxi2.get_fare(), taxi2.price_per_km, taxi2.current_fare_distance))

main()