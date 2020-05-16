from prac_08.taxi import Taxi
from random import randint


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness