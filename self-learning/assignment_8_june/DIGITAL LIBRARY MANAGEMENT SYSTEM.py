# ==========================================
# DIGITAL LIBRARY MANAGEMENT SYSTEM
# ==========================================

# Empty dictionary to store book details
library = {}

# ------------------------------------------
# Enter details of 30 books
# ------------------------------------------

for i in range(1, 31):

    print(f"\nEnter Details of Book {i}")

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter Available Copies: "))

    library[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }

# ==========================================
# 1. ADD A BOOK
# ==========================================

book_id = input("\nEnter New Book ID: ")

title = input("Enter Title: ")
author = input("Enter Author: ")
copies = int(input("Enter Copies: "))

library[book_id] = {
    "title": title,
    "author": author,
    "copies": copies
}

print("Book Added Successfully")

# ==========================================
# 2. REMOVE A BOOK
# ==========================================

book_id = input("\nEnter Book ID To Remove: ")

if book_id in library:
    del library[book_id]
    print("Book Removed Successfully")
else:
    print("Book Not Found")

# ==========================================
# 3. SEARCH BOOK BY ID
# ==========================================

book_id = input("\nEnter Book ID To Search: ")

if book_id in library:
    print("Book Found")
    print(library[book_id])
else:
    print("Book Not Found")

# ==========================================
# 4. SEARCH BOOK BY TITLE
# ==========================================

title = input("\nEnter Book Title To Search: ")

for book_id, details in library.items():

    if details["title"] == title:
        print("Book Found")
        print(book_id,
              details["title"],
              details["author"],
              details["copies"])
        break

else:
    print("Book Not Found")

# ==========================================
# 5. UPDATE AVAILABLE COPIES
# ==========================================

book_id = input("\nEnter Book ID: ")

if book_id in library:

    new_copies = int(input("Enter New Number Of Copies: "))

    library[book_id]["copies"] = new_copies

    print("Copies Updated Successfully")

else:
    print("Book Not Found")

# ==========================================
# 6. ISSUE A BOOK
# ==========================================

book_id = input("\nEnter Book ID To Issue: ")

if book_id in library:

    if library[book_id]["copies"] > 0:

        library[book_id]["copies"] -= 1

        print("Book Issued Successfully")

    else:

        print("Book Currently Unavailable")

else:

    print("Book Not Found")

# ==========================================
# 7. RETURN A BOOK
# ==========================================

book_id = input("\nEnter Book ID To Return: ")

if book_id in library:

    library[book_id]["copies"] += 1

    print("Book Returned Successfully")

else:

    print("Book Not Found")

# ==========================================
# 8. DISPLAY BOOKS WITH FEWER THAN 3 COPIES
# ==========================================

print("\nBOOKS WITH FEWER THAN 3 COPIES")

for book_id, details in library.items():

    if details["copies"] < 3:

        print(book_id,
              details["title"],
              details["author"],
              details["copies"])

# ==========================================
# 9. DISPLAY UNAVAILABLE BOOKS
# ==========================================

print("\nUNAVAILABLE BOOKS")

for book_id, details in library.items():

    if details["copies"] == 0:

        print(book_id,
              details["title"],
              details["author"])

# ==========================================
# 10. FIND MOST AVAILABLE BOOK
# ==========================================

copies_list = []

for details in library.values():

    copies_list.append(details["copies"])

max_copies = max(copies_list)

print("\nMOST AVAILABLE BOOK")

for book_id, details in library.items():

    if details["copies"] == max_copies:

        print(book_id,
              details["title"],
              details["author"],
              details["copies"])

# ==========================================
# 11. GENERATE RESTOCKING REPORT
# ==========================================

print("\nRESTOCKING REPORT")

for book_id, details in library.items():

    if details["copies"] < 3:

        print(book_id,
              details["title"],
              details["copies"])

# ==========================================
# 12. CREATE DICTIONARY OF BOOKS REQUIRING
#     IMMEDIATE PURCHASE (COPIES = 0)
# ==========================================

purchase_books = {}

for book_id, details in library.items():

    if details["copies"] == 0:

        purchase_books[book_id] = details

print("\nBOOKS REQUIRING IMMEDIATE PURCHASE")

for book_id, details in purchase_books.items():

    print(book_id,
          details["title"],
          details["author"],
          details["copies"])

# ==========================================
# DISPLAY COMPLETE LIBRARY
# ==========================================

print("\nCOMPLETE LIBRARY RECORD")

for book_id, details in library.items():

    print(book_id,
          details["title"],
          details["author"],
          details["copies"])
