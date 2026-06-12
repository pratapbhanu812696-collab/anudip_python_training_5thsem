# ---------------------------------------------------------
# STUDENT RESULT MANAGEMENT SYSTEM
# ---------------------------------------------------------
# File : results.txt
# Functions:
# 1. Display all student records
# 2. Search student by ID
# 3. Find topper and lowest scorer
# 4. Calculate class average
# 5. Count pass and fail students
# 6. Generate grades
# 7. Write grade report into grades.txt
# ---------------------------------------------------------

FILE_NAME = "results.txt"


# Function to load student records from file
def load_students():

    students = []

    file = open(FILE_NAME, "r")

    for line in file:

        data = line.strip().split(",")

        student = {
            "id": data[0],
            "name": data[1],
            "marks": int(data[2])
        }

        students.append(student)

    file.close()

    return students


# Function to display all student records
def display_students():

    students = load_students()

    print("\nALL STUDENT RECORDS")
    print("-" * 40)

    for student in students:

        print(student["id"], student["name"], student["marks"])


# Function to search student using Student ID
def search_student():

    students = load_students()

    student_id = input("Enter Student ID: ")

    found = False

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])

            found = True
            break

    if not found:
        print("Student not found.")


# Function to find topper and lowest scorer
def topper_lowest():

    students = load_students()

    topper = students[0]
    lowest = students[0]

    for student in students:

        if student["marks"] > topper["marks"]:
            topper = student

        if student["marks"] < lowest["marks"]:
            lowest = student

    print("\nTOPPER")
    print(topper["id"], topper["name"], topper["marks"])

    print("\nLOWEST SCORER")
    print(lowest["id"], lowest["name"], lowest["marks"])


# Function to calculate class average
def class_average():

    students = load_students()

    total = 0

    for student in students:

        total += student["marks"]

    average = total / len(students)

    print("Class Average =", average)


# Function to count pass and fail students
def pass_fail_count():

    students = load_students()

    pass_count = 0
    fail_count = 0

    for student in students:

        if student["marks"] >= 40:
            pass_count += 1

        else:
            fail_count += 1

    print("Pass Students =", pass_count)
    print("Fail Students =", fail_count)


# Function to assign grade
def get_grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 40:
        return "C"

    else:
        return "F"


# Function to generate and display grades
def generate_grades():

    students = load_students()

    print("\nGRADE REPORT")
    print("-" * 40)

    for student in students:

        grade = get_grade(student["marks"])

        print(student["id"],student["name"],student["marks"],grade)


# Function to write grades into grades.txt
def write_grade_report():

    students = load_students()

    file = open("grades.txt", "w")

    for student in students:

        grade = get_grade(student["marks"])

        line = student["id"],",",\
               student["name"],",",\
               str(student["marks"]),",",\
               grade,"\n"

        file.write(line)

    file.close()

    print("Grade report written to grades.txt")


# ---------------- MAIN MENU ---------------- #

while True:

    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Display All Students")
    print("2. Search Student by ID")
    print("3. Find Topper and Lowest Scorer")
    print("4. Calculate Class Average")
    print("5. Count Pass and Fail Students")
    print("6. Generate Grades")
    print("7. Write Grade Report to File")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        display_students()

    elif choice == "2":
        search_student()

    elif choice == "3":
        topper_lowest()

    elif choice == "4":
        class_average()

    elif choice == "5":
        pass_fail_count()

    elif choice == "6":
        generate_grades()

    elif choice == "7":
        write_grade_report()

    elif choice == "8":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")
