"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():

    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(celsius)))
        elif choice == "F":
            farheneit = float(input("Farheneit: "))
            print("Result: {:.2f} F".format(farheneit_to_celsius(farheneit)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def farheneit_to_celsius(farheneit):
    return (farheneit - 32) * 5 / 9

main()