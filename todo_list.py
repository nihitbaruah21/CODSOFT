import os

FILENAME = "mytasks.txt"

def read_tasks():
    if not os.path.isfile(FILENAME):
        return []
    with open(FILENAME, "r") as f:
        return [line.strip() for line in f.readlines()]

def write_tasks(task_list):
    with open(FILENAME, "w") as f:
        f.writelines([task + "\n" for task in task_list])

def list_tasks(task_list):
    print("\n📋 Your Tasks:")
    if not task_list:
        print("  (No tasks found)")
    else:
        for idx, task in enumerate(task_list, start=1):
            print(f"  {idx}. {task}")

def add_new_task(task_list):
    new_task = input("📝 Enter task description: ").strip()
    if new_task:
        task_list.append(new_task)
        print("✅ Task added.")
    else:
        print("⚠️ Empty task not added.")

def mark_done(task_list):
    list_tasks(task_list)
    try:
        num = int(input("✅ Task number to mark done: "))
        if 1 <= num <= len(task_list):
            task_list[num - 1] += " [DONE]"
            print("👌 Marked as done.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def remove_task(task_list):
    list_tasks(task_list)
    try:
        num = int(input("🗑️ Task number to delete: "))
        if 1 <= num <= len(task_list):
            removed = task_list.pop(num - 1)
            print(f"🗑️ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Enter a valid number.")

def main_menu():
    tasks = read_tasks()
    while True:
        print("\n--- To-Do Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save & Exit")

        choice = input("🔘 Choose an option (1-5): ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_new_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            write_tasks(tasks)
            print("📁 Tasks saved. Goodbye!")
            break
        else:
            print("❌ Invalid input. Try 1-5.")

if __name__ == "__main__":
    main_menu()