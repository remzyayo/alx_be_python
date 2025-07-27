# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    # Format and display in a readable format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    try:
        # Prompt user for number of days
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        # Calculate future date
        future_date = datetime.now() + timedelta(days=number_of_days)
        # Format and display future date
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter a valid integer for number of days.")

# Run the functions
if display_current_datetime == "_main_":
    display_current_datetime()
    calculate_future_date()