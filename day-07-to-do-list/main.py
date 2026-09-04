def addTask(todo,userInput):
    while userInput.lower()=='y':
        task=input("Enter the task you want to add: ")
        todo.append(task)
        print("Task added")
        userInput=input("Do you want to add another task: ")
        return addTask(todo,userInput)
    else:
        return todo

def deleteTask(todo,userInput):
    while userInput=='y':
        task=int(input("Enter the task number you want to delete: "))
        todo.pop(task)
        userInput=input("Do you want to delete another task: ")
        return deleteTask(todo,userInput)
    else:
        return todo

print("==== TO-DO LIST ====")
todo=["Empty list"]
print(todo)

updateTodo=int(input("Enter the updation you want to do: "))
match updateTodo:
    case 1:
        todo= addTask(todo,'y')
    case 2:
        todo= deleteTask(todo, 'y')
    case _:
        print("Invalid input")

print(todo[1:])