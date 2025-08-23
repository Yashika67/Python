# Weekly Planner App
# Dictionary to store tasks for each day
weekly_tasks = {
"Monday": [],"Tuesday": [],"Wednesday": [],"Thursday": [],"Friday": [],"Saturday": [],"Sunday": []
}

# Function to display tasks
def tasks(day):
    if weekly_tasks[day]:
        print(f"\nTasks for {day}:")
        for i, task in enumerate(weekly_tasks[day], 1):
            print(f"{i}. {task}")
    else:
        print(f"\nNo tasks for {day}.")

# Main App Loop
while True:
    print("\n--- Weekly Planner ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == '1':
        day = input("Enter the day of the week: ").capitalize()
        if day in weekly_tasks:
            task = input("Enter your task: ")
            weekly_tasks[day].append(task)
            print(f"Task added to {day}!")
        else:
            print("Invalid day. Please enter a correct day (e.g., Monday).")

    elif choice == '2':
        day = input("Enter the day you want to view tasks for: ").capitalize()
        if day in weekly_tasks:
            tasks(day)
        else:
            print("Invalid day. Please enter a correct day.")

    elif choice == '3':
        print("Exiting Weekly Planner. Have a productive week!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
