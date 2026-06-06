# Book data
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Part 1: Display unavailable books
print("Unavailable Books:")

for book in books:
    if book[1] == 0:
        print(book[0])

# Part 2: Books with more than 2 copies
print("Books with more than 2 copies:")

for book in books:
    if book[1] > 2:
        print(book[0])

# Part 3: Count available books
count = 0

for book in books:
    if book[1] > 0:
        count += 1

print("Available Books =", count)

# Part 4: Search for a book
search_book = input("Enter book name: ")

for book in books:
    if book[0] == search_book:
        print("Book Found")
        break
