NUMBERS_WANTED = 5
numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username_is_valid = False
while not username_is_valid:
    input_username = input("Username: ")
    if input_username in usernames:
        username_is_valid = True
        break
    print("Invalid username!")

for i in range(NUMBERS_WANTED):
    numbers.append(int(input("Number: ")))
print(numbers)

print("the first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[-1]))
print("the smallest number is {}".format(min(numbers)))
print("the largest number is {}".format(max(numbers)))
print("the average of the numbers is {:.1f}".format(sum(numbers)/len(numbers)))

