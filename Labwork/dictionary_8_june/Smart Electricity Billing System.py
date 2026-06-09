units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

highest_house = ""
max_units = -1
lowest_house = ""
min_units = 99999
total_units = 0
campaign_count = 0

low_consumption = []
medium_consumption = []
high_consumption = []

print("Houses Consuming More Than 400 Units:")
for house, consumed in units.items():
    total_units += consumed
    
    # 1. More than 400 units
    if consumed > 400:
        print(house)
        
    # 2. Highest consumer
    if consumed > max_units:
        max_units = consumed
        highest_house = house
        
    # 3. Lowest consumer
    if consumed < min_units:
        min_units = consumed
        lowest_house = house
        
    # 5. Categorization logic
    if consumed < 200:
        low_consumption.append(house)
    elif 200 <= consumed <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)
        
    # 6. Energy-saving campaign check
    if consumed > 300:
        campaign_count += 1

print(f"\nHighest Consumption: {highest_house} ({max_units} units)")
print(f"Lowest Consumption: {lowest_house} ({min_units} units)")
print(f"Total Units Consumed: {total_units}")
print(f"Low Consumption: {low_consumption}")
print(f"Medium Consumption: {medium_consumption}")
print(f"High Consumption: {high_consumption}")
print(f"Eligible for Energy-Saving Campaign: {campaign_count}")
