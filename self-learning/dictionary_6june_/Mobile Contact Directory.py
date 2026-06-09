# Mobile Contact Directory

contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Task 1: Display contact names in alphabetical order
names = list(contacts.keys())
names.sort()

print("Contacts in Alphabetical Order:")
for name in names:
    print(name)

# Task 2: Count total contacts
count = 0

for name in contacts:
    count += 1

print("Total Contacts =", count)

# Task 3 and 5: Search contact using break
search = input("Enter Contact Name: ")

for name in contacts:
    if name == search:
        print("Contact Found:", contacts[name])
        break

# Task 4: Names starting with vowel
vowel_names = []

for name in contacts:
    if name[0] in "AEIOUaeiou":
        vowel_names.append(name)

print("Names Starting with Vowel =", vowel_names)
