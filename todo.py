tasks=[]
def show_menu():
    print("\n1. View\n2. Add\n3. Delete\n4. Exit")
def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(i, task)
def add_tasks():
    task = input("Enter task: ")
    tasks.append(task)
def delete_task():
    view_tasks()
    num = int(input("Enter number: "))
    tasks.pop(num - 1)
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
        break
       