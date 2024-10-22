# multiplication_table.py

def print_multiplication_table(number):
    for i in range(1, 11):  # Loop from 1 to 10
        product = number * i
        print(f"{number} * {i} = {product}")

def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))  # Prompt for input
        print_multiplication_table(number)  # Call the function to print the table
    except ValueError:
        print("Invalid input. Please enter a numeric value.")  # Handle non-numeric input

if __name__ == "__main__":
    main()
