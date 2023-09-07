# Calculator
from art import calc

print("CALCULATOR")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(calc)
    num1 = float(input("Put in the first number: "))
    should_continue = True

    while should_continue:
        operator = input("Which Operation to carry out: '+', '-', '*', '/': ")
        num2 = float(input("Put in the next number: "))
        calculation = operations[operator]
        answer = calculation(num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")
        continue_or_exit = input(
            f"Type 'Y' to continue calculating with {answer}, type 'N' to stop and type any other thing to start a new calculation: "
        )
        if continue_or_exit.lower() == "n":
            should_continue = False
        elif continue_or_exit.lower() == "y":
            num1 = answer
        else:
            calculator()


calculator()
