# SPEND - WISE
name = input("Enter your name : ")
print(f"Hello, {name} Welcome to the Expense Tracker !")

budget = int(input("What's your Monthly Budget : "))

# Expense used bar 
# print("""
#  __________
# ( |||      )
#  ‾‾‾‾‾‾‾‾‾‾""")

expenses = []

def category():
    print(f"""
======== Select Category ========
1. Food & Dining
2. Groceries
3. Transportation
4. Bills & Utilities
5. Shopping
6. Education
7. Healthcare
8. Entertainment
9. Tours & Picnic
10. Personal / Miscellaneous
11. Other
=================================  
""") 
       
    user_response = int(input("Choose Category : "))

    if(user_response == 1):
        val = "Food & Dining"
        return val
    elif(user_response == 2):
        val = "Groceries"
        return val
    elif(user_response == 3):
        val = "Transportation"
        return val        
    elif(user_response == 4):
        val = "Bills & Utilities"
        return val
    elif(user_response == 5):
        val = "Shopping"
        return val
    elif(user_response == 6):
        val = "Education"
        return val
    elif(user_response == 7):
        val = "Healthcare"
        return val
    elif(user_response == 8):
        val = "Entertainment"
        return val
    elif(user_response == 9):
        val = "Tours & Picnic"
        return val
    elif(user_response == 10):
        val = "Personal / Miscellaneous"
        return val
    elif(user_response == 11):
        val = "None"
        return val
    else:
        print("INVALID RESPONSE")
        menu()


def add_expense():
    global total_expense
    global ID
    ID += 1
    transaction_ID = ID
    value = category()
    expense_name = input("Expense Name : ")
    expense_amt = int(input("Expense Amount : "))
    expenses.append({
        "Tracker ID" : transaction_ID,
        "Category" : value,
        "Name" : expense_name,
        "Amount" : expense_amt
    })
    
    total_expense += expense_amt
    print("Expense is added Succesfully !")
    menu()

def view_expense():
    print()
    for expense in expenses:
        print(f"""|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
| Category       : {expense["Category"]}   
| Expense        : {expense["Name"]}       
| Amount         : {expense["Amount"]}     
| Transaction ID : {expense["Tracker ID"]}  
|___________________________________________
""")
    menu()

def search_expense():
    print("""
======= SEARCH BY =======
1. Category
2. Name
3. Amount
4. ID
5. RETURN TO MENU
========================
""")
    user_response = int(input("Chose Option : "))

    # Search by Category
    if user_response == 1:
        value = category()
        for expense in expenses:
            if expense["Category"] == value:
                print(f"""
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
| Category       : {expense["Category"]}   
| Expense        : {expense["Name"]}       
| Amount         : {expense["Amount"]}     
| Transaction ID : {expense["Tracker ID"]}  
|___________________________________________
""")        
            else:
                print("No Expenses in Category")
        menu()

    # Search By Name
    elif user_response == 2:
        search = input("Expense Name : ")
        for expense in expenses:
            if search.lower() in expense["Name"].lower():
                print(f"""
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
| Category       : {expense["Category"]}   
| Expense        : {expense["Name"]}       
| Amount         : {expense["Amount"]}     
| Transaction ID : {expense["Tracker ID"]}  
|___________________________________________
""") 
            else:
                print()
                print("No Expense Record Found")
                menu()
        menu()

    #Search by Amount
    elif user_response == 3:
        print("Enter the Range")
        min = int(input("Minimum Amount : "))
        max = int(input("Maximum Amount : "))
        for expense in expenses:
            if min <= expense["Amount"] <= max:
                print(f"""
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
| Category       : {expense["Category"]}   
| Expense        : {expense["Name"]}       
| Amount         : {expense["Amount"]}     
| Transaction ID : {expense["Tracker ID"]}  
|___________________________________________
""")
            else:
                print("No Expense Found")
                menu()
        menu()        

    # Search by ID
    elif user_response == 4:
        transaction_ID = int(input("Enter the ID : "))
        for expense in expenses:
            if expense["Tracker ID"] == transaction_ID:
                print(f"""
|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
| Category       : {expense["Category"]}   
| Expense        : {expense["Name"]}       
| Amount         : {expense["Amount"]}     
| Transaction ID : {expense["Tracker ID"]}  
|___________________________________________
""")        
            else:
                print("INVALID ID")
                menu()
        menu()

    # Return to Menu
    elif user_response == 5:
        menu()

    else:
        print("INVALID OPTION !")
        search_expense()

def monthly_summary():
    print(f"""
======= MONTHLY SUMMARY =======
Total Spending         : {total_expense}
Total Transactions     : {ID}

Highest Expense        : {max(expense["Amount"] for expense in expenses)}
Lowest Expense         : {min(expense["Amount"] for expense in expenses)}

================================
""")
        

def menu():
    print("""
======= MENU =======
1. Add Expense
2. View All Expenses
3. Search Expense
4. Monthly Summary
5. Category Analysis
6. Budget Tracker
7. Savings Report
8. Edit Expense
9. Remove Expense
10. Exit
=====================
""")

    user_response = int(input("Chose Option : "))

    if (user_response == 1):
        add_expense()
    elif (user_response == 2):
        view_expense()
    elif (user_response == 3):
        search_expense()
    elif (user_response == 4):
        monthly_summary()
    elif (user_response == 5):
        print("Category Analysis")
    elif (user_response == 6):
        print("Budget Tracker")
    elif (user_response == 7):
        print("Savings Report")
    elif (user_response == 8):
        print("Edit Expense")
    elif (user_response == 9):
        print("Remove Expense")
    elif (user_response == 10):
        print("Exiting the Expense Tracker. Goodbye!")
    else:
        print("INVALID RESPONSE")
        menu()


ID = 0
total_expense = 0
menu()

