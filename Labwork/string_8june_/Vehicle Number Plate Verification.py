# ------------------------------------------
# Vehicle Number Plate Verification
# ------------------------------------------

vehicle = "MH12AB4589"

# Task 1: Extract state code
state = vehicle[:2]

# Task 2: Extract district code
district = vehicle[2:4]

# Task 3: Extract series
series = vehicle[4:6]

# Task 4: Extract vehicle number
number = vehicle[6:]

print("State Code =", state)
print("District Code =", district)
print("Series =", series)
print("Vehicle Number =", number)

# Task 5: Count letters and digits
letters = 0
digits = 0

for ch in vehicle:

    if ch.isalpha():
        letters += 1

    elif ch.isdigit():
        digits += 1

print("Total Letters =", letters)
print("Total Digits =", digits)

# Task 6: Verify format
valid = True

if not vehicle[:2].isalpha():
    valid = False

if not vehicle[2:4].isdigit():
    valid = False

if not vehicle[4:6].isalpha():
    valid = False

if not vehicle[6:].isdigit():
    valid = False

# Task 7: Display status
if valid:
    print("Vehicle Number Status : Valid")
else:
    print("Vehicle Number Status : Invalid")
