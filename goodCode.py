"""
Simple Calculator Program
------------------------
This module provides basic arithmetic operations with proper error handling.
Demonstrates: KISS, Single Responsibility, DRY, and Documentation principles.
"""


def get_number_input(prompt):
    """
    Safely get a numeric input from the user.

    Args:
        prompt (str): The message to display when asking for input

    Returns:
        float: The validated number entered by the user

    Example:
        >>> num = get_number_input("Enter a number: ")
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_operation_choice():
    """
    Display operation menu and get user's choice.

    Returns:
        str: The selected operation symbol (+, -, *, /)
    """
    print("\nAvailable operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    valid_operations = {'1': '+', '2': '-', '3': '*', '4': '/'}

    while True:
        choice = input("Select operation (1-4): ")
        if choice in valid_operations:
            return valid_operations[choice]
        print("Invalid choice! Please select 1, 2, 3, or 4.")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Return the quotient of two numbers.

    Raises:
        ZeroDivisionError: If attempting to divide by zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return a / b


def perform_calculation(a, b, operation):
    """
    Execute the requested arithmetic operation.

    Args:
        a (float): First number
        b (float): Second number
        operation (str): Operation symbol (+, -, *, /)

    Returns:
        float or str: Result of calculation or error message
    """
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    try:
        result = operations[operation](a, b)
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except KeyError:
        return "Error: Invalid operation"


def display_result(a, b, operation, result):
    """
    Display the calculation result in a formatted way.

    Args:
        a (float): First number
        b (float): Second number
        operation (str): Operation performed
        result (float/str): Result or error message
    """
    print(f"\n{'=' * 40}")
    if isinstance(result, (int, float)):
        print(f"{a} {operation} {b} = {result}")
    else:
        print(result)
    print(f"{'=' * 40}\n")


def calculator():
    """
    Main calculator function that orchestrates the program flow.

    This function handles the main loop of the calculator program,
    allowing users to perform multiple calculations until they
    choose to exit.
    """
    print("Welcome to the Simple Calculator!")
    print("=" * 40)

    while True:
        # Get user input
        num1 = get_number_input("\nEnter first number: ")
        num2 = get_number_input("Enter second number: ")
        operation = get_operation_choice()

        # Perform calculation
        result = perform_calculation(num1, num2, operation)

        # Display result
        display_result(num1, num2, operation, result)

        # Ask to continue
        again = input("Do another calculation? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            break

    print("\nThank you for using the calculator. Goodbye!")


if __name__ == "__main__":
    calculator()