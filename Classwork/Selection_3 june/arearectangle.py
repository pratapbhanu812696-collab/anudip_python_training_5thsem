# program to calculate area and perimeter of a rectangle 

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
if length > 0 and breadth > 0:
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print("Area of Rectangle =", area)
    print("Perimeter of Rectangle =", perimeter)
else:
    print("Invalid input! Length and breadth must be greater than 0.")
