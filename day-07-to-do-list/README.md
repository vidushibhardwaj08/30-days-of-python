# DAY 9 — TO-DO LIST

A command-line To-Do List application built using Python.

## ABOUT

The program allows users to create and manage tasks directly from the command line.

Each task is stored along with its current status as either `pending` or `completed`.

The application allows users to add new tasks, delete existing tasks using their task number, view all tasks along with their status, and update the status of a task between pending and completed.

The program runs continuously using a menu-driven interface, allowing users to perform multiple operations without restarting the application.

It also validates user input to prevent the program from crashing when invalid values or task numbers are entered.

## FEATURES

* Add one or multiple tasks

* Automatically assign `pending` status to newly added tasks

* Delete tasks using their displayed task number

* View all tasks with serial number, task name, and status

* Mark pending tasks as completed

* Change completed tasks back to pending

* Menu-driven command-line interface

* Continuous program execution

* Validation for invalid menu input

* Validation for invalid task numbers

* Exception handling for non-numeric input

## CONCEPTS PRACTICED

* Functions

* Dictionaries

* Dictionary keys and values

* `dict.items()`

* `dict.keys()`

* `dict.update()`

* `dict.pop()`

* `list()`

* User input

* Type conversion

* `while` loops

* `for` loops

* `if / else` statements

* `match / case`

* `try / except`

* `ValueError`

* `len()`

* `range()`

* f-strings

* String methods

* `.lower()`

* Input validation

* Dictionary manipulation

* Index-based task selection

## HOW TO RUN

Make sure Python is installed on your system.

Clone the repository or download the project files.

Navigate to the project directory and run:

```bash
python main.py
```

The application will display a menu where you can choose to add, delete, view, or update the status of tasks.

## EXAMPLE

```text
==== TO-DO LIST ====

Enter the updation you want to do:

1. Add Task
2. Delete Task
3. View Task
4. Edit Task Status

S.No.   TASK            STATUS
1       resume          pending
2       workout         pending
3       mock test       completed
```

## FUTURE ENHANCEMENTS

* Save tasks to a file so they remain available after restarting the program

* Load previously saved tasks automatically

* Add due dates and priorities to tasks

* Improve task formatting in the terminal

* Allow users to edit task names

* Add task categories

## LEARNING OUTCOME

This project helped me move beyond storing simple values in lists and understand how dictionaries can be used to associate related information.

I also practiced breaking a larger program into separate functions, manipulating dictionary data, handling invalid user input, and building a menu-driven application that can perform multiple operations during a single execution.
