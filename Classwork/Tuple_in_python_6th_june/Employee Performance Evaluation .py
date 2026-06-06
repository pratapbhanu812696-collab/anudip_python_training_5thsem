#Employee Performance Evaluation using tuples
# Define a tuple to store employee performance data
employees = (
("E101", "Anuj", 92),
("E102", "Rahul", 76),
("E103", "Priya", 58),
("E104", "Neha", 88),
("E105", "Amit", 45)
)
#1.Display details of employees scoring 80 or above.
for emp in employees:
    if emp[2] >= 80:
        print(f"Employee ID: {emp[0]}, Name: {emp[1]}, Score: {emp[2]}")


#2.Count the number of employees who need improvement (score below 60)
improvement_count = sum(1 for emp in employees if emp[2] < 60)
print(f"Number of employees needing improvement: {improvement_count}")


#3.Find the employee with the highest score
highest_score_employee = max(employees, key=lambda emp: emp[2])
print(f"Employee with the highest score: {highest_score_employee[1]} (Score: {highest_score_employee[2]})")


#4.Create a list containing the names of all employees scoring above 75.
high_scorers = [emp[1] for emp in employees if emp[2] > 75]
print("Employees scoring above 75:", high_scorers)


#5.Display the performance category for each employee:
#90 and above → Excellent
# 75 to 89 → Good
# 60 to 74 → Average
# Below 60 → Needs Improvement
for emp in employees:
    if emp[2] >= 90:
        category = "Excellent"
    elif emp[2] >= 75:
        category = "Good"
    elif emp[2] >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    print(f"Employee ID: {emp[0]}, Name: {emp[1]}, Score: {emp[2]}, Performance Category: {category}")
    

