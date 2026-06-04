#Calculating simple interest 
p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest (%): "))
t = float(input("Enter Time (years): "))
if p <= 0 or r <= 0 or t <= 0:
    print("Invalid Input")
else:
    si = (p * r * t) / 100
    print("Simple Interest =", si)
