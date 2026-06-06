# Attendance record
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Part 1: Count present and absent days
present = 0
absent = 0

for day in attendance:
    if day == 'P':
        present += 1
    else:
        absent += 1

print("Present Days =", present)
print("Absent Days =", absent)

# Part 2: Attendance percentage
percentage = (present / len(attendance)) * 100

print("Attendance Percentage =", percentage)

# Part 3: Check eligibility
if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")

# Part 4: Display absent positions
print("Absent on Days:")

for i in range(len(attendance)):
    if attendance[i] == 'A':
        print(i + 1)
