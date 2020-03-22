"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When a non-integer is input (e.g a string or float)
2. When will a ZeroDivisionError occur?
    When the denominator is set as 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Dividing by zero is mathematically impossible, the user is already given an error message
    noting that mathematical impossibility when they attempt it. The error is handled
    and doesn't lead to a crash, no more is needed to be done.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
