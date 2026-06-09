# Library Book Availability

books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Task 1: Display unavailable books
print("Unavailable Books:")

for book in books:
    if books[book] == 0:
        print(book)

# Task 2: Count available books
count = 0

for book in books:
    if books[book] > 0:
        count += 1

print("Available Books =", count)

# Task 3: Book with maximum copies
max_book = ""
max_copies = 0

for book in books:
    if books[book] > max_copies:
        max_copies = books[book]
        max_book = book

print("Book with Maximum Copies =", max_book)

# Task 4: Books having less than 3 copies
low_books = []

for book in books:
    if books[book] < 3:
        low_books.append(book)

print("Books with less than 3 copies =", low_books)

# Task 5: Total number of books
total = 0

for book in books:
    total += books[book]

print("Total Books Available =", total)
