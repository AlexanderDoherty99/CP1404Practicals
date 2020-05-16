"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Old')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    new_name = ""
    reached_extension = False
    for i, char in enumerate(filename):
        try:
            if reached_extension:
                new_name += char.lower()
            elif char == ".":
                new_name += char
                reached_extension = True
            elif char == " ":
                new_name += "_"
            elif char.islower and filename[i-1] == " ":
                new_name += char.upper()
            elif char.isupper and char not in SPECIAL_CHARACTERS and filename[i+1].isupper():
                new_name += "{}_".format(char)
            elif filename[i-1] in SPECIAL_CHARACTERS:
                new_name += char.upper()
            else:
                new_name += char
        except IndexError:
            new_name += char
            break
    return new_name


def demo_walk():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        # for filename in filenames:
        #     new_name = get_fixed_filename(filename)
        #     print("Renaming {} to {}".format(directory_name + filename, new_name))
        #     os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


main()
# demo_walk()

