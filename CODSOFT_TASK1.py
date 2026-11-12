import json
import os

tasks = []
file_name = "tasks.json"


def save_tasks():
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    global tasks

    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as file:
                tasks = json.load(file)
        except (json.JSONDecodeError, OSError):
            tasks = []


def add_task():
    name = input("Enter your task: ").strip()

    if name == "":
        print("Task cannot be empty.")
        return

    tasks.append({"name": name, "done": False})
    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("Your task list is empty.")
        return

    print("\n--- Your To-Do List ---")

    for i, task in enumerate(tasks, start=1):
        if task["done"]:
            status = "Completed"
        else:
            status = "Pending"

        print(str(i) + ". " + task["name"] + " - " + status)


def update_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter the task number to update: "))

        if 1 <= number <= len(tasks):
            name = input("Enter the new task name: ").strip()

            if name == "":
                print("Task name cannot be empty.")
                return

            tasks[number - 1]["name"] = name
            save_tasks()
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter the task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter the task number to delete: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            save_tasks()
            print("Deleted task:", removed_task["name"])
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


load_tasks()

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Thank you for using the To-Do List!")
        break
    else:
        print("Invalid choice. Please try again.")
