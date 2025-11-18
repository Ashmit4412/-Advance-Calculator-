import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def sqrt(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    else:
        return math.sqrt(x)

def absolute(x):
    return abs(x)

print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Power (x^y)")
print("6. Modulus (%)")
print("7. Square Root (√x)")
print("8. Absolute Value (|x|)")

choice = input("Enter choice (1-8): ")

if choice in ('1', '2', '3', '4', '5', '6'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '6':
        print(f"{num1} % {num2} = {modulus(num1, num2)}")

elif choice == '7':
    num = float(input("Enter the number: "))
    print(f"√{num} = {sqrt(num)}")
elif choice == '8':
    num = float(input("Enter the number: "))
    print(f"|{num}| = {absolute(num)}")
else:
    print("Invalid input")