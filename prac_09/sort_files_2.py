import shutil
import os


def main():
    os.chdir('FilesToSort')
    filetypes = []
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extension = filename[int(filename.index(".")):]
        if extension not in filetypes:
            filetypes.append(extension)
            os.mkdir(extension[1:])
        shutil.move(filename, '{}/'.format(extension[1:]) + filename)

main()
