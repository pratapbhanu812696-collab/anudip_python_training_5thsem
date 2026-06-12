'''Employee Payroll Management System 
Problem Statement 
A company stores employee details in a text file named employees.txt. 
File Format 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Requirements 
Create a menu-driven program to: 
1. Display all employee records.  
2. Search employee details using Employee ID.  
3. Calculate the average salary.  
4. Find the highest-paid and lowest-paid employee.  
5. Display employees earning above ₹50,000.  
6. Add a new employee record to the file.  
7. Generate salary categories:  
o High (₹60,000 and above)  
o Medium (₹40,000–₹59,999)  
o Low (Below ₹40,000) '''

# Employee Payroll Management System

FILE_NAME = "employees.txt"


# Function to load employee records from file
def load_employees():

    employees = []

    file = open(FILE_NAME, "r")

    for line in file:

        data = line.strip().split(",")

        employee = {
            "id": data[0],
            "name": data[1],
            "salary": int(data[2])
        }

        employees.append(employee)

    file.close()

    return employees


# Function to display all employee records
def display_employees():

    employees = load_employees()

    print("\nEmployee Records")
    print("-" * 40)

    for emp in employees:
        print(emp["id"], emp["name"], emp["salary"])


# Function to search employee by ID
def search_employee():

    emp_id = input("Enter Employee ID: ")

    employees = load_employees()

    found = False

    for emp in employees:

        if emp["id"] == emp_id:

            print("\nEmployee Found")
            print("ID:", emp["id"])
            print("Name:", emp["name"])
            print("Salary:", emp["salary"])

            found = True
            break

    if not found:
        print("Employee not found.")


# Function to calculate average salary
def average_salary():

    employees = load_employees()

    total_salary = 0

    for emp in employees:
        total_salary += emp["salary"]

    avg = total_salary / len(employees)

    print("Average Salary =", avg)


# Function to find highest and lowest paid employee
def highest_lowest_salary():

    employees = load_employees()

    highest = employees[0]
    lowest = employees[0]

    for emp in employees:

        if emp["salary"] > highest["salary"]:
            highest = emp

        if emp["salary"] < lowest["salary"]:
            lowest = emp

    print("\nHighest Paid Employee")
    print(highest["id"], highest["name"], highest["salary"])

    print("\nLowest Paid Employee")
    print(lowest["id"], lowest["name"], lowest["salary"])


# Function to display employees earning above 50000
def employees_above_50000():

    employees = load_employees()

    print("\nEmployees Earning Above ₹50,000")
    print("-" * 40)

    for emp in employees:

        if emp["salary"] > 50000:
            print(emp["id"], emp["name"], emp["salary"])


# Function to add new employee
def add_employee():

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file = open(FILE_NAME, "a")

    file.write("\n",emp_id,",",name,",",salary)

    file.close()

    print("Employee Added Successfully.")


# Function to generate salary categories
def salary_categories():

    employees = load_employees()

    print("\nSalary Categories")
    print("-" * 40)

    print("\nHigh Salary Employees")
    for emp in employees:

        if emp["salary"] >= 60000:
            print(emp["id"], emp["name"], emp["salary"])

    print("\nMedium Salary Employees")
    for emp in employees:

        if 40000 <= emp["salary"] <= 59999:
            print(emp["id"], emp["name"], emp["salary"])

    print("\nLow Salary Employees")
    for emp in employees:

        if emp["salary"] < 40000:
            print(emp["id"], emp["name"], emp["salary"])


# Main Menu
while True:

    print("\n===== Employee Payroll Management System =====")
    print("1. Display All Employees")
    print("2. Search Employee by ID")
    print("3. Calculate Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above ₹50,000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_employees()

    elif choice == "2":
        search_employee()

    elif choice == "3":
        average_salary()

    elif choice == "4":
        highest_lowest_salary()

    elif choice == "5":
        employees_above_50000()

    elif choice == "6":
        add_employee()

    elif choice == "7":
        salary_categories()

    elif choice == "8":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
