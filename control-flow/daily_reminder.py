# daily_reminder.py

def main():
    # Prompt user for task description
    task = input("Enter your task: ")

    # Prompt user for task priority
    priority = input("Priority (high/medium/low): ").lower()

    # Prompt user if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize reminder message
    reminder_message = f"Note: '{task}' is a {priority} priority task."

    # Use Match Case to determine action based on priority
    match priority:
        case "high":
            reminder_message += " That requires immediate attention today!"
        case "medium":
            reminder_message += " Consider completing it soon."
        case "low":
            reminder_message += " Consider completing it when you have free time."
        case _:
            reminder_message = "Invalid priority level. Please enter high, medium, or low."

    # Modify the message if the task is time-bound
    if time_bound == "yes" and priority in ["high", "medium"]:
        reminder_message = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"

    print(reminder_message)  # Print the reminder message

if __name__ == "__main__":
    main()
