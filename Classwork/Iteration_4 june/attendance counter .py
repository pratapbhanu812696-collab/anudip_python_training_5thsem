#attendance counter

# Start the counter at 0
attendance_count = 0

# Keep running the loop until 30 students are reached
while attendance_count < 30:  
    # Increase the count by 1
    attendance_count = attendance_count + 1
    
    # Print the exact output matching your assignment
    print("Student Entered")
    print(f"Attendance Count: {attendance_count}")
    print() # Prints a blank line for clean spacing
# Once the loop is done, print the final message
print("Attendance is full. No more students can enter.")
