#Shopping Cart Bill
item_name = input("Enter the name of the item: ")
quantity = int(input("Enter the quantity: "))
price_per_item = float(input("Enter the price per item: "))
if quantity <= 0 or price_per_item <= 0:
    print("Invalid input! Quantity and price must be greater than 0.")
else:
    total_cost = quantity * price_per_item
    print(f"Total cost for {quantity} {item_name}(s) is: ${total_cost:.2f}")

