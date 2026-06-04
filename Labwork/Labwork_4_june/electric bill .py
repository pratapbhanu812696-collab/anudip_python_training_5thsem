# Electricity Bill Calculator
number_of_units = float(input("Enter the number of units consumed: "))
rate_per_unit = 0.0
if number_of_units <= 100:
    rate_per_unit = 0.5
elif number_of_units <= 200:
    rate_per_unit = 0.75
elif number_of_units <= 300:
    rate_per_unit = 1.20
else:
    rate_per_unit = 1.50
total_bill = number_of_units * rate_per_unit
print(f"Total electricity bill: ${total_bill:.2f}")


