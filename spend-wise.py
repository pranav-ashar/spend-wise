# SPEND-WISE
name = input("Enter your name : ")
print(f"Hello, {name} Welcome to the Expense Tracker !")

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
        print("Food & Dining")
    elif(user_response == 2):
        print("Groceries")
    elif(user_response == 3):
        print("Transportation")
    elif(user_response == 4):
        print("Bills & Utilities")
    elif(user_response == 5):
        print("Shopping")
    elif(user_response == 6):
        print("Education")
    elif(user_response == 7):
        print("Healthcare")
    elif(user_response == 8):
        print("Entertainment")
    elif(user_response == 9):
        print("Tours and Picnic")
    elif(user_response == 10):
        print("Personal / Miscellaneous")
    elif(user_response == 11):
        print("Other")
    else:
        print("INVALID RESPONSE")

def add_expense():
    category()


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
9. Delete Expense
10. Exit
=====================
""")

    user_response = int(input("Chose Option : "))

    if (user_response == 1):
        add_expense()
    elif (user_response == 2):
        print("View All Expenses")
    elif (user_response == 3):
        print("Search Expense")
    elif (user_response == 4):
        print("Monthly Summary")
    elif (user_response == 5):
        print("Category Analysis")
    elif (user_response == 6):
        print("Budget Tracker")
    elif (user_response == 7):
        print("Savings Report")
    elif (user_response == 8):
        print("Edit Expense")
    elif (user_response == 9):
        print("Delete Expense")
    elif (user_response == 10):
        print("Exiting the Expense Tracker. Goodbye!")
    else:
        print("INVALID RESPONSE")
        menu()


menu()