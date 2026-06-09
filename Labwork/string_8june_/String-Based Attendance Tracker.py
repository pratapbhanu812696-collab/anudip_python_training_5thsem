# ------------------------------------------
# String-Based Attendance Tracker
# ------------------------------------------

attendance = "PPAPPPAAPPPPAPP"

print("Attendance Record =", attendance)

# Task 1
present = 0
absent = 0

for ch in attendance:

    if ch == "P":
        present += 1
    else:
        absent += 1

print("Present Days =", present)
print("Absent Days =", absent)

# Task 2
percentage = (present / len(attendance)) * 100

print("Attendance Percentage =", percentage)

# Task 3: Longest Present Streak
current = 0
longest_present = 0

for ch in attendance:

    if ch == "P":
        current += 1

        if current > longest_present:
            longest_present = current

    else:
        current = 0

print("Longest Present Streak =", longest_present)

# Task 4: Longest Absent Streak
current = 0
longest_absent = 0

for ch in attendance:

    if ch == "A":
        current += 1

        if current > longest_absent:
            longest_absent = current

    else:
        current = 0

print("Longest Absent Streak =", longest_absent)

# Task 5
if percentage < 75:
    print("Attendance Status : Below 75%")
else:
    print("Attendance Status : Above 75%")
