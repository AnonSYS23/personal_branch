def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Welcome to the calculator!")

while True:
    operation = input("Enter an operation (+, -, *, /): ")
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation. Please try again.")
        continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)

    print(f"{num1} {operation} {num2} = {result}\n")

    another_operation = input("Do you want to perform another operation? (y/n): ")
    if another_operation.lower() == "n":
        print("Thanks for using the calculator!")
        break
