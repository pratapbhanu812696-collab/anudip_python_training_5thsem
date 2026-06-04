#Consecutive Digit Number
number=int(input("Enter a number: "))
temp=number
prev=-1
flag=0
while temp>0:
    digit=temp%10
    if prev==-1:
        prev=digit
    else:
        if digit!=prev-1:
            flag=1
            break
        prev=digit
    temp//=10
if flag==0:    print(number,"is a consecutive digit number.")
else:    print(number,"is not a consecutive digit number.")
