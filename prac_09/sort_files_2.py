import shutil
import os


def main():
    os.chdir('FilesToSort')
    categories = {}
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename[int(filename.index(".")):]
        # If the extension is not categorised, ask user to do so.
        if not get_key(extension, categories) in categories.keys():
            desired_category = input("What category would you like to sort {} files into? ".format(extension[1:]))
            # Checks if category already exists in dictionary
            if desired_category not in categories.keys():
                categories[desired_category] = []
            # Checks if Folder already exists for category
            if not os.path.exists(desired_category):
                os.mkdir(desired_category)
            # Adds extension into category dictionary
            categories[desired_category].append(extension)
        # Find which category the extension belongs in and move it there
        shutil.move(filename, '{}/'.format(get_key(extension,categories)) + filename)


def get_key(check_value, dictionary):
    # Check all value arrays for desired value, if found, return the parent key
    for key, value in dictionary.items():
        if check_value in value:
            return key

main()
