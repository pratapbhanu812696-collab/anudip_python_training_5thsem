# Product quality data
products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# Part 1: Display failed product IDs
print("Failed Product IDs:")

for product in products:
    if product[1] == "Fail":
        print(product[0])

# Part 2: Count passed and failed products
passed = 0
failed = 0

for product in products:
    if product[1] == "Pass":
        passed += 1
    else:
        failed += 1

print("Passed =", passed)
print("Failed =", failed)

# Part 3: Pass percentage
percentage = (passed / len(products)) * 100

print("Pass Percentage =", percentage)

# Part 4: Stop if 3 failures found
fail_count = 0

for product in products:
    if product[1] == "Fail":
        fail_count += 1

    if fail_count == 3:
        print("3 Failures Found")
        break
