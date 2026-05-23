# a expense tracker 
print("=" * 45)
print("💸  Welcome to Personal Expense Tracker  💸")
print("=" * 45)
print("Track your daily spending easily and smartly!")
print("\nChoose an option from the menu below:\n")
expenses = [] # an empty list

with open("expense_tracker.txt", "r") as file:

    for line in file:

        parts = line.strip().split(",") # split()convert the string into list because it is seperated with spaces

        expense = {

            "Date": parts[0],

            "Category": parts[1],

            "Description": parts[2],

            "Amount": float(parts[3])

        }

        expenses.append(expense) # adding the data that is saved in  file into list
        #so that the given below function can be performed on the saved data 
        # making your data permanently save (you alway delete the data using the option from menu)
   
def add_expense(): # function to add an expense 
    date=input("Enter the date of expense: ")
    category=input("Enter the category of the expense (food , travel, shoping ,):  ")
    description=input("Enter expense description: ")
    amount = float(input("Enter the amount of expense: "))
    expense ={
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount,
        }
    expenses.append(expense)
    with open("expense_tracker.txt","a") as file: # for saving the expense in the file(for making the data permanent)
        file.write(f"{date},{category},{description},{amount}\n")
    print("\nExpense is succesfully added")
    print(f"\n Total expense added : {len(expenses)}")

def view_expense():# function to veiw the expense
    if len(expenses)==0:
        print("Add expense")
    else:   
        for expense in expenses:
            print("-"*30)
            print(f"{'Date:':15} {expense['Date']}")
            print(f"{'Category:':15} {expense['Category']}")
            print(f"{'Description:':15} {expense['Description']}")
            print(f"{'amount:':15} {expense['Amount']}")
            print("-"*30)
def total_expense(): # function for the total expense(total amount till now)
    if len(expenses)==0:
        print("\nTill now the total expense is Zero")  
    else:
        total_expense = 0
        for expense in expenses:
            total_expense  += expense["Amount"]
        print(f"The total expense till now = {total_expense}")
        print("-"*30)       

def search_category():# function to search the category
    if(len(expenses))==0:
        print("\n No expense found ")
        return 
    search_category = input("Enter the category: ")
    print("-"*30)
    found = False
    total = 0
    for expense in expenses:
        if  expense['Category'].lower() == search_category.lower():

            found = True
            total +=expense['Amount']
            
            print(f"{'Date:':15} {expense['Date']}")
            print(f"{'Description:':15} {expense['Description']}")
            print(f"{'Amount:':15} {expense['Amount']}") 
            print("-"*30)
    if found :
            print(f" {search_category} total : {total}")# for the category wise total
    else:        
        print("\n No matching category found.")

def delete_expense():#function to delete an expense
    for i , expense in enumerate(expenses):
        print(f"{i:7} => {expense}")
    try:  # tries to execute  
        select = int(input("Enter the expense no.: "))
        expenses.pop(select)
        print("\n The selected expense has been deleted.")
        print("-"*30)
    except:#if an error occur the program jump to this
        print("\nInvalid expense number.")
        print("-"*30)
    def safe_expense():  # function to save the remaining expense in expenses[]  
        with open("expense_tracker.txt","w") as file: #clears old file content.
            for expense in expenses:
                 file.write(f"{expense['Date']},{expense['Category']},{expense['Description']},{expense['Amount']}\n")
    safe_expense()

while True:# this loop is added to keep running the program untill user chose to exit 
    print("\n===== EXPENSE TRACKER MENU =====")
    print("1. Add expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Search Category")
    print("5. Delete expense ")
    print("6. Exit")
    print("="*30)
    print("\n  ")
     
    choice =int(input("Enter the option from menu: "))
    print("\n")
    
    if choice==1:
        add_expense()
    elif choice==2:
        view_expense()
    elif choice==3:
        total_expense()
    elif choice == 4:
        search_category()
    elif choice == 5:
        delete_expense()    
    elif choice == 6:
        print("\nThank you for using Expense Tracker 💸")
        break
    else :
         print("\nInvalid choice. Please try again.")    



