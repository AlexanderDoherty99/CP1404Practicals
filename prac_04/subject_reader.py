"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data_arrays = get_data()
    print(data_arrays)
    for data in range(len(data_arrays)):
        print("{} is taught be {:<12} and has {:>3} students".format(data_arrays[data][0], data_arrays[data][1], data_arrays[data][2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_arrays = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data_arrays.append(parts)
        print("----------")
    input_file.close()
    return data_arrays


main()