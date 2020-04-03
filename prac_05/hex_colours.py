"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

def main():

    COLOUR_TO_CODE = {"blue1": "0000ff", "brown1": "ff4040", "chocolate": "d2691e", "coral": "ff7f60",
                      "cyan1": "00ffff", "darkgreen": "007400", "darkorange": "ff8c00", "darkviolet": "9400d3",
                      "gold1": "ffd700", "gray": "bebebe", "green1": "00ff00"}
    print(COLOUR_TO_CODE)

    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        if colour_name in COLOUR_TO_CODE:
            print(colour_name, "is", COLOUR_TO_CODE[colour_name])
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()

