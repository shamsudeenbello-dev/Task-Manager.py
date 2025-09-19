# A simple Task Manager program

# List to store tasks
Task_box = []


def show_tasks():
    """Display all saved tasks."""
    if not Task_box:
        print("No New Tasks Added Yet!\n")
    else:
        for i, task in enumerate(Task_box, 1):
            print(f"{i}. {task}")
        print()  # Clean spacing


def add_task(new_task, user_name):
    """Add a new task to the Task_box."""
    if new_task.strip():  # Prevent empty tasks
        Task_box.append(new_task)
        print(f"{user_name}, Your Task Has Been Successfully Added!\n")
    else:
        print("Empty tasks cannot be added!\n")


def delete_task(Del_task):
    """Delete a task by its number (1-based index)."""
    if Task_box:  # Prevent IndexError on empty list
        option_removed = Task_box.pop(Del_task - 1)
        print(f"Task '{option_removed}' has been Deleted.\n")
    else:
        print("No tasks to delete!\n")


def edit_task(task_number, user_name):
    """Edit/update a task by its number (1-based index)."""
    if 0 < task_number <= len(Task_box):
        print(f"Current Task: {Task_box[task_number - 1]}")
        new_value = input("Enter the new task description: ")
        if new_value.strip():
            Task_box[task_number - 1] = new_value
            print(f"{user_name}, Task {task_number} has been successfully updated!\n")
        else:
            print("Empty input is not allowed. Task not updated.\n")
    else:
        print("Invalid Task Number!\n")


def main():
    """Main program loop for task manager."""
    print("=" * 60)
    print(" " * 23, "TASK MANAGER")
    print("=" * 60, "\n")

    # Prompt for username (default if none given)
    user_name = input("Please Input Your Name Here:  ") or "Dear User"

    print(f"\nWelcome To Task Manager, {user_name}.\n")
    print(f"{user_name}, this is a task-managing program that enables you to "
          "store, add, delete, and edit important tasks in order to reduce your daily workload.\n")

    while True:
        # Menu options
        print(f"\nWhat would you like to do, {user_name}?\n")
        print("1. Show All Saved Tasks ✓")
        print("2. Add A New Task ✓")
        print("3. Delete A Saved Task ✓")
        print("4. Clear All Saved Tasks ✓")
        print("5. Edit A Task ✓")
        print("6. End The Program\n")

        # Get user choice
        task_type = input("Select An Option:  ")
        try:
            task_type = int(task_type)
        except ValueError:
            print("Input A Number!\n")
            continue

        # Handle menu choice
        if task_type == 1:
            show_tasks()

        elif task_type == 2:
            new_task = input("Add New Task: ")
            add_task(new_task, user_name)

        elif task_type == 3:
            if not Task_box:
                print("No tasks to delete!\n")
                continue
            show_tasks()
            Del_task = input("Choose The Task To Delete: ")
            try:
                Del_task = int(Del_task)
            except ValueError:
                print("Input A Number!\n")
                continue
            if 0 < Del_task <= len(Task_box):
                confirm = input(f"Are you sure you want to delete task {Del_task}? (yes/no): ").lower()
                if confirm == "yes":
                    delete_task(Del_task)
                else:
                    print("*Delete* Cancelled.\n")
            else:
                print(f"{user_name}, That Is An Invalid Task Number!\n")

        elif task_type == 4:
            if Task_box:
                confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()
                if confirm == "yes":
                    Task_box.clear()
                    print(f"{user_name}, all saved tasks have been successfully deleted!\n")
                else:
                    print("Clear All Cancelled.\n")
            else:
                print("No tasks to clear!\n")

        elif task_type == 5:
            if not Task_box:
                print("No tasks to edit!\n")
                continue
            show_tasks()
            task_num = input("Choose The Task To Edit: ")
            try:
                task_num = int(task_num)
            except ValueError:
                print("Input A Number!\n")
                continue
            edit_task(task_num, user_name)

        elif task_type == 6:
            print(f"\nThanks For Your Time!, {user_name}\n")
            break

        else:
            print("Invalid Task Number!\n")


if __name__ == "__main__":
    main()