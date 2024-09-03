# Define the Task class
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

# Define the ToDoList class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Removed task: {removed_task.description}")
        else:
            print("Invalid task number.")

    def mark_task_complete(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_complete()
            print(f"Marked task as complete: {self.tasks[task_number].description}")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

# Display the menu options
def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Mark a task as complete")
    print("4. Show all tasks")
    print("5. Exit")

# Main function to run the application
def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)

        elif choice == '2':
            task_number = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(task_number)

        elif choice == '3':
            task_number = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.mark_task_complete(task_number)

        elif choice == '4':
            todo_list.show_tasks()

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
