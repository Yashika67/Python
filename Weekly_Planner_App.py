import random
# Daily motivational quotes
quotes = [
    "Stay focused and never give up!",
    "Small steps every day lead to big results.",
    "Dream it. Wish it. Do it.",
    "Discipline is the bridge between goals and success.",
    "Be the energy you want to attract."
]

# Planner structure
planner = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

# Show random quote
def show_quote():
    print("\n Quote of the Day:")
    print(random.choice(quotes))

# Display menu
def show_menu():
    print("\n--- Smart Weekly Planner ---")
    print("1. Add Task with Priority")
    print("2. View Tasks for a Day")
    print("3. Search Task by Keyword")
    print("4. View Weekly Summary")
    print("5. Count Total Tasks")
    print("6. Exit")

# Get a valid day input
def get_day():
    day = input("Enter day (e.g., Monday): ").capitalize()
    if day in planner:
        return day
    else:
        print("Invalid day. Try again.")
        return None

# Add a task with priority
def add_task():
    day = get_day()
    if day:
        task = input("Enter task : ")
        priority = input("Set priority (High / Medium / Low): ").capitalize()
        planner[day].append({"task": task, "priority": priority})
        print(" Task added!")

# View tasks for a specific day
def view_tasks():
    day = get_day()
    if day:
        tasks = planner[day]
        if tasks:
            print(f"\n Tasks for {day}:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. [{t['priority']}] {t['task']}")
        else:
            print("No tasks for this day.")

# Search task across all days
def search_tasks():
    keyword = input("Enter keyword to search: ").lower()
    found = False
    for day, tasks in planner.items():
        for t in tasks:
            if keyword in t["task"].lower():
                print(f" Found in {day}: [{t['priority']}] {t['task']}")
                found = True
    if not found:
        print("No tasks found with that keyword.")

# Weekly summary
def view_weekly_summary():
    print("\n Weekly Summary:")
    for day, tasks in planner.items():
        print(f"\n{day}:")
        if tasks:
            for t in tasks:
                print(f"  [{t['priority']}] {t['task']}")
        else:
            print("  No tasks.")

# Count total tasks
def task_count():
    total = sum(len(tasks) for tasks in planner.values())
    print(f"\n Total tasks for the week: {total}")

# Main loop
show_quote()
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        search_tasks()
    elif choice == '4':
        view_weekly_summary()
    elif choice == '5':
        task_count()
    elif choice == '6':
        print(" Exiting Smart Weekly Planner. Stay organized!")
        break
    else:
        print("Invalid option. Choose between 1-6.")
