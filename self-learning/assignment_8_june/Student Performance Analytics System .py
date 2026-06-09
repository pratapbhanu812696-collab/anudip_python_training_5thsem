'''Student Performance Analytics System 
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).  '''
#creating blank dictionary
students={}
#taking details of 30 students
for i in range(30):

    student_id=input("enter thee id of student")
    name=input("enter the name of the student")
    marks=input("enter the marks of the student ")
    students[student_id]= {"name":name, "marks": marks}
print(students)
print("------------------------------------------------")

#Task-1 To Display all student records.
print(students)

#Task-2 To Search a student using Student ID
search_id = input("Enter Student ID: ")

found = False

for student_id, details in students.items():
    if student_id == search_id:
        print("Student Found")
        print("Name :", details["name"])
        found = True
        break

if not found:
    print("Student ID not found")

# Task-3 to Add a new student.
print("enter details of students to b added")
student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
marks = int(input("Enter Marks: "))

students[student_id] = {
    "name": name,
    "marks": marks
}

print("Student added successfully!")

#Task-4 to Update marks of an existing student.
print("enter name of student to be updated and also the marks")
student_id = input("Enter Student ID: ")

if student_id in students:
    new_marks = int(input("Enter New Marks: "))
    students[student_id]["marks"] = new_marks
    print("Marks updated successfully!")
else:
    print("Student ID not found")


#Task-5 to Delete a student. 

name = input("Enter student name to delete: ")

for student_id, details in students.items():
    if details["name"] == name:
        del students[student_id]
        print("Student deleted successfully")
        break
else:
    print("Student not found")

#task-6 To Find topper and lowest scorer

for student in students.values():
    highest_marks = max(student["marks"]) 

for student in students.values():
    lowest_marks = min(student["marks"])

for student_id, details in students.items():

    if details["marks"] == highest_marks:
        print("\nTopper")
        print("ID   :", student_id)
        print("Name :", details["name"])
        print("Marks:", details["marks"])

    if details["marks"] == lowest_marks:
        print("\nLowest Scorer")
        print("ID   :", student_id)
        print("Name :", details["name"])
        print("Marks:", details["marks"])

#Task-7 to Calculate class average.   
for details in students.values() / len(students):
    average = sum(details["marks"])

print("Class Average:", round(average, 2))

#Task-8 to Count pass and fail students

pass_count = 0
fail_count = 0

for details in students.values():

    if details["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Passed Students:", pass_count)
print("Failed Students:", fail_count)

'''task-9 to  Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  '''
for details in students.values():

    if details["marks"] >= 90:
        print("Student got A grade")
    elif (details["marks"] >=75) and (details["marks"]<=89):
        print("Student got B grade")
    elif (details["marks"] >=50) and(details["marks"]<=74):
        print("Student got grade C")
    else:
        print("Student got F grade")

#task-10 to Display students scoring above average
total_marks = 0

for details in students.values():
    total_marks += details["marks"]

average = total_marks / len(students)

print("Class Average:", average)

print("\nStudents Scoring Above Average:")

for student_id, details in students.items():
    if details["marks"] > average:
        print(student_id, details["name"], details["marks"])

#task-11 to display top 5 performers.
student_list = []

for student_id, details in students.items():
    student_list.append([details["marks"], student_id, details["name"]])

student_list.sort()

print("Top 5 Performers:")

for student in student_list[-1:-6:-1]:
    print(student[1], student[2], student[0])

#task-12 to Create a separate dictionary for scholarship students (marks > 85).
scholarship_students = {}

for student_id, details in students.items():

    if details["marks"] > 85:
        scholarship_students[student_id] = details

print("Scholarship Students:\n")

for student_id, details in scholarship_students.items():
    print(student_id, details["name"], details["marks"])
