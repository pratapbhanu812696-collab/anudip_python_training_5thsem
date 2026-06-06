# List of products and their prices
orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Part 1: Display products costing more than 1000
print("Products costing more than ₹1000:")
for product in orders:
    if product[1] > 1000:
        print(product[0])

# Part 2: Find the most expensive product
max_product = orders[0]

for product in orders:
    if product[1] > max_product[1]:
        max_product = product

print("\nMost Expensive Product:", max_product[0], "-", max_product[1])

# Part 3: Calculate total order value
total = 0

for product in orders:
    total += product[1]

print("Total Order Value =", total)

# Part 4: Count products costing below 1000
count = 0

for product in orders:
    if product[1] < 1000:
        count += 1

print("Products below ₹1000 =", count)
