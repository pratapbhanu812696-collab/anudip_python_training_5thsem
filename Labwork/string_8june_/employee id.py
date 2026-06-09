# Employee ID
emp_id = "EMP2026ANUJ458"

# Task 1: Count uppercase letters
upper = 0

# Task 2: Count digits
digits = 0

# Task 6: Create a list containing all digits
digit_list = []

# Task 7: Find the sum of all digits
digit_sum = 0

for ch in emp_id:
    if ch.isupper():
        upper += 1

    if ch.isdigit():
        digits += 1
        digit_list.append(int(ch))
        digit_sum += int(ch)

# Task 3: Extract the joining year
year = emp_id[3:7]

# Task 4: Extract the employee name
name = emp_id[7:-3]

# Task 5: Check whether the ID follows the required rules
valid = True

# Rule 1: Starts with "EMP"
if emp_id[:3] != "EMP":
    valid = False

# Rule 2: Contains exactly 4 digits for the year
if len(year) != 4 or not year.isdigit():
    valid = False

# Rule 3: Ends with exactly 3 digits
last_part = emp_id[-3:]

if len(last_part) != 3 or not last_part.isdigit():
    valid = False

# Display employee ID
print("Employee ID:", emp_id)
print()

# Display uppercase letters and digits count
print("Uppercase Letters:", upper)
print("Digits:", digits)
print()

# Display joining year and employee name
print("Joining Year:", year)
print("Employee Name:", name)
print()

# Display digit list and sum of digits
print("Digit List:", digit_list)
print("Sum of Digits:", digit_sum)
print()

# Task 8: Display whether the ID is valid or invalid
if valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")
