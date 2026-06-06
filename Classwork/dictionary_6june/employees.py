# ------------------------------------------
# Program: Employee Salary Record Using Dictionary
# Objective:
# Create a dictionary of 10 employees where
# Employee ID is the key and Salary is the value.
# Find:
# 1. Total employees having salary greater than 30000.
# 2. Employee IDs whose salary is below 20000.
# ------------------------------------------

# Create an empty dictionary
employees = {}

# Input records of 10 employees
for i in range(10):
    emp_id = int(input("Enter Employee ID: "))
    salary = int(input("Enter Salary: "))

    employees[emp_id] = salary

# Count employees having salary greater than 30000
count = 0

for emp_id in employees:
    if employees[emp_id] > 30000:
        count += 1

print("\nTotal Employees having salary greater than 30000 =", count)

# Display employee IDs having salary below 20000
print("\nEmployees having salary below 20000:")

for emp_id in employees:
    if employees[emp_id] < 20000:
        print(emp_id)
