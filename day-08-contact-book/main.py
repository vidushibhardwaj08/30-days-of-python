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

def viewContacts():
    if not contacts:
        print("No contacts found")
        return

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
    
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
    elif userInput==2:
        viewContacts()
    if userInput==6:
        break

print(contacts)