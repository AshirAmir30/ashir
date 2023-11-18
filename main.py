import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y


def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number"
    return math.sqrt(x)


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'sin' for sine")
    print("Enter 'cos' for cosine")
    print("Enter 'tan' for tangent")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ["sin", "cos", "tan"]:
        angle = float(input("Enter angle in degrees: "))
        if user_input == "sin":
            print("Result:", sine(angle))
        elif user_input == "cos":
            print("Result:", cosine(angle))
        elif user_input == "tan":
            print("Result:", tangent(angle))
    elif user_input in ["add", "subtract", "multiply", "divide", "sqrt"]:
        num1 = float(input("Enter first number: "))
        if user_input != "sqrt":
            num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result:", add(num1, num2))
        elif user_input == "subtract":
            print("Result:", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result:", multiply(num1, num2))
        elif user_input == "divide":
            print("Result:", divide(num1, num2))
        elif user_input == "sqrt":
            print("Result:", square_root(num1))
    else:
        print("Unknown input. Please try again.")





