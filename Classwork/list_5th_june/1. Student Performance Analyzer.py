# Initial student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

# Initialize lists and counters
passed_students = []
failed_count = 0
merit_list = []

# Initialize highest and lowest with the first element of the list
highest_marks = marks[0]
lowest_marks = marks[0]

# Single loop to process all conditions
for mark in marks:
    # 1. Check for passed students (marks >= 40)
    if mark >= 40:
        passed_students.append(mark)
    else:
        # 2. Count failed students
        failed_count += 1
        
    # 3. Find highest and lowest marks manually
    if mark > highest_marks:
        highest_marks = mark
    if mark < lowest_marks:
        lowest_marks = mark
        
    # 4. Create merit list (marks > 75)
    if mark > 75:
        merit_list.append(mark)

# Display the results
print(f"Passed Students: {passed_students}")
print(f"Failed Count: {failed_count}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Merit List: {merit_list}")
