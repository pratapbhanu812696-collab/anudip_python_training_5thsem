# ------------------------------------------
# Email Address Validator
# ------------------------------------------

email = "rahul.sharma2026@gmail.com"

print("Email =", email)

# Task 1: Extract username
username = email.split("@")[0]
print("Username =", username)

# Task 2: Extract domain
domain = email.split("@")[1].split(".")[0]
print("Domain =", domain)

# Task 3: Extract extension
extension = email.split(".")[-1]
print("Extension =", extension)

# Task 4: Count digits in username
digit_count = 0

for ch in username:
    if ch.isdigit():
        digit_count += 1

print("Digits Found =", digit_count)

# Task 5: Count special characters
special_count = 0

for ch in email:
    if not ch.isalnum():
        special_count += 1

print("Special Characters Found =", special_count)

# Task 6: Validate email
valid = True

if email.count("@") != 1:
    valid = False

if "." not in email.split("@")[1]:
    valid = False

# Task 7: Display status
if valid:
    print("Email Status : Valid")
else:
    print("Email Status : Invalid")
