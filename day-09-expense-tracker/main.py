print("\nEXPENSE TRACKER\n")

expenseList=[]

def addExpense():
    print("im here")
    description= input("Enter expense description: ")
    amount= input("Enter expense amount: ")
    category= input("Choose a category: ")

    new_expense={"name":description,"amount":amount,"category":category}
    expenseList.append(new_expense)
    print(f"{description} added in expense list")

def viewExpense():
    for expense in expenseList:
        print(f"\nName: {expense["name"]}")
        print(f"Amount: {expense["amount"]}")
        print(f"Category: {expense["category"]}")

while True:
    choice=int(input("\nSelect an option: " \
"\n1. Add an expense" \
"\n2. View all expenses" \
"\n3. Calculate total expenses" \
"\n4. View expenses by category" \
"\n5. Delete an expense" \
"\n6. Exit\n"))
    if choice==1:
        addExpense()
    elif choice==2:
        viewExpense()
    elif choice==6:
        break

