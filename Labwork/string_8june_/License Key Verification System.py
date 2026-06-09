# ------------------------------------------
# License Key Verification System
# ------------------------------------------

key = "ABCD-EFGH-IJKL-MNOP"

print("License Key =", key)

# Task 1 & 2
groups = key.split("-")

print("Groups =", groups)

valid = True

if len(groups) != 4:
    valid = False

for group in groups:

    if len(group) != 4:
        valid = False

# Task 3
letters = 0

for ch in key:

    if ch.isalpha():
        letters += 1

print("Total Letters =", letters)

# Task 4
vowels = 0

for ch in key:

    if ch in "AEIOUaeiou":
        vowels += 1

print("Total Vowels =", vowels)

# Task 5
merged = key.replace("-", "")

print("Merged Key =", merged)

# Task 6
print("Group List =", groups)

# Task 7
if valid:
    print("License Key Status : Valid")
else:
    print("License Key Status : Invalid")
