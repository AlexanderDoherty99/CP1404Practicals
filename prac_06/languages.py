

from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages = [ruby, python, visual_basic]

    list_dynamic(languages)


def list_dynamic(languages):
    print("The dynamically typed languages are:")
    for row in languages:
        if row.is_dynamic():
            print(row.name)


main()

