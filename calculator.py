"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("> ")

    tokens = user_input.split(" ")

    if tokens[0] == "q":
        print("Exiting calculator.")
        break
    elif len(tokens) < 2:
        print("Please provide enough inputs.")
        continue

    operator = tokens[0]
    num1 = tokens[1]

    # If there are three tokens, then the second number should be the last token
    if len(tokens) == 3:
        num2 = tokens[2]

    # Try except block here to handle scenario where user inputs too few numbers for a given operator
    try:
        # Check to make sure numbers inputted are valid numeric strings
        if not num1.isdigit() or not num2.isdigit():
            print("Please enter numbers after the operator.")
            continue

        # We need a variable to store the result returned from each math function
        result = None

        # Check each operator
        # For each math function call, we need to cast each number string to a float
        # in order to return results of type float
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
        else:
            print("Please input a valid operator.")

        print(result)

    except NameError:
        print("Please provide the appropriate length of numbers for each operator.")