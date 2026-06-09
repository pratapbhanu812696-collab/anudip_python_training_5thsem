performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Categorization lists and trackers
needs_improvement = 0
top_performer = ""
max_score = -1
total_score = 0

excellent = []
good = []
average = []
poor = []

print("Employees Scoring Above 80:")
for emp, score in performance.items():
    total_score += score
    
    # 1. Scores above 80
    if score > 80:
        print(emp)
        
    # 2. Count needs improvement
    if score < 60:
        needs_improvement += 1
        
    # 3. Top performer check
    if score > max_score:
        max_score = score
        top_performer = emp
        
    # 5. Grouping into categories
    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average.append(emp)
    else:
        poor.append(emp)

avg_score = total_score / len(performance)

print(f"\nTop Performer: {top_performer} ({max_score})")
print(f"Employees Needing Improvement: {needs_improvement}")
print(f"Average Score: {avg_score:.1f}")
print(f"Excellent: {excellent}")
print(f"Good: {good}")
print(f"Average: {average}")
print(f"Poor: {poor}")
