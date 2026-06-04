# Armstrong Number Checker
# 1. Take input from the user
number = int(input("Enter a number: "))
# 2. Check if the number is an Armstrong number
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n
# 3. Analyze the number and print the result
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
