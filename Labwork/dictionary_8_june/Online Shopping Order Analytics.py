sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# Variables for tracking
best_product = ""
max_sales = -1
least_product = ""
min_sales = 99999
total_sold = 0
promo_required = []
between_10_30 = 0

print("Products Sold More Than 20 Times:")
for item, qty in sales.items():
    total_sold += qty  # Calculate total units
    
    # 1. Check sales > 20
    if qty > 20:
        print(item)
        
    # 2. Track best selling
    if qty > max_sales:
        max_sales = qty
        best_product = item
        
    # 3. Track least selling
    if qty < min_sales:
        min_sales = qty
        least_product = item
        
    # 5. Products requiring promotion
    if qty < 15:
        promo_required.append(item)
        
    # 6. Count between 10 and 30
    if 10 <= qty <= 30:
        between_10_30 += 1

print(f"\nBest Selling Product: {best_product} ({max_sales})")
print(f"Least Selling Product: {least_product} ({min_sales})")
print(f"Total Units Sold: {total_sold}")
print(f"Products Requiring Promotion: {promo_required}")
print(f"Products Having Sales Between 10 and 30: {between_10_30}")
