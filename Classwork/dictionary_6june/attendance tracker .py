attendance = {}

# Input attendance for 30 students
for i in range(30):
    roll_no = int(input("Enter Roll Number: "))
    status = input("Enter Attendance (Present/Absent): ")

    attendance[roll_no] = status

# Display present students
print("\nStudents Present:")

for roll_no, status in attendance.items():
    if status.lower() == "present":
        print(roll_no)
