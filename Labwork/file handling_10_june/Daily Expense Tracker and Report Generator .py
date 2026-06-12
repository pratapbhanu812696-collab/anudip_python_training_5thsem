'''Daily Expense Tracker and Report Generator 
Problem Statement 
Daily expenses are recorded in expenses.txt. 
File Format 
Food,450 
Travel,300 
Shopping,1200 
Electricity,850 
Internet,700 
Entertainment,600 
Medicine,400 
Education,1500 
Fuel,900 
Miscellaneous,250 
Requirements 
Develop a program to: 
1. Display all expenses.  
2. Calculate total expenditure.  
3. Find the category with highest and lowest spending.  
4. Display expenses greater than ₹800.  
5. Add a new expense category.  
6. Update an existing expense amount.  
7. Generate a summary report in report.txt containing:  
o Total Expenses  
o Highest Expense Category  
o Lowest Expense Category  
o Categories spending more than ₹800 '''


# ---------------------------------------------------------
# DAILY EXPENSE TRACKER AND REPORT GENERATOR
# ---------------------------------------------------------
# Functions:
# 1. Display all expenses
# 2. Calculate total expenditure
# 3. Find highest and lowest expense category
# 4. Display expenses greater than ₹800
# 5. Add a new expense category
# 6. Update an existing expense amount
# 7. Generate summary report in report.txt
# ---------------------------------------------------------

FILE_NAME = "expenses.txt"


# Function to load expenses from file
def load_expenses():

    expenses = []

    file = open(FILE_NAME, "r")

    for line in file:

        data = line.strip().split(",")

        expense = {
            "category": data[0],
            "amount": int(data[1])
        }

        expenses.append(expense)

    file.close()

    return expenses


# Function to save expenses into file
def save_expenses(expenses):

    file = open(FILE_NAME, "w")

    for expense in expenses:

        line = expense["category"],",",str(expense["amount"]) + "\n"

        file.write(line)

    file.close()


# Function to display all expenses
def display_expenses():

    expenses = load_expenses()

    print("\nALL EXPENSES")
    print("-" * 40)

    for expense in expenses:

        print(expense["category"], expense["amount"])


# Function to calculate total expenditure
def total_expenditure():

    expenses = load_expenses()

    total = 0

    for expense in expenses:

        total += expense["amount"]

    print("Total Expenditure = ₹", total)


# Function to find highest and lowest spending category
def highest_lowest_expense():

    expenses = load_expenses()

    highest = expenses[0]
    lowest = expenses[0]

    for expense in expenses:

        if expense["amount"] > highest["amount"]:
            highest = expense

        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("\nHighest Expense Category")
    print(highest["category"], "₹", highest["amount"])

    print("\nLowest Expense Category")
    print(lowest["category"], "₹", lowest["amount"])


# Function to display expenses greater than ₹800
def expenses_above_800():

    expenses = load_expenses()

    print("\nEXPENSES GREATER THAN ₹800")
    print("-" * 40)

    for expense in expenses:

        if expense["amount"] > 800:

            print(expense["category"], "₹", expense["amount"])


# Function to add a new expense category
def add_expense():

    expenses = load_expenses()

    category = input("Enter Category Name: ")
    amount = int(input("Enter Amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense Added Successfully.")


# Function to update expense amount
def update_expense():

    expenses = load_expenses()

    category = input("Enter Category Name to Update: ")

    found = False

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            new_amount = int(input("Enter New Amount: "))

            expense["amount"] = new_amount

            save_expenses(expenses)

            print("Expense Updated Successfully.")

            found = True
            break

    if not found:
        print("Category not found.")


# Function to generate summary report
def generate_report():

    expenses = load_expenses()

    total = 0

    highest = expenses[0]
    lowest = expenses[0]

    high_spending = []

    for expense in expenses:

        total += expense["amount"]

        if expense["amount"] > highest["amount"]:
            highest = expense

        if expense["amount"] < lowest["amount"]:
            lowest = expense

        if expense["amount"] > 800:
            high_spending.append(expense)

    file = open("report.txt", "w")

    file.write("DAILY EXPENSE SUMMARY REPORT\n")
    file.write("-" * 35 + "\n")

    file.write("Total Expenses = ₹",str(total),"\n\n")

    file.write("Highest Expense Category:\n")
    file.write(highest["category"]," ₹",str(highest["amount"]),"\n\n")

    file.write("Lowest Expense Category:\n")
    file.write(lowest["category"]," ₹" ,str(lowest["amount"]),"\n\n")

    file.write("Categories Spending More Than ₹800:\n")

    for expense in high_spending:

        file.write(expense["category"]," ₹",str(expense["amount"]),"\n")

    file.close()

    print("Report Generated Successfully in report.txt")


# ---------------- MAIN MENU ---------------- #

while True:

    print("\n===== DAILY EXPENSE TRACKER =====")
    print("1. Display All Expenses")
    print("2. Calculate Total Expenditure")
    print("3. Find Highest and Lowest Expense")
    print("4. Display Expenses Greater Than ₹800")
    print("5. Add New Expense Category")
    print("6. Update Expense Amount")
    print("7. Generate Summary Report")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_expenses()

    elif choice == "2":
        total_expenditure()

    elif choice == "3":
        highest_lowest_expense()

    elif choice == "4":
        expenses_above_800()

    elif choice == "5":
        add_expense()

    elif choice == "6":
        update_expense()

    elif choice == "7":
        generate_report()

    elif choice == "8":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
