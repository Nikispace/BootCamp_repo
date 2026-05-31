# Simple calculator program using Python

def add(a, b):
    # This function returns the sum of two numbers
    return a + b

def subtract(a, b):
    # This function returns the difference between two numbers
    return a - b

def multiply(a, b):
    # This function returns the product of two numbers
    return a * b

def divide(a, b):
    # This function returns the division result of two numbers and handles division by zero
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

if __name__ == "__main__":
    print("Welcome to the Simple Calculator!")
    print("Choose an operation: +, -, *, /")
    op = input("Enter operation: ")
    
    # Take number inputs from the user and convert them to float for decimal support
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operation selected."

    print("Result:", result)

    # Built with love with the help of CipherSchools