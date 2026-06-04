 #if three side form a triangle , than specify type of triangle
# Get the three sides from the user
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# 1. Check if the sides can actually make a triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    
    # 2. Find the type based on sides
    if a == b == c:
        print("It is an Equilateral triangle (all sides equal).")
    elif a == b or b == c or a == c:
        print("It is an Isosceles triangle (two sides equal).")
    else:
        print("It is a Scalene triangle (all sides different).")

else:
    print("These sides cannot form a triangle!")
