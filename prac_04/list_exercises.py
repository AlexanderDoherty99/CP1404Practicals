NUMBERS_WANTED = 5
numbers = []

for i in range(NUMBERS_WANTED):
    numbers.append(int(input("Number: ")))
print(numbers)

print("the first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[-1]))
print("the smallest number is {}".format(min(numbers)))
print("the largest number is {}".format(max(numbers)))
print("the average of the numbers is {:.1f}".format(sum(numbers)/len(numbers)))