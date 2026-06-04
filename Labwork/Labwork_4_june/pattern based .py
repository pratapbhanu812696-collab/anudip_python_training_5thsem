#7. Pattern-Based Number Pyramid
# 1. Take input from the user
rows = int(input("Enter the number of rows for the pyramid: "))
# 2. Generate the pyramid pattern
for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print numbers in the pyramid
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row

