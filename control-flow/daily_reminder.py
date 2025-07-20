Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match Priority:
    case "high":
        Customized_Reminder = f" High Priority: Don't forget to {Task}."
        print("reminder")
    case "medium":
        Customized_Reminder = f" Medium Priority: Make time to {Task}."
    case "low":
        Customized_Reminder = f" Low Priority: You can do {Task} when you have free time."
    case _:
        Customized_Reminder = f" Unknown Priority: {Task} (check the priority spelling)."
if time_bound == "yes":
    Customized_Reminder += " This is a time-sensitive task that requires immediate attention today!"
print("\n Reminder: {Customized_Reminder}")
print(Reminder)
