# ---------------------------------------------------------
# LIBRARY BOOK ISSUE SYSTEM
# ---------------------------------------------------------

FILE_NAME = "books.txt"


# Function to load books from file
def load_books():

    books = []

    file = open(FILE_NAME, "r")

    for line in file:

        data = line.strip().split(",")

        book = {
            "id": data[0],
            "name": data[1],
            "copies": int(data[2])
        }

        books.append(book)

    file.close()

    return books


# Function to save updated books into file
def save_books(books):

    file = open(FILE_NAME, "w")

    for book in books:

        line = book["id"],",",book["name"],",",str(book["copies"]),"\n"

        file.write(line)

    file.close()


# Function to display all books
def display_books():

    books = load_books()

    print("\nALL BOOKS")
    print("-" * 40)

    for book in books:

        print(book["id"], book["name"], book["copies"])


# Function to search a book using Book ID
def search_book():

    books = load_books()

    book_id = input("Enter Book ID: ")

    found = False

    for book in books:

        if book["id"] == book_id:

            print("\nBook Found")
            print("ID:", book["id"])
            print("Name:", book["name"])
            print("Copies:", book["copies"])

            found = True
            break

    if not found:
        print("Book not found.")


# Function to issue a book
def book_issuing():

    books = load_books()

    book_id = input("Enter Book ID to issue: ")

    found = False

    for book in books:

        if book["id"] == book_id:

            found = True

            if book["copies"] > 0:

                book["copies"] -= 1

                save_books(books)

                print("\nBook Issued Successfully")
                print("Remaining Copies:", book["copies"])

            else:

                print("Book is unavailable.")

            break

    if not found:
        print("Book not found.")


# Function to return a book
def book_returned():

    books = load_books()

    book_id = input("Enter Book ID to return: ")

    found = False

    for book in books:

        if book["id"] == book_id:

            found = True

            book["copies"] += 1

            save_books(books)

            print("\nBook Returned Successfully")
            print("Available Copies:", book["copies"])

            break

    if not found:
        print("Book not found.")


# Function to display unavailable books
def unavailable_books():

    books = load_books()

    print("\nUNAVAILABLE BOOKS")
    print("-" * 40)

    found = False

    for book in books:

        if book["copies"] == 0:

            print(book["id"], book["name"], book["copies"])

            found = True

    if not found:
        print("No unavailable books.")


# Function to display books requiring restocking
def book_restocking():

    books = load_books()

    print("\nBOOKS REQUIRING RESTOCKING")
    print("-" * 40)

    found = False

    for book in books:

        if book["copies"] < 2:

            print(book["id"], book["name"], book["copies"])

            found = True

    if not found:
        print("No books require restocking.")


# ---------------- MAIN MENU ---------------- #

while True:

    print("\n===== LIBRARY BOOK ISSUE SYSTEM =====")
    print("1. Display All Books")
    print("2. Search Book by ID")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        book_issuing()

    elif choice == "4":
        book_returned()

    elif choice == "5":
        unavailable_books()

    elif choice == "6":
        book_restocking()

    elif choice == "7":

        print("Exiting Program...")
        break

    else:

        print("Invalid Choice. Try Again.")
