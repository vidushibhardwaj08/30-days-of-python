print("\nCONTACT BOOK\n")
contacts = {}

def addContact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully")

while True:
    print("""    1. Add Contact
    2. View All Contacts
    3. Search Contact
    4. Update Contact
    5. Delete Contact
    6. Exit\n""")

    userInput = int(input("Choose an option: "))

    if userInput==1:
        addContact()

    if userInput==6:
        break

print(contacts)