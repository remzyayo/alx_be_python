Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match Priority:
    case "high":
        Reminder = (f"High Priority: Don't forget to {Task}.")
        print("reminder")
    case "medium":
        Reminder = (f"Medium Priority: Make time to {Task}.")
    case "low":
        Reminder = (f"Low Priority: You can do {Task} when you have free time.")
    case _:
        Reminder = (f"Unknown Priority: {Task} (check the priority spelling).")
if time_bound == "yes":
<<<<<<< HEAD
    Reminder += " This is a time-sensitive task that requires immediate attention today!"
print(f"\n Reminder: ")
=======
        Reminder += (f"This is a time-sensitive task that requires immediate attention today!")
print(f"Reminder: {Reminder}")
>>>>>>> 8fa96cacb9cf7e6ae5053fcdf770e8e4af74a04f
print(Reminder)
