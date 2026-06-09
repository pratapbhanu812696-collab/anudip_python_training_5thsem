# ------------------------------------------
# Username Generator System
# ------------------------------------------

name = "Rahul Sharma"

print("Original Name =", name)

# Task 1 & 2
username = name.replace(" ", "").lower()

# Task 3
username = username + "2026"

print("Generated Username =", username)

# Task 4
if len(username) > 12:
    short_username = username[:12]
    print("First 12 Characters =", short_username)

# Task 5 & 6
vowels = 0
consonants = 0

for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Username Length =", len(username))
print("Vowels =", vowels)
print("Consonants =", consonants)

# Task 7
print("Status : Username Generated Successfully")# ------------------------------------------
# Username Generator System
# ------------------------------------------

name = "Rahul Sharma"

print("Original Name =", name)

# Task 1 & 2
username = name.replace(" ", "").lower()

# Task 3
username = username + "2026"

print("Generated Username =", username)

# Task 4
if len(username) > 12:
    short_username = username[:12]
    print("First 12 Characters =", short_username)

# Task 5 & 6
vowels = 0
consonants = 0

for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Username Length =", len(username))
print("Vowels =", vowels)
print("Consonants =", consonants)

# Task 7
print("Status : Username Generated Successfully")
