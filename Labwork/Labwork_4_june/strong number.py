# Strong Number Verification
# 1. Take input from the user
number = int(input("Enter a number: "))
# 2. Check if the number is a Strong number
def is_strong(n):
    factorial_sum = 0
    for digit in str(n):
        factorial_sum += factorial(int(digit))
    return factorial_sum == n
# Helper function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
# 3. Analyze the number and print the result
if is_strong(number):           
    print(f"{number} is a Strong number.")
else:    print(f"{number} is not a Strong number.")  
