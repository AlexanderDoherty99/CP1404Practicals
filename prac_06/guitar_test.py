from prac_06.guitar import Guitar


def main():
    Guitar1 = Guitar("Gibson L-5 CES", 1922,  16035.40)
    Guitar2 = Guitar("Another Guitar", 2013, 16035.41)
    print("{} get_age() - Expected 98. Got {}.".format(Guitar1.name, Guitar1.get_age()))
    print("{} get_age() - Expected 7. Got {}.".format(Guitar2.name, Guitar2.get_age()))
    print("{} is_vintage() - Expected True. Got {}.".format(Guitar1.name, Guitar1.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}.".format(Guitar2.name, Guitar2.is_vintage()))


main()
