# Food Delivery performance Tracker
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]
#1. fastest_delivery(times)
def fastest_delivery(times):
    return min(times)
print(f"Fastest Delivery: {fastest_delivery(delivery_time)} minutes")

#2.delayed_orders(times)
def delayed_orders(times):
    delayed = []
    for t in times:
        if t > 45:
            delayed.append(t)
    return delayed
print(f"Delayed Orders:\n{delayed_orders(delivery_time)}")

#3.average_delivery_time(times)
def average_delivery_time(times):
    total_time = sum(times)
    total_orders = len(times)
    return total_time / total_orders
print(f"Average Delivery Time:\n{average_delivery_time(delivery_time)} minutes")

#4.delivery_category(times)
def delivery_category(times):
    print("Categories:")
    for t in times:
        if t <= 30:
            category = "Fast"
        elif t <= 45:
            category = "Normal"
        else:
            category = "Delayed"
        print(f"{t} -> {category}")
        delivery_cate
