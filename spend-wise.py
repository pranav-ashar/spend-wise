
name = input("Enter your name : ")
print(f"Hello, {name} Welcome to the Expense Tracker !")

# print("""
#  __________
# ( |||      )
#  ‾‾‾‾‾‾‾‾‾‾""")


def menu():
    print("""
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
""")

    user_response = int(input("User Response : "))

    if (user_response == 1):
        print("Add Expense")
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
        print("Invalid Response")

while True:
    menu()