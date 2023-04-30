"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? ans = ValueError occurs when I enter anything except for integers.
2. When will a ZeroDivisionError occur? ans = ZeroDivisionError occours when I try to divide by 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? ans = I used the while loop.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while ZeroDivisionError:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
        if denominator != 0:
            break
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")


print("Finished.")

