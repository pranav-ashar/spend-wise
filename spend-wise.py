# SPEND - WISE
tracker = {
    "1. Food & Dining" : {
        
    },

    "2. Groceries" : {

    },

    "3. Transportation" : {

    },

    "4. Bills & Utilities" : {

    },

    "5. Shopping" : {

    },

    "6. Education" : {

    },

    ""
    "7. Healthcare" : {

    },

    "8. Entertainment" : {

    },

    "9. Tours & Picnic" : {

    },

    "10. Personal / Miscellaneous" : {

    },
}



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
        val = "1. Food & Dining"
        return val
    elif(user_response == 2):
        val = "2. Groceries"
        return val
    elif(user_response == 3):
        val = "3. Transportation"
        return val        
    elif(user_response == 4):
        val = "4. Bills & Utilities"
        return val
    elif(user_response == 5):
        val = "5. Shopping"
        return val
    elif(user_response == 6):
        val = "6. Education"
        return val
    elif(user_response == 7):
        val = "7. Healthcare"
        return val
    elif(user_response == 8):
        val = "8. Entertainment"
        return val
    elif(user_response == 9):
        val = "9. Tours & Picnic"
        return val
    elif(user_response == 10):
        val = "Personal / Miscellaneous"
        return val
    elif(user_response == 11):
        val = "None"
        return val
    else:
        print("INVALID RESPONSE")

def add_expense():
    value = category()
    print()
    expense_name = input("Expense Name : ")
    expense_amt = int(input("Expense Amount : "))
    tracker[value][expense_name] = expense_amt
    print(f"{expense_name} is added succesfully")
    menu()

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