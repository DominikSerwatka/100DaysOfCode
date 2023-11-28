#Calculator
from art import logo
from clear import clear
# Add
def add(n1, n2):
    return n1+n2

# Subtract
def sub(n1, n2):
    return n1-n2

# Multiply
def multi(n1, n2):
    return n1*n2

# Divide
def div(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div,
}


def calculator():
    print(logo)
    num1 = int(input("What's the first number?: "))
    for oper in operations:
        print(oper)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))
    answer1 = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer1}")
    run = False
    check = input(f"Type 'y' to continue calculating with {answer1},  or type 'n' to start new calculation, or type 'exit' to stop calculation: ")
    if check == "y":
        run = True
    elif check == "n":
        clear()
        calculator()
    else:
        run = False

    while run:
        
        operation_symbol = input("Pick another operation from the line above: ")
        num3 = int(input("What's the next number?: "))
        answer2 = operations[operation_symbol](answer1, num3)
        print(f"{answer1} {operation_symbol} {num3} = {answer2}")
        answer1 = answer2
        check = input(f"Type 'y' to continue calculating with {answer1}, or type 'n' to start new calculation, or type 'exit' to stop calculation: ")
        if check == "y":
            run = True
        elif check == "n":
            clear()
            calculator()
        else:
            run = False

calculator()