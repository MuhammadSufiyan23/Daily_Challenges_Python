# DAY-7 CHALLENGE

def show_menu():
    print("\nWelcome to To-Do List!")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("✅ Task Added!")

def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks added yet!")
    else:
        print("\n📝 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"❌ Deleted: {removed_task}")
            else:
                print("⚠ Invalid task number!")
        except ValueError:
            print("⚠ Please enter a valid number!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Have a great day!")
            break
        else:
            print("⚠ Invalid choice! Please select from 1-4.")

if __name__ == "__main__":
    main()
