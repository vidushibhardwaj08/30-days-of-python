def calculator(operation, num1, num2):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "Invalid operator"

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError: 
    print("Not an integer")
    exit()

try:
    operator= str(input("Enter the operator symbol: "))
except ValueError:
    print("Not a string")
    exit()

result = calculator(operator, num1, num2)
print(result)
