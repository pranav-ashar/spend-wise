expenses = []

ID = 0


def category():
    print("""
========== CATEGORY ==========

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

==============================
""")

    user_response = int(input("Choose Category : "))

    if user_response == 1:
        return "Food & Dining"

    elif user_response == 2:
        return "Groceries"

    elif user_response == 3:
        return "Transportation"

    elif user_response == 4:
        return "Bills & Utilities"

    elif user_response == 5:
        return "Shopping"

    elif user_response == 6:
        return "Education"

    elif user_response == 7:
        return "Healthcare"

    elif user_response == 8:
        return "Entertainment"

    elif user_response == 9:
        return "Tours & Picnic"

    elif user_response == 10:
        return "Personal / Miscellaneous"

    elif user_response == 11:
        return "Other"

    else:
        print("INVALID RESPONSE")
        return None


def monthly_statistics(expenses):
    total = 0
    count = 0
    highest = 0
    lowest = None
    category_totals = {}

    for expense in expenses:

        amount = expense["Amount"]
        category_name = expense["Category"]

        total += amount
        count += 1

        if amount > highest:
            highest = amount

        if lowest is None or amount < lowest:
            lowest = amount

        if category_name not in category_totals:
            category_totals[category_name] = 0

        category_totals[category_name] += amount

    return total, count, highest, lowest, category_totals


def add_expense():
    global ID

    value = category()

    if value is None:
        menu()
        return

    expense_name = input("Expense Name : ")
    expense_amt = int(input("Expense Amount : "))

    if expense_amt <= 0:
        print("Invalid Expense Amount")
        menu()
        return

    ID += 1
    transaction_ID = ID

    expenses.append({
        "Tracker ID": transaction_ID,
        "Category": value,
        "Name": expense_name,
        "Amount": expense_amt
    })

    print()
    print("Expense is Added Successfully!")
    print()

    menu()


def view_expense():
    print()

    if len(expenses) == 0:
        print("No Expenses Recorded")
        menu()
        return

    for expense in expenses:

        print(f"""
----------------------------------

Category       : {expense["Category"]}
Expense        : {expense["Name"]}
Amount         : ₹{expense["Amount"]}
Transaction ID : {expense["Tracker ID"]}

----------------------------------
""")

    menu()


def search_expense():
    print("""
========== SEARCH BY ==========

1. Category
2. Name
3. Amount
4. ID
5. RETURN TO MENU

===============================
""")

    user_response = int(input("Choose Option : "))

    if user_response == 1:

        value = category()

        if value is None:
            search_expense()
            return

        found = False

        for expense in expenses:

            if expense["Category"] == value:

                found = True

                print(f"""
----------------------------------

Category       : {expense["Category"]}
Expense        : {expense["Name"]}
Amount         : ₹{expense["Amount"]}
Transaction ID : {expense["Tracker ID"]}

----------------------------------
""")

        if not found:
            print("No Expenses in Category")

        menu()

    elif user_response == 2:

        search = input("Expense Name : ")

        found = False

        for expense in expenses:

            if search.lower() in expense["Name"].lower():

                found = True

                print(f"""
----------------------------------

Category       : {expense["Category"]}
Expense        : {expense["Name"]}
Amount         : ₹{expense["Amount"]}
Transaction ID : {expense["Tracker ID"]}

----------------------------------
""")

        if not found:
            print("No Expense Record Found")

        menu()

    elif user_response == 3:

        print("Enter the Range")

        minimum = int(input("Minimum Amount : "))
        maximum = int(input("Maximum Amount : "))

        if minimum > maximum:
            print("Invalid Range")
            print("Minimum amount cannot be greater than maximum amount.")
            menu()
            return

        found = False

        for expense in expenses:

            if minimum <= expense["Amount"] <= maximum:

                found = True

                print(f"""
----------------------------------

Category       : {expense["Category"]}
Expense        : {expense["Name"]}
Amount         : ₹{expense["Amount"]}
Transaction ID : {expense["Tracker ID"]}

----------------------------------
""")

        if not found:
            print("No Expense Found")

        menu()

    elif user_response == 4:

        transaction_ID = int(input("Enter the ID : "))

        found = False

        for expense in expenses:

            if expense["Tracker ID"] == transaction_ID:

                found = True

                print(f"""
----------------------------------

Category       : {expense["Category"]}
Expense        : {expense["Name"]}
Amount         : ₹{expense["Amount"]}
Transaction ID : {expense["Tracker ID"]}

----------------------------------
""")

                break

        if not found:
            print("INVALID ID")

        menu()

    elif user_response == 5:

        menu()

    else:

        print("INVALID OPTION!")
        search_expense()


def monthly_summary():

    total, count, highest, lowest, category_totals = monthly_statistics(expenses)

    print("""
===================================
         MONTHLY SUMMARY
===================================
""")

    if count == 0:

        print("No Expenses Recorded")

        print("""
===================================
""")

        menu()
        return

    average = total / count

    highest_category = max(
        category_totals,
        key=category_totals.get
    )

    lowest_category = min(
        category_totals,
        key=category_totals.get
    )

    print(f"Total Spending             : ₹{total}")
    print(f"Total Transactions         : {count}")
    print(f"Average Expense            : ₹{average:.2f}")
    print(f"Highest Expense            : ₹{highest}")
    print(f"Lowest Expense             : ₹{lowest}")
    print()
    print(f"Highest Spending Category  : {highest_category}")
    print(f"Category Spending          : ₹{category_totals[highest_category]}")
    print()
    print(f"Lowest Spending Category   : {lowest_category}")
    print(f"Category Spending          : ₹{category_totals[lowest_category]}")

    print("""
===================================
""")

    menu()


def menu():

    print("""
===================================
             SPENDWISE
===================================

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

===================================
""")

    user_response = int(input("Choose Option : "))

    if user_response == 1:
        add_expense()

    elif user_response == 2:
        view_expense()

    elif user_response == 3:
        search_expense()

    elif user_response == 4:
        monthly_summary()

    elif user_response == 5:
        print("Category Analysis")
        menu()

    elif user_response == 6:
        print("Budget Tracker")
        menu()

    elif user_response == 7:
        print("Savings Report")
        menu()

    elif user_response == 8:
        print("Edit Expense")
        menu()

    elif user_response == 9:
        print("Remove Expense")
        menu()

    elif user_response == 10:
        print()
        print("Exiting SpendWise. Goodbye!")

    else:
        print("INVALID RESPONSE")
        menu()


menu()