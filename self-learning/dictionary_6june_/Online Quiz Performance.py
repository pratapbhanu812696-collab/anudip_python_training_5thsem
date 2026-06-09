# Online Quiz Performance

quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Task 1: Students scoring 15 or above
print("Students scoring 15 or above:")

for student in quiz_scores:
    if quiz_scores[student] >= 15:
        print(student)

# Task 2: Count students scoring below 10
count = 0

for student in quiz_scores:
    if quiz_scores[student] < 10:
        count += 1

print("Students below 10 =", count)

# Task 3: Top performer
top_student = ""
top_marks = 0

for student in quiz_scores:
    if quiz_scores[student] > top_marks:
        top_marks = quiz_scores[student]
        top_student = student

print("Top Performer =", top_student)

# Task 4: Students who passed
passed = []

for student in quiz_scores:
    if quiz_scores[student] >= 10:
        passed.append(student)

print("Passed Students =", passed)

# Task 5: Class average
total = 0

for student in quiz_scores:
    total += quiz_scores[student]

average = total / len(quiz_scores)

print("Class Average =", average)
