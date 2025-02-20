# This is a bad calculator implementation that intentionally violates coding best practices.
# It violates the single responsibility principle, repeats code unnecessarily, and has poor documentation.

def calc():
    print("Calculator")
    # Taking input without validation or error checking
    n1 = input("Enter first number: ")
    n2 = input("Enter second number: ")
    op = input("Choose operation (+, -, *, /): ")
    
    # The same conversion is repeated in each branch (violating DRY)
    if op == "+":
        result = float(n1) + float(n2)
        print("Result is: " + str(result))
    elif op == "-":
        result = float(n1) - float(n2)
        print("Result is: " + str(result))
    elif op == "*":
        result = float(n1) * float(n2)
        print("Result is: " + str(result))
    elif op == "/":
        # Doesn't check for whether code is divisble by 0
        result = float(n1) / float(n2)
        print("Result is: " + str(result))
    else:
        print("Invalid operator")
    
    # No clear separation of concerns or proper error handling

calc()
