# Electricity Consumption Report

units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Task 1: Houses consuming more than 300 units
print("Houses consuming more than 300 units:")

for house in units:
    if units[house] > 300:
        print(house)

# Task 2: Count houses consuming less than 200 units
count = 0

for house in units:
    if units[house] < 200:
        count += 1

print("Houses consuming less than 200 units =", count)

# Task 3: House with highest consumption
max_house = ""
max_unit = 0

for house in units:
    if units[house] > max_unit:
        max_unit = units[house]
        max_house = house

print("Highest Consumption House =", max_house)

# Task 4: Houses eligible for awareness campaign
campaign = []

for house in units:
    if units[house] > 400:
        campaign.append(house)

print("Awareness Campaign Houses =", campaign)

# Task 5: Categorize houses
print("House Categories:")

for house in units:
    if units[house] < 200:
        category = "Low"
    elif units[house] <= 350:
        category = "Medium"
    else:
        category = "High"

    print(house, "-", category)
