'''
Hi my name is Abayomi and here is my interpitation of the calculator app


'''
print ('Hello World')
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

result = None  # Initialize the result variable

while True:
    # Display the menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exit' to end the program")

    user_input = input(": ")

    if user_input == "exit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        if result is not None:
            num1 = result
        else:
            num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            result = add(num1, num2)
        elif user_input == "subtract":
            result = subtract(num1, num2)
        elif user_input == "multiply":
            result = multiply(num1, num2)
        elif user_input == "divide":
            result = divide(num1, num2)
        
        print("Result: ", result)
        
        # Ask if the user wants to perform more calculations
        more_calculations = input("Do you want to perform more calculations with this result? (yes/no): ")
        if more_calculations.lower() != "yes":
            result = None  # Reset the result if the user doesn't want to continue
    else:
        print("Invalid input. Please enter a valid operation.")
