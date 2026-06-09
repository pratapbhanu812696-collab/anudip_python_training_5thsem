# Student Marks Analysis

marks = {
    "Aarav": 78,
    "Diya": 92,
    "Rohan": 45,
    "Ishita": 88,
    "Kabir": 56,
    "Meera": 39,
    "Arjun": 95,
    "Saanvi": 67,
    "Vivaan": 82,
    "Anaya": 51
}

# Task 1: Display students scoring 80 or above
print("Students scoring 80 or above:")
for student in marks:
    if marks[student] >= 80:
        print(student)

# Task 2: Count failed students
count = 0
for student in marks:
    if marks[student] < 40:
        count += 1

print("Failed Students =", count)

# Task 3: Find highest scorer
topper = max(marks, key=marks.get)
print("Highest Scorer =", topper)

# Task 4: Students scoring between 60 and 75
students_list = []

for student in marks:
    if 60 <= marks[student] <= 75:
        students_list.append(student)

print("Students scoring between 60 and 75 =", students_list)

# Task 5: Assign grades
print("Grades:")

for student in marks:
    if marks[student] >= 90:
        grade = "A"
    elif marks[student] >= 75:
        grade = "B"
    elif marks[student] >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student, "-", grade)
