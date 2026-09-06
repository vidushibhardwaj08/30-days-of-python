def addTask(todo,userInput):
    while userInput.lower()=='y':
        task=input("Enter the task you want to add: ")
        todo.update({task:"pending"})
        print("Task added\n")
        userInput=input("Do you want to add another task: ")
    else:
        return todo

def deleteTask(todo,userInput):
    while userInput.lower()=='y':
        try:
            task_index=int(input("Enter the task number you want to delete: "))

            if 1<= task_index <= len(todo):
                key_to_delete=list(todo.keys())[task_index - 1]
                todo.pop(key_to_delete)
                print(f"{key_to_delete} deleted successfully\n")
            else:
                print("Invalid task number")
        except ValueError:
            print("please enter a valid number")

        userInput=input("Do you want to delete another task: ")
    return todo

def viewTask(todo):
    if len(todo)==0:
        print("No tasks")
    else:
        print("S.No.\tTASK\t\tSTATUS")
        i=1
        for key, value in todo.items():
            print(f"{i}\t{key}\t\t{value}")
            i += 1
        print("\n")

print("==== TO-DO LIST ====")
todo={"resume":"pending", "workout":"pending", "mock test":"completed"}

while True:
    try:
        updateTodo=int(input("Enter the updation you want to do:\n"
            "1. Add Task\n"
            "2. Delete Task\n"
            "3. View Task\n"))
    except ValueError:
        print("Please enter a valid number\n")
        continue

    match updateTodo:
        case 1:
            todo= addTask(todo,'y')
        case 2:
            todo= deleteTask(todo, 'y')
        case 3:
            viewTask(todo)
        case _:
            print("Invalid input")
            exit()


