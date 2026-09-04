def addTask(todo,userInput):
    while userInput.lower()=='y':
        task=input("Enter the task you want to add: ")
        todo.append(task)
        print("Task added")
        userInput=input("Do you want to add another task: ")
    else:
        return todo

def deleteTask(todo,userInput):
    while userInput.lower()=='y':
        try:
            task=int(input("Enter the task number you want to delete: "))

            if 1<= task <= len(todo):
                deleted_task=todo.pop(task-1)
                print(f"{deleted_task} deleted succesfully")
            else:
                print("Invalid task number")
        except ValueError:
            print("please enter a valid number")

        userInput=input("Do you want to delete another task: ")
        return todo

print("==== TO-DO LIST ====")
todo=[]
print(todo)

updateTodo=int(input("Enter the updation you want to do:\n"
    "1. Add Task\n"
    "2. Delete Task\n"))
match updateTodo:
    case 1:
        todo= addTask(todo,'y')
    case 2:
        todo= deleteTask(todo, 'y')
    case _:
        print("Invalid input")

print(todo)