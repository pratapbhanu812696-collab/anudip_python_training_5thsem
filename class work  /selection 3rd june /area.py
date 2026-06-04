# program to calculate area and perimeter of a triangle
#input threr side of triangle
s1=int(input("enter side 1"))
s2=int(input("enter side2"))
s3=int(input("enter side3"))
perimeter=s1+s2+s3
print("perimeter of triangle is",perimeter)
# calculate area of triangle using Heron's formula
s=perimeter/2
area=(s*(s-s1)*(s-s2)*(s-s3))**0.5
print("area of triangle is",area)
