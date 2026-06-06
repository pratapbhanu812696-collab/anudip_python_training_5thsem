# Employee data
employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# Part 1: Employees earning above 50000
print("Employees earning above ₹50000:")

for emp in employees:
    if emp[1] > 50000:
        print(emp[0])

# Part 2: Highest-paid employee
highest = employees[0]

for emp in employees:
    if emp[1] > highest[1]:
        highest = emp

print("Highest Paid Employee =", highest[0])

# Part 3: Total salary expenditure
total_salary = 0

for emp in employees:
    total_salary += emp[1]

print("Total Salary Expenditure =", total_salary)

# Part 4: Count employees earning below 40000
count = 0

for emp in employees:
    if emp[1] < 40000:
        count += 1

print("Employees below ₹40000 =", count)
