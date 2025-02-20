"""
Calculator Program was chosen. Did the work solo. Below are the principles that I followed.  
    - Single Responsibility: EAch operation does have its own dedicated function. 
    - DRY: Code is not repeated. 
    - Document your Code: Functions are well-documented. 
"""
def add(a, b):
    # Return the sum of a and b.
    return a + b

def subtract(a, b):
    # Return the difference between a and b.
    return a - b

def multiply(a, b):
    # Return the product of a and b.
    return a * b

def divide(a, b):
    """
    Return the result of dividing a by b.
    
    Raises:
        ValueError: If b is zero to avoid division by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    # Main function to execute calculator operations.
    print("Kc's Simple Calculator")
    
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Choices
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter choice (1/2/3/4): ")
    
    if operation == '1':
        result = add(num1, num2)
        op_name = "addition"
    elif operation == '2':
        result = subtract(num1, num2)
        op_name = "subtraction"
    elif operation == '3':
        result = multiply(num1, num2)
        op_name = "multiplication"
    elif operation == '4':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            return
        op_name = "division"
    else:
        print("Invalid operation selected.")
        return

    print(f"The result of the {op_name} is: {result}")

if __name__ == "__main__":
    main()
