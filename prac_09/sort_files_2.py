import shutil
import os


def main():
    os.chdir('FilesToSort')
    categories = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename[int(filename.index(".")):]
        if extension not in categories:
            desired_category = input("What category would you like to sort {} files into? ".format(extension[1:]))
            categories[desired_category] = extension
            os.mkdir(desired_category)
        if ".doc" in categories.values():
            print(get_key(extension, categories))
        # shutil.move(filename, '{}/'.format(extension[1:]) + filename)


def get_key(check_value, dictionary):
    for key, value in dictionary.items():
        if check_value == value:
            return key
    return "no key found"

main()
