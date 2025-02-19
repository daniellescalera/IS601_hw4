"""This module runs the interactive calculator program."""
from calculator.history import History
from calculator.operations import Operations
from calculator.calculations import Calculation

def main():
    #calculator program that supports decimal and whole numbers
    while True:
        print("\n🔢 Simple Calculator 🔢")
        print("Enter two numbers first, then choose an operation.")
        print("Type 'exit' at any time to quit.")

        # Get user input for numbers first (allow "exit" to quit)
        num1_input = input("Enter the first number: ").strip().lower()
        if num1_input == "exit":
            print("Goodbye! 👋")
            break  # Exit the loop

        num2_input = input("Enter the second number: ").strip().lower()
        if num2_input == "exit":
            print("Goodbye! 👋")
            break

        # Get user input for operation
        print("\nChoose an operation: add, subtract, multiply, divide, history")
        operation = input("Enter operation: ").strip().lower()

        if operation == "exit":
            print("Goodbye! 👋")
            break

        if operation == "history":
            last_calc = History.get_last_calculation()
            if last_calc:
                print(f"📜 Last Calculation: {last_calc}")
            else:
                print("📜 No calculations in history yet.")
            continue  # Restart loop to ask for numbers again

        if operation not in ["add", "subtract", "multiply", "divide"]:
            print(f"❌ Unknown operation: {operation}")  # Handle unknown operations
            continue

        # Try converting numbers to float AFTER the operation is entered
        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print(f"❌ Invalid number input: {num1_input} or {num2_input} is not a valid number.")
            continue  # Restart loop

        # Perform the selected operation
        try:
            if operation == "add":
                result = Operations.add(num1, num2)
            elif operation == "subtract":
                result = Operations.subtract(num1, num2)
            elif operation == "multiply":
                result = Operations.multiply(num1, num2)
            elif operation == "divide":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero") #divide by zero is not allowed
                result = Operations.divide(num1, num2)

            # Create a Calculation instance and add it to history
            calculation = Calculation(num1, num2, operation, result)  # Correct for how we want to input our numbers
            History.add_calculation(num1, num2, operation, result)

            print(f"✅ Result: {num1} {operation} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
