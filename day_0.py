# a expense tracker 
print("=" * 45)
print("💸  Welcome to Personal Expense Tracker  💸")
print("=" * 45)
print("Track your daily spending easily and smartly!")
print("\nChoose an option from the menu below:\n")
expenses = []
while True:
    print("\n===== EXPENSE TRACKER MENU =====")
    print("1. Add expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Search Category")
    print("5. Exit")
     
    choice =int(input("Enter the option from menu: "))
    
    if choice==1:
        date=input("Enter the date of expense: ")
        category=input("enter the category of the expense (food , travel, shoping ,):  ")
        description=input("Enter expense description: ")
        amount = float(input("enter the amount of expense: "))
        expense ={
            "Date": date,
            "Category": category,
            "description": description,
            "Amount": amount,
        }
        expenses.append(expense)
        print("Expense is succesfully added")
    if choice==2:
        if len(expenses)==0:
            print("Add expense")
        else:    
           for expense in expenses:
               print(f"Date: {expense['Date']}")
               print(f"Category: {expense['Category']}")
               print(f"Description: {expense['description']}")
               print(f"amount: {expense['Amount']}")
               print("-"*30)
    if choice==3:
        if len(expenses)==0:
            print("Till now the total expense is Zero")  
        else:
            total_expense = 0
            for expense in expenses:
                 total_expense  += expense["Amount"]
                 print(f"The total expense till now = {total_expense}")
                 print("-"*30)       

    if choice == 4:
        if(len(expenses))==0:
            print("no expense found")
        category1 = input("Enter the category: ")
        for expense in expenses:
            if category1 == expense['Category']:
                print(expense['Amount']) 
        print("-"*30)
    elif choice == 5:
    
         print("Thank you for using Expense Tracker 💸")

         break



