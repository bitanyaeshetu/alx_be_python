from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()  # Get the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """Calculates and displays the future date based on user input."""
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days)  # Calculate future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    display_current_datetime()  # Display current date and time
    calculate_future_date()  # Calculate and display future date

if __name__ == "__main__":
    main()
