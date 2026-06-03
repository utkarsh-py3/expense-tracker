# Personal Expense Tracker

print("=" * 45)
print("💸  Welcome to Personal Expense Tracker  💸")
print("=" * 45)
print("Track your daily spending easily and smartly!")
print("\nChoose an option from the menu below:\n")

expenses = [] # Main list that stores all expense records


# Load saved expenses from file
# This makes the data persistent even after the program is closed
try:
    with open("expense_tracker.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")

            expense = {
                "Date": parts[0],
                "Category": parts[1],
                "Description": parts[2],
                "Amount": float(parts[3])
            }

            expenses.append(expense)# adding the data that is saved in  file into list
        #so that the given below function can be performed on the saved data 
        # making your data permanently save (you can allways delete the data using the option from menu)

except FileNotFoundError:
    pass



# Save all current expenses back to the file
# Used after deleting an expense
def save_expenses():
    with open("expense_tracker.txt", "w") as file:
        for expense in expenses:
            file.write(
                f"{expense['Date']},"
                f"{expense['Category']},"
                f"{expense['Description']},"
                f"{expense['Amount']}\n"
            )


# Add Expense
def add_expense():
    date = input("Enter the date of expense: ")
    category = input("Enter the category (food, travel, shopping): ")
    description = input("Enter expense description: ")
    amount = float(input("Enter the amount of expense: "))

    expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    expenses.append(expense)

    with open("expense_tracker.txt", "a") as file:# for saving the expense in the file(for making the data permanent)
        file.write(
            f"{date},{category},{description},{amount}\n"
        )

    print("\nExpense successfully added.")
    print(f"Total expenses added: {len(expenses)}")


# View Expenses
def view_expense():
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    for expense in expenses:
        print("-" * 30)
        print(f"{'Date:':15} {expense['Date']}")
        print(f"{'Category:':15} {expense['Category']}")
        print(f"{'Description:':15} {expense['Description']}")
        print(f"{'Amount:':15} {expense['Amount']}")
        print("-" * 30)


# Total Expense
def total_expense():
    if len(expenses) == 0:
        print("\nTill now the total expense is Zero")
        return

    total = 0

    for expense in expenses:
        total += expense["Amount"]

    print(f"\nTotal Expense Till Now = ₹{total}")
    print("-" * 30)


# Search Category
def search_category():
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    search_category = input("Enter category: ")

    found = False
    total = 0

    print("-" * 30)

    for expense in expenses:
        if expense["Category"].lower() == search_category.lower():

            found = True
            total += expense["Amount"]

            print(f"{'Date:':15} {expense['Date']}")
            print(f"{'Description:':15} {expense['Description']}")
            print(f"{'Amount:':15} {expense['Amount']}")
            print("-" * 30)

    if found:
        print(f"{search_category} Total = ₹{total}")# for the category wise total
    else:
        print("\nNo matching category found.")


# Delete Expense
def delete_expense():
    if len(expenses) == 0:
        print("\nNo expenses available to delete.")
        return

    for i, expense in enumerate(expenses):
        print(f"{i} => {expense}")

    try:
        select = int(input("Enter expense number to delete: "))

        expenses.pop(select)

        save_expenses()

        print("\nSelected expense deleted successfully.")
        print("-" * 30)

    except (ValueError, IndexError):
        print("\nInvalid expense number.")
        print("-" * 30)


# Main Menu
while True:

    print("\n===== EXPENSE TRACKER MENU =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Search Category")
    print("5. Delete Expense")
    print("6. Exit")
    print("=" * 30)

    try:
        choice = int(input("\nEnter option from menu: "))

    except ValueError:
        print("\nPlease enter a valid number.")
        continue

    print()

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expense()

    elif choice == 3:
        total_expense()

    elif choice == 4:
        search_category()

    elif choice == 5:
        delete_expense()

    elif choice == 6:
        print("\nThank you for using Expense Tracker 💸")
        break

    else:
        print("\nInvalid choice. Please try again.")