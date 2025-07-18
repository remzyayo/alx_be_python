Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
TimeBound = input("Is it time-bound? (yes/no): ").lower()
match Priority:
    case "high":
        reminder = f" High Priority: Don't forget to {Task}."
    case "medium":
        reminder = f" Medium Priority: Make time to {Task}."
    case "low":
        reminder = f" Low Priority: You can do {Task} when you have free time."
    case _:
        reminder = f" Unknown Priority: {Task} (check the priority spelling)."
if TimeBound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"
print("\n REMINDER")
print(reminder)
