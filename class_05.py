"""
1. Take Num1 and Num2
2. Take an input asking the user what operation to perform 
3. Check if the selected option exists and carry out the arithemetic oparation
"""

print("Welcome to Codesignature's Calculator!!!")

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("Select an option below:\nA)Addition\nB)Subtraction\nC)Division\nD)Multipiplication")
option = input("==> ").upper()


if option == "A":
    print(f"The Sum of {num1} and {num2} is {num1 + num2}")
elif option == "B":
    print(f"The Diffrence btw {num1} and {num2} is {num1 - num2}")
elif option == "C":
    print(f"The Quotient of {num1} and {num2} is {num1 / num2}")
elif option == "D":
    print(f"The Product of {num1} and {num2} is {num1 * num2}")
else: 
    print(f"Invalid Option {option}")
    