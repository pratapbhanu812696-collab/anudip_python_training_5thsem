# Inventory Management System

inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Task 1: Products with stock less than 10
print("Products with stock less than 10:")

for item in inventory:
    if inventory[item] < 10:
        print(item)

# Task 2: Count products having stock more than 50
count = 0

for item in inventory:
    if inventory[item] > 50:
        count += 1

print("Products with stock more than 50 =", count)

# Task 3: Product with minimum stock
minimum = min(inventory, key=inventory.get)

print("Product with minimum stock =", minimum)

# Task 4: Products requiring restocking
restock = []

for item in inventory:
    if inventory[item] < 20:
        restock.append(item)

print("Restocking Required =", restock)

# Task 5: Total inventory count
total = 0

for item in inventory:
    total += inventory[item]

print("Total Inventory Count =", total)
