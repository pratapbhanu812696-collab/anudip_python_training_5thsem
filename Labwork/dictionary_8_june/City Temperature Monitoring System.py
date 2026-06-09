temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

hottest_city = ""
max_temp = -99
coolest_city = ""
min_temp = 99
total_temp = 0
pleasant_cities = []
between_35_40 = 0

print("Cities Above 40°C:")
for city, temp in temperature.items():
    total_temp += temp
    
    # 1. Cities above 40
    if temp > 40:
        print(city)
        
    # 2. Find hottest
    if temp > max_temp:
        max_temp = temp
        hottest_city = city
        
    # 3. Find coolest
    if temp < min_temp:
        min_temp = temp
        coolest_city = city
        
    # 5. Pleasant list
    if temp < 35:
        pleasant_cities.append(city)
        
    # 6. Count between 35 and 40
    if 35 <= temp <= 40:
        between_35_40 += 1

avg_temp = total_temp / len(temperature)

print(f"\nHottest City: {hottest_city} ({max_temp}°C)")
print(f"Coolest City: {coolest_city} ({min_temp}°C)")
print(f"Average Temperature: {avg_temp:.1f}°C")
print(f"Pleasant Cities: {pleasant_cities}")
print(f"Cities Between 35°C and 40°C: {between_35_40}")
