# ---------------------------------------------------------
# CONTACT MANAGEMENT SYSTEM
# ---------------------------------------------------------
# Functions:
# 1. Display all contacts
# 2. Search contact by name
# 3. Add new contact
# 4. Update contact number
# 5. Delete contact
# 6. Display contacts starting with a vowel
# 7. Save all modifications to contacts.txt
# ---------------------------------------------------------

FILE_NAME = "contacts.txt"


# Function to load contacts from file
def load_contacts():

    contacts = []

    file = open(FILE_NAME, "r")

    for line in file:

        data = line.strip().split(",")

        contact = {
            "name": data[0],
            "number": data[1]
        }

        contacts.append(contact)

    file.close()

    return contacts


# Function to save contacts into file
def save_contacts(contacts):

    file = open(FILE_NAME, "w")

    for contact in contacts:

        line = contact["name"],",",contact["number"],"\n"

        file.write(line)

    file.close()


# Function to display all contacts
def display_contacts():

    contacts = load_contacts()

    print("\nALL CONTACTS")
    print("-" * 30)

    for contact in contacts:

        print(contact["name"], contact["number"])


# Function to search contact by name
def search_contact():

    contacts = load_contacts()

    name = input("Enter Contact Name: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            print("\nContact Found")
            print("Name:", contact["name"])
            print("Number:", contact["number"])

            found = True
            break

    if not found:
        print("Contact not found.")


# Function to add a new contact
def add_contact():

    contacts = load_contacts()

    name = input("Enter Name: ")
    number = input("Enter Mobile Number: ")

    contact = {
        "name": name,
        "number": number
    }

    contacts.append(contact)

    save_contacts(contacts)

    print("Contact Added Successfully.")


# Function to update contact number
def update_contact():

    contacts = load_contacts()

    name = input("Enter Contact Name to Update: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            new_number = input("Enter New Number: ")

            contact["number"] = new_number

            save_contacts(contacts)

            print("Contact Updated Successfully.")

            found = True
            break

    if not found:
        print("Contact not found.")


# Function to delete a contact
def delete_contact():

    contacts = load_contacts()

    name = input("Enter Contact Name to Delete: ")

    found = False

    for contact in contacts:

        if contact["name"].lower() == name.lower():

            contacts.remove(contact)

            save_contacts(contacts)

            print("Contact Deleted Successfully.")

            found = True
            break

    if not found:
        print("Contact not found.")


# Function to display contacts starting with vowels
def vowel_contacts():

    contacts = load_contacts()

    print("\nCONTACTS STARTING WITH VOWELS")
    print("-" * 30)

    vowels = "AEIOUaeiou"

    found = False

    for contact in contacts:

        if contact["name"][0] in vowels:

            print(contact["name"], contact["number"])

            found = True

    if not found:
        print("No contacts found.")


# ---------------- MAIN MENU ---------------- #

while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add New Contact")
    print("4. Update Contact Number")
    print("5. Delete Contact")
    print("6. Display Contacts Starting With Vowel")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_contacts()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        add_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        vowel_contacts()

    elif choice == "7":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
