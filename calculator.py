"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_input = input("> ")

    tokens = user_input.split(" ")

    if tokens[0] == "q":
        print("Exiting calculator.")
        break

    operator = tokens[0]
    num1 = tokens[1]

    if len(tokens) == 3:
        num2 = tokens[2]
    elif len(tokens) == 4:
        num3 = tokens[3]

    result = None

    if operator == "+":
        result = add(float(num1), float(num2))
    elif operator == "-":
        result = subtract(float(num1), float(num2))
    elif operator == "*":
        result = multiply(float(num1), float(num2)) 
    elif operator == "/":
        result = divide(float(num1), float(num2))  
    elif operator == "square":
        result = square(float(num1))
    elif operator == "cube":
        result = cube(float(num1))
    elif operator == "pow":
        result = power(float(num1), float(num2))
    elif operator == "mod":
        result = mod(float(num1), float(num2))

    print(result)