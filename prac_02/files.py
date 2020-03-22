# Q1
out_file = open('name.txt', 'w')
name = str(input("Please input your name: "))
print(name, file=out_file)
out_file.close()

# Q2
in_file = open('name.txt', 'r')
print(in_file.readline())
in_file.close()

# Q3
in_file = open('numbers.txt', 'r')
total = 0
for line in range(2):
    total += int(in_file.readline())
in_file.close()
print(total)
