"""
To-Do List App - A basic command-line application for task management.

Users can add, view, remove, and update status of tasks.
"""

# Initialize an empty list to store tasks with status
todo_list = []

# Infinite loop for the app menu

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print("5. Update Task Status")

    choice = input("Enter your choice (1-5):").strip()

    if choice == "1":
        task_text = input("Enter the task: ").strip()
        task = {"task": task_text, "status": "Pending"}
        todo_list.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not todo_list:
            print("No tasks yet.")
        else:
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task['task']} - Status: {task['status']}")

    elif choice == "3":
        if not todo_list:
            print("Nothing to remove.")
        else:
            try:
                task_no = int(input("Enter the task number to remove: "))
                if 1 <= task_no <= len(todo_list):
                    removed = todo_list.pop(task_no - 1)
                    print(f"Removed task: {removed['task']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List App. Goodbye!")
        break

    elif choice == "5":
        if not todo_list:
            print("Nothing to update.")
        else:
            try:
                task_no = int(input("Enter the task number to update: "))
                if 1 <= task_no <= len(todo_list):
                    new_status = input("Enter new status (Pending / Done): ").strip().capitalize()
                    if new_status in ["Pending", "Done"]:
                        todo_list[task_no - 1]["status"] = new_status
                        print(f"✅ Task {task_no} status updated to '{new_status}'.")
                    else:
                        print(" Invalid status. Please enter 'Pending' or 'Done'.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    else:
        print("Invalid choice. Please try again.")
