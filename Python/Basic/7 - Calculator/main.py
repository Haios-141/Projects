from art import logo
from os import system, name


def clear():
    # for windows
    if name == "nt":
        _ = system("cls")
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


#Add Function
def add(n1, n2):
    return n1 + n2


#Subtract Function
def subtract(n1, n2):
    return n1 - n2


#Multiply Function
def multiply(n1, n2):
    return n1 * n2


#Divide Function
def divide(n1, n2):
    if n2 == 0:
        return "Undefined. Division by 0"
    else:
        return n1 / n2


def verify_symbol(prompt):
    operation_symbol = input(prompt)
    while operation_symbol != "+" and operation_symbol != "-" and \
    operation_symbol != "*" and operation_symbol != "/":
        operation_symbol = input(prompt)

    return operation_symbol


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    # calculator logo
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        prompt = "Pick an operation: "
        operation_symbol = verify_symbol(prompt)
        
        num2 = float(input("What's the next number?: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if answer == "Undefined. Division by 0":
            break;
        
        repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        while repeat != "y" and repeat != "n":
            repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    
        if repeat == "n":
            should_continue = False
            clear()
            calculator()
        else:
            num1 = answer

calculator()