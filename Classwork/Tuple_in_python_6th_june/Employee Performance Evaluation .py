employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)


print("Employees Scoring 80 or Above:")
for emp in employees:
    if emp[2] >= 80:
        print(emp[0], emp[1], emp[2])
        

improvement = 0

highest = employees[0]

high_performers = []

print("\nPerformance Categories:")
for emp in employees:
    score = emp[2]

    if score < 60:
        improvement += 1

    if score > highest[2]:
        highest = emp

    if score > 75:
        high_performers.append(emp[1])

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)

print("\nEmployees Needing Improvement:", improvement)

print("\nHighest Performer:")
print(highest[0], highest[1], highest[2])

print("\nHigh Performers:")
print(high_performers)
