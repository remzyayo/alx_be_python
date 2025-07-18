Task = input("Enter your task: Finish your task")
Priority = input("Enter the priority (high, medium, low): ").lower()
TimeBound = input("Is the task time-bound? (yes or no): ").lower()
match priority:
    case "high":
        reminder = f" High Priority: Don't forget to {task}."
    case "medium":
        reminder = f" Medium Priority: Make time to {task}."
    case "low":
        reminder = f" Low Priority: You can do {task} when you have free time."
    case _:
        reminder = f" Unknown Priority: {task} (check the priority spelling)."
if TimeBound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"
print("\n REMINDER")
print(reminder)
         