# Sample Data
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# Variables to store results for Tasks 2, 3, 4, and 5
needs_improvement_count = 0
highest_score = -1
highest_performer = None
high_performers_list = []
categories_output = []

print("Employees Scoring 80 or Above:")
# Loop through the data to process all tasks
for emp_id, name, score in employees:
    
    # Task 1: Display details of employees scoring 80 or above
    if score >= 80:
        print(f"{emp_id} {name} {score}")
        
    # Task 2: Count employees needing improvement (score below 60)
    if score < 60:
        needs_improvement_count += 1
        
    # Task 3: Find the employee with the highest score
    if score > highest_score:
        highest_score = score
        highest_performer = (emp_id, name, score)
        
    # Task 4: Create a list of names scoring above 75
    if score > 75:
        high_performers_list.append(name)
        
    # Task 5: Determine performance category
    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    
    categories_output.append(f"{name} -> {category}")

print("-" * 30) # Separator for neatness

# Task 2 Output
print(f"Employees Needing Improvement: {needs_improvement_count}")

# Task 3 Output
print("Highest Performer:")
if highest_performer:
    print(f"{highest_performer[0]} {highest_performer[1]} {highest_performer[2]}")

# Task 4 Output
print("High Performers:")
print(high_performers_list)

# Task 5 Output
print("Performance Categories:")
for record in categories_output:
    print(record)
