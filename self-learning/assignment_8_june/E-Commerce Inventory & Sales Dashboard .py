''' E-Commerce Inventory & Sales Dashboard 
Problem Statement 
An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10). '''


#creating blank dictionary
products={}
#taking details of 30 students
for i in range(30):

    product_id=input("enter the id of product")
    name=input("enter the name of the product")
    price=input("enter the price of the product ")
    stock=input("enter the stock of the product ")
    sold= input("enter sold no. of product")
    products[product_id]= {"name":name,"price":price, "stock": stock,"sold":sold}
print("------------------------------------------------")

#Task-1 To Display all student records.
print(products)

# Task-2 to Add a new product.
print("enter details of product to be added")
product_id = input("Enter product ID: ")
name = input("Enter Name: ")
price=input("price of product:")
stock=input("enter the stock available of the product:")
sold = int(input("Enter sold amount of the product: "))

products[product_id] ={
    "name":name,
    "price":price,
    "stock": stock,
    "sold":sold}

print("Product added successfully!")

#Task-3 to Update stock after sales
print("enter name of product to be updated after the sales")
product_id = input("Enter product ID: ")

if product_id in products:
    new_stock = int(input("Enter New stock available: "))
    new_sold=int(input("enter the sold amount"))
    products[product_id]["stock"] = new_stock
    products[product_id]["sold"] = new_sold
    print("Products details updated successfully!")
else:
    print("Product not found")


#Task-4 to Find out-of-stock products

for product_id, details in products.items():
    if details["stock"] == 0:
        print(product_id, details["name"], details["price"], details["sold"])

#task-5 to  Find products with stock less than 5

for product_id, details in products.items():
    if details["stock"] < 5:
        print(product_id, details["name"], details["price"], details["sold"])

#task-6 to Calculate total inventory value
total_inventory_value = 0

for details in products.values():
    total_inventory_value += (details["price"] * details["stock"])

print("Total Inventory Value:", total_inventory_value)

'''task-7/8 Find best-selling product / Find least-selling product.'''

sold_list = []

for product in products.values():
    sold_list.append(product["sold"])

best_selling = max(sold_list)
least_selling = min(sold_list)

for product_id, details in products.items():

    if details["sold"] == best_selling:
        print("\nBest Selling Product")
        print("ID   :", product_id)
        print("Name :", details["name"])
        print("Sold :", details["sold"])

    if details["sold"] == least_selling:
        print("\nLeast Selling Product")
        print("ID   :", product_id)
        print("Name :", details["name"])
        print("Sold :", details["sold"])


#task-9 to calculate total revenue
total_revenue = 0

for details in products.values():
    total_revenue += details["price"] * details["sold"]

print("Total Revenue Generated:", total_revenue)


#Task-10 Generate a low-stock report.
print("LOW STOCK REPORT")
print("----------------")

for product_id, details in products.items():

    if details["stock"] < 10:
        print("Product ID :", product_id)
        print("Name       :", details["name"])
        print("Price      :", details["price"])
        print("Stock      :", details["stock"])
        print("Sold       :", details["sold"])


#task-11 to Display products whose sales exceed the average sales.  
total_sales = 0

for details in products.values():
    total_sales += details["sold"]

average_sales = total_sales / len(products)

print("\nProducts with Sales Above Average:\n")

for product_id, details in products.items():

    if details["sold"] > average_sales:
        print(product_id, details["name"], details["sold"])

#task-12 to Create a dictionary of products eligible for promotion (sales < 10).

promotion_products = {}

for product_id, details in products.items():

    if details["sold"] < 10:
        promotion_products[product_id] = details

print("Products Eligible for Promotion:\n")

for product_id, details in promotion_products.items():
    print(product_id, details["name"], details["sold"])
