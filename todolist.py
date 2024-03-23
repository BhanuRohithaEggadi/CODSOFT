class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority, due_date):
        task = Task(description, priority, due_date)
        self.tasks.append(task)

    def edit_task(self, task_index, new_description, new_priority, new_due_date):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.description = new_description
            task.priority = new_priority
            task.due_date = new_due_date
        else:
            print("Invalid task index. Task not found.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index. Task not found.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
        else:
            print("Invalid task index. Task not found.")

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✓" if task.completed else " "
            print(f"{i + 1}. [{status}] {task.description} (Priority: {task.priority}, Due: {task.due_date})")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List App ---")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Display Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(description, priority, due_date)
        elif choice == "2":
            task_index = int(input("Enter task index to edit: ")) - 1
            new_description = input("Enter new task description: ")
            new_priority = input("Enter new task priority: ")
            new_due_date = input("Enter new due date: ")
            todo_list.edit_task(task_index, new_description, new_priority, new_due_date)
        elif choice == "3":
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_completed(task_index)
        elif choice == "5":
            todo_list.display_tasks()
        elif choice == "6":
            print("Exiting the app. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
