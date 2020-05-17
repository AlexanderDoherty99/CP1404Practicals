import shutil
import os


def main():
    os.chdir('FilesToSort')
    filetypes = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename[int(filename.index(".")):]


main()
