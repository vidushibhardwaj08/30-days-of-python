# DAY 10 — CONTACT BOOK

A simple command-line Contact Book built using Python.

## ABOUT

The program allows users to store and manage contact information through an interactive command-line menu.

Each contact contains a name, phone number, and email address. The program uses a nested dictionary to store contact details and provides options to add, view, search, update, and delete contacts.

The program continues running until the user chooses to exit and also handles invalid menu inputs to prevent the application from crashing.

## FEATURES

* Add a new contact with name, phone number, and email

* View all saved contacts

* Search for a contact by name

* Update the phone number and email of an existing contact

* Delete an existing contact

* Display a message when no contacts are available

* Display a message when a searched contact does not exist

* Handle invalid menu inputs using exception handling

* Validate that the selected menu option is between 1 and 6

* Keep the program running until the user chooses to exit

## CONCEPTS PRACTICED

* Dictionaries

* Nested dictionaries

* Dictionary keys and values

* `.items()`

* `.pop()`

* Functions

* Function calls

* `while` loops

* `for` loops

* `if / elif / else`

* `input()`

* Type conversion

* `try / except`

* `ValueError`

* `continue`

* `break`

* `return`

* Input validation

* Searching dictionary data

* Updating dictionary values

* Deleting dictionary entries

* CRUD operations

## HOW TO RUN

Make sure Python is installed, then run:

```bash
python main.py
```

The program will display the following menu:

```text
CONTACT BOOK

1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

Choose an option by entering a number between 1 and 6 and follow the instructions displayed in the terminal.

## FUTURE ENHANCEMENTS

* Add phone number validation

* Add email address validation

* Prevent duplicate contacts

* Make contact searching case-insensitive

* Allow partial-name searches

* Allow users to update the contact name

* Sort contacts alphabetically

* Add confirmation before deleting a contact

* Store contacts in a file so that data remains available after closing the program

* Add a graphical user interface (GUI)
