# match_case_calculator.py

def perform_calculation(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                return num1 / num2
        case _:
            return "Invalid operation."

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ").strip()

        result = perform_calculation(num1, num2, operation)

        if isinstance(result, str):  # Check if the result is an error message
            print(result)
        else:
            print(f"The result is {result:.2f}")  # Format result to 2 decimal places

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
