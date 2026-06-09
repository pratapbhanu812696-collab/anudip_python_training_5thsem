#Employee Salary Processing

salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Task 1: Employees earning above 60000
print("Employees earning above 60000:")

for emp in salary:
    if salary[emp] > 60000:
        print(emp)

# Task 2: Count employees earning below 40000
count = 0

for emp in salary:
    if salary[emp] < 40000:
        count += 1

print("Employees earning below 40000 =", count)

# Task 3: Highest-paid employee
highest = max(salary, key=salary.get)

print("Highest Paid Employee =", highest)

# Task 4: Employees eligible for bonus
bonus = []

for emp in salary:
    if salary[emp] > 50000:
        bonus.append(emp)

print("Bonus Eligible Employees =", bonus)

# Task 5: Average salary
total = 0

for emp in salary:
    total += salary[emp]

average = total / len(salary)

print("Average Salary =", average)
