# ask the user to input no of row and then print the pattern
rows = int(input("Enter number of rows: "))

if(rows<=0):
    exit("Invalid number of rows")
#to display pattern
for i in range(1, rows+1):
    print("*" * i)
