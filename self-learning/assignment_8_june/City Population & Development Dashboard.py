#Problem Statement
The government wants to analyze city data.
Store details of at least 30 cities.
Example Structure
cities = {
"Delhi": {
"population": 32000000,
"area": 1484,
"literacy": 89
}
}
Requirements
1. Display all city details.
2. Find the most populated city.
3. Find the least populated city.
4. Calculate average population.
5. Display cities with literacy rate above 90%.
6. Display cities with literacy below average.
7. Calculate population density.
8. Find city with highest density.
9. Categorize cities:
o Small
o Medium
o Large
10. Create a development-priority list.
11. Generate separate dictionaries for:
o High Literacy Cities
o Low Literacy Cities
12. Generate a national summary report.
Challenge
Rank all cities based on population density.
Assignment Rule (Important)
For all 5 Questions:
• Use at least 30 records.
• Do not use built-in sorting functions (sorted(), sort()).
• Use loops and conditions to find maximum, minimum, rankings, and reports.
• Display results in a structured format.
• Add a menu-driven interface using while loop.





# 1. Database containing exactly 30 cities
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 90},
    "Kolkata": {"population": 15000000, "area": 206, "literacy": 87},
    "Bangalore": {"population": 13000000, "area": 741, "literacy": 92},
    "Chennai": {"population": 12000000, "area": 426, "literacy": 90},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 83},
    "Ahmedabad": {"population": 8600000, "area": 505, "literacy": 89},
    "Pune": {"population": 7000000, "area": 331, "literacy": 91},
    "Surat": {"population": 6200000, "area": 462, "literacy": 88},
    "Jaipur": {"population": 4000000, "area": 467, "literacy": 76},
    "Lucknow": {"population": 3900000, "area": 349, "literacy": 84},
    "Kanpur": {"population": 3200000, "area": 260, "literacy": 83},
    "Nagpur": {"population": 2900000, "area": 228, "literacy": 92},
    "Indore": {"population": 3300000, "area": 276, "literacy": 87},
    "Thane": {"population": 2500000, "area": 147, "literacy": 91},
    "Bhopal": {"population": 2600000, "area": 285, "literacy": 85},
    "Visakhapatnam": {"population": 2300000, "area": 540, "literacy": 82},
    "Pimpri": {"population": 2000000, "area": 181, "literacy": 90},
    "Patna": {"population": 2500000, "area": 135, "literacy": 83},
    "Vadodara": {"population": 2200000, "area": 220, "literacy": 91},
    "Ghaziabad": {"population": 2400000, "area": 210, "literacy": 85},
    "Ludhiana": {"population": 1900000, "area": 159, "literacy": 82},
    "Agra": {"population": 1800000, "area": 121, "literacy": 73},
    "Nashik": {"population": 1700000, "area": 259, "literacy": 88},
    "Faridabad": {"population": 1500000, "area": 204, "literacy": 84},
    "Meerut": {"population": 1600000, "area": 141, "literacy": 78},
    "Rajkot": {"population": 1400000, "area": 170, "literacy": 86},
    "Kalyan": {"population": 1300000, "area": 137, "literacy": 93},
    "Vasai": {"population": 1200000, "area": 105, "literacy": 89},
    "Varanasi": {"population": 1400000, "area": 82, "literacy": 77}
}

# --- PRE-CALCULATIONS FOR THE DASHBOARD ---
total_pop = 0
total_lit = 0
for c in cities:
    total_pop += cities[c]["population"]
    total_lit += cities[c]["literacy"]

avg_pop = total_pop / len(cities)
avg_lit = total_lit / len(cities)

while True:
    print("\n" + "="*50)
    print("      CITY POPULATION & DEVELOPMENT DASHBOARD")
    print("="*50)
    print("1. Display All City Details")
    print("2. Find Most Populated City")
    print("3. Find Least Populated City")
    print("4. Calculate Average Population")
    print("5. Cities with Literacy Above 90%")
    print("6. Cities with Literacy Below Average")
    print("7. View Population Density for All Cities")
    print("8. Find City with Highest Density")
    print("9. Categorize Cities by Size")
    print("10. View Development Priority List")
    print("11. View High/Low Literacy Separate Dictionaries")
    print("12. Generate National Summary & Density Rank Challenge")
    print("13. Exit")
    print("="*50)
    
    choice = input("Enter your choice (1-13): ")
    
    if choice == "1":
        print(f"\n{'City':<15}{'Population':<15}{'Area (sq km)':<15}{'Literacy %':<10}")
        print("-" * 55)
        for city, info in cities.items():
            print(f"{city:<15}{info['population']:<15}{info['area']:<15}{info['literacy']:<10}")
            
    elif choice == "2":
        max_p = -1
        top_city = ""
        for city, info in cities.items():
            if info["population"] > max_p:
                max_p = info["population"]
                top_city = city
        print(f"\nMost Populated City: {top_city} ({max_p} citizens)")
        
    elif choice == "3":
        min_p = 999999999
        lowest_city = ""
        for city, info in cities.items():
            if info["population"] < min_p:
                min_p = info["population"]
                lowest_city = city
        print(f"\nLeast Populated City: {lowest_city} ({min_p} citizens)")
        
    elif choice == "4":
        print(f"\nAverage City Population: {avg_pop:.2f}")
        
    elif choice == "5":
        print("\nCities with Literacy Rate Above 90%:")
        for city, info in cities.items():
            if info["literacy"] > 90:
                print(f"* {city} ({info['literacy']}%)")
                
    elif choice == "6":
        print(f"\nCities with Literacy Below Average ({avg_lit:.2f}%):")
        for city, info in cities.items():
            if info["literacy"] < avg_lit:
                print(f"* {city} ({info['literacy']}%)")
                
    elif choice == "7":
        print(f"\n{'City':<15}{'Population Density (per sq km)':<30}")
        print("-" * 45)
        for city, info in cities.items():
            density = info["population"] / info["area"]
            print(f"{city:<15}{density:.2f}")
            
    elif choice == "8":
        max_density = -1
        dense_city = ""
        for city, info in cities.items():
            density = info["population"] / info["area"]
            if density > max_density:
                max_density = density
                dense_city = city
        print(f"\nCity with Highest Density: {dense_city} ({max_density:.2f} people/sq km)")
        
    elif choice == "9":
        print(f"\n{'City':<15}{'Category':<10}")
        print("-" * 30)
        for city, info in cities.items():
            if info["population"] >= 10000000:
                cat = "Large"
            elif info["population"] >= 3000000:
                cat = "Medium"
            else:
                cat = "Small"
            print(f"{city:<15}{cat:<10}")
            
    elif choice == "10":
        print("\n⚠️ DEVELOPMENT-PRIORITY LIST ⚠️")
        print("Criteria: Literacy below average AND High Population (> 2.5 million)")
        print("-" * 60)
        for city, info in cities.items():
            if info["literacy"] < avg_lit and info["population"] > 2500000:
                print(f"-> {city} [Urgent Intervention Required]")
                
    elif choice == "11":
        high_literacy_cities = {}
        low_literacy_cities = {}
        
        for city, info in cities.items():
            if info["literacy"] >= 85:
                high_literacy_cities[city] = info["literacy"]
            else:
                low_literacy_cities[city] = info["literacy"]
                
        print("\n--- High Literacy Cities Dct (>=85%) ---")
        print(high_literacy_cities)
        print("\n--- Low Literacy Cities Dict (<85%) ---")
        print(low_literacy_cities)
        
    elif choice == "12":
        print("\n================ NATIONAL SUMMARY REPORT ================")
        print(f"Total National Monitored Population : {total_pop}")
        print(f"Average City Literacy Rate         : {avg_lit:.2f}%")
        
        # Challenge: Rank all cities based on density using standard loops
        clist = []
        for city, info in cities.items():
            density = info["population"] / info["area"]
            clist.append([city, density])
            
        # Custom Manual Bubble Sort Loop
        n = len(clist)
        for i in range(n):
            for j in range(0, n-i-1):
                if clist[j][1] < clist[j+1][1]:
                    clist[j], clist[j+1] = clist[j+1], clist[j]
                    
        print("\n--- RANKING BY POPULATION DENSITY (Highest to Lowest) ---")
        print(f"{'Rank':<6}{'City':<15}{'Density':<15}")
        print("-" * 36)
        for rank in range(len(clist)):
            print(f"#{rank+1:<5}{clist[rank][0]:<15}{clist[rank][1]:.2f}")
            
    elif choice == "13":
        print("\nExiting Dashboard. Have a great day!")
        break
    else:
        print("\nInvalid option! Please enter a number from 1 to 13.")
