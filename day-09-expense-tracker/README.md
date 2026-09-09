# DAY 11 — EXPENSE TRACKER

A simple command-line Expense Tracker built using Python.

## ABOUT

The program allows users to add, view, calculate, filter, and delete expenses.

Each expense is stored with a description, amount, and category.

The program uses a list of dictionaries to store expense data and provides a menu-driven interface so users can perform different operations until they choose to exit.

The program also includes input validation and handles invalid values using exception handling.

## FEATURES

* Add a new expense

* Store expense description, amount, and category

* View all expenses

* Display expenses with numbering

* Calculate total expenses

* View expenses by category

* Calculate total spending for a selected category

* Delete an expense

* Validate expense amounts

* Handle invalid menu input

* Handle empty expense lists

* Case-insensitive category matching

* Menu-driven program

## CONCEPTS PRACTICED

* Python functions

* Lists

* Dictionaries

* List of dictionaries

* `for` loops

* `while` loops

* `if / elif / else`

* User input

* `float()`

* `int()`

* `try / except`

* `ValueError`

* Input validation

* `enumerate()`

* `.lower()`

* `append()`

* `pop()`

* Dictionary key-value access

* Calculations

* Searching and filtering data

* Variable scope

* Returning values from functions

## HOW TO RUN

Make sure Python is installed on your system.

Clone the repository or download the project files.

Open the project folder in your terminal and run:

```bash
python main.py
```

## MENU OPTIONS

The program provides the following options:

```text
1. Add an expense
2. View all expenses
3. Calculate total expenses
4. View expenses by category
5. Delete an expense
6. Exit
```

## EXAMPLE

```text
EXPENSE TRACKER

Select an option:

1. Add an expense
2. View all expenses
3. Calculate total expenses
4. View expenses by category
5. Delete an expense
6. Exit

Enter expense description: Coffee
Enter expense amount: 150
Choose a category: Food

Coffee added to expense list
```

The user can continue adding expenses and use the other menu options to view and manage them.

## LEARNING OUTCOME

This project helped me understand how Python data structures can be used together to store and manage structured information.

I also practiced separating program functionality into functions, performing calculations on stored data, filtering records based on user input, validating input, and building a menu-driven command-line application.
