# pattern_drawing.py

def draw_pattern(size):
    row = 0  # Initialize row counter
    while row < size:  # Loop for each row
        for _ in range(size):  # Loop for each column
            print("*", end="")  # Print asterisk without newline
        print()  # Move to the next line after each row
        row += 1  # Increment the row counter

def main():
    try:
        size = int(input("Enter the size of the pattern: "))  # Prompt for input
        if size > 0:  # Check if the input is a positive integer
            draw_pattern(size)  # Call the function to draw the pattern
        else:
            print("Please enter a positive integer.")  # Handle non-positive input
    except ValueError:
        print("Invalid input. Please enter a numeric value.")  # Handle non-numeric input

if __name__ == "__main__":
    main()
