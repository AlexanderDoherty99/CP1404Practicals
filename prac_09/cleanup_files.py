"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(directory_name + filename, new_name))
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


def get_fixed_filename(filename):
    new_name = ""
    reached_extension = False
    for i, char in enumerate(filename):
        try:
            if reached_extension:
                new_name += char.lower()
            elif char == "." and filename[i+1].upper() == "T":
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


main()

