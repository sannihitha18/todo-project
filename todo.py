tasks=[]
def show_menu():
    print("\n1. View\n2. Add\n3. Delete\n4. Mark Done\n5.Exit")
def view_tasks():
    if not tasks:
        print("No tasks!")
    for i, (task, done) in enumerate(tasks, 1):
            status = "✅" if done else "❌"
            print(f"{i}. {task} [{status}]")
def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark done: "))
    tasks[num - 1][1] = True
def add_tasks():
    task = input("Enter task: ")
    tasks.append([task,False])
def save_tasks():
    with open("tasks.txt", "w") as f:
        for task, done in tasks:
            f.write(f"{task}|{done}\n")
def load_tasks():
    tasks.clear()   
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task, done = line.strip().split("|")
                tasks.append([task, done == "True"])
    except:
        pass
def delete_task():
    view_tasks()
    try:
        num = int(input("Enter number: "))
        tasks.pop(num - 1)
    except:
        print("Invalid input!")
load_tasks()
while True:
    show_menu()
    ch = input("Choice: ")
    if ch == "1":
        view_tasks()
    elif ch == "2":
        add_tasks()
    elif ch == "3":
        delete_task()
    elif ch == "4":
        mark_done()
    elif ch == "5":
        save_tasks()
        print("Tasks saved successfully")
        break
        
       