import math

print("Scientist Calculator\n")

while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Quit")

    choice = input("Enter choice (1-11): ")

    if choice == '11':
        break

    num1 = float(input("Enter first number: "))

    if choice != '6' and choice != '7' and choice != '8' and choice != '9' and choice != '10':
        num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print(num1, "+", num2, "=", result)
    elif choice == '2':
        result = num1 - num2
        print(num1, "-", num2, "=", result)
    elif choice == '3':
        result = num1 * num2
        print(num1, "*", num2, "=", result)
    elif choice == '4':
        result = num1 / num2
        print(num1, "/", num2, "=", result)
    elif choice == '5':
        result = math.pow(num1, num2)
        print(num1, "^", num2, "=", result)
    elif choice == '6':
        result = math.sqrt(num1)
        print("sqrt(", num1, ") =", result)
    elif choice == '7':
        result = math.log10(num1)
        print("log10(", num1, ") =", result)
    elif choice == '8':
        result = math.sin(num1)
        print("sin(", num1, ") =", result)
    elif choice == '9':
        result = math.cos(num1)
        print("cos(", num1, ") =", result)
    elif choice == '10':
        result = math.tan(num1)
        print("tan(", num1, ") =", result)
    else:
        print("Invalid input")
