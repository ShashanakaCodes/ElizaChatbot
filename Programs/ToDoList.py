FILE_NAME = "tasks.csv"
tasks = []

def create_csv_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task', 'Deadline'])
def save_tasks_to_csv():
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Deadline'])
        for task in tasks:
            if 'deadline' in task:
                writer.writerow([task['name'], task['deadline']])
            else:
                writer.writerow([task, ""])
def load_tasks_from_csv():
    create_csv_file()
    tasks.clear()  # Clear the existing tasks before loading from CSV
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if row[1] != "":
                tasks.append({'name': row[0], 'deadline': row[1]})
            else:
                tasks.append({'name': row[0]})
def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("Tasks:")
        tasks_with_deadline = [task for task in tasks if 'deadline' in task]
        tasks_without_deadline = [task for task in tasks if 'deadline' not in task]

        if tasks_with_deadline:
            print("\nTasks with Deadline:")
            for i, task in enumerate(sorted(tasks_with_deadline, key=lambda x: x['deadline']), start=1):
                print(f"{i}. {task['name']} - Deadline: {task['deadline']}")

        if tasks_without_deadline:
            print("\nTasks without Deadline:")
            for i, task in enumerate(tasks_without_deadline, start=len(tasks_with_deadline) + 1):
                print(f"{i}. {task['name']}")
show_tasks()
def add_task(task):
    has_deadline = input("Does the task have a deadline? (yes/no): ").lower()
    if has_deadline == 'yes':
        deadline = input("Enter the deadline for the task: ")
        tasks.append({'name': task, 'deadline': deadline})
    else:
        tasks.append({'name': task})
    print(f"Task '{task}' added.")
def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)['name']
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")
def update_task(task_index):
    if 1 <= task_index <= len(tasks):
        print("1. Edit Task\n2. Edit Deadline")
        sub_choice = input("Enter your sub-choice: ")
        if sub_choice == '1':
            updated_task = input("Enter the updated task: ")
            tasks[task_index - 1]['name'] = updated_task
            print(f"Task {task_index} updated to '{updated_task}'.")
        elif sub_choice == '2':
            updated_deadline = input("Enter the updated deadline: ")
            tasks[task_index - 1]['deadline'] = updated_deadline
            print(f"Task {task_index} deadline updated to '{updated_deadline}'.")
        else:
            print("Invalid sub-choice.")
        save_tasks_to_csv()
    else:
        print("Invalid task index.")
load_tasks_from_csv()
def todo():
    while True:
        print("\nMain Menu\n1. Show Tasks\n2. Add Task\n3. Delete Task\n4. Update Task\n5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(task)
            save_tasks_to_csv()
        elif choice == '3':
            show_tasks()
            task_index = int(input("Enter the index of the task to delete: "))
            delete_task(task_index)
            save_tasks_to_csv()
        elif choice == '4':
            show_tasks()
            task_index = int(input("Enter the index of the task to update: "))
            update_task(task_index)
        elif choice == "5":
                print("Exiting the to-do. Gooodbye!")
                break
        else:
            print("Invalid choice. Please try again.")
