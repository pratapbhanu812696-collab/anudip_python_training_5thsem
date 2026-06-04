#program to check three angles from a triangle or not
angle1=int(input("enter angle1")) 
#validating input
if angle1<=0:
    print("invalid input")
else:
    angle2=int(input("enter angle2"))
    if angle2<=0:
        print("invalid input")
    else:
        angle3=int(input("enter angle3"))
        if angle3<=0:
            print("invalid input")
        else:
            sum=angle1+angle2+angle3
            if sum==180:
                print("it is a triangle")
            else:
                print("it is not a triangle")
