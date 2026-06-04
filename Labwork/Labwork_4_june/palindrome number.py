#9. Palindrome and Reverse Number Checker
# 1. Take input from the user
number = int(input("Enter a number: "))
# 2. Check if the number is a palindrome
def is_palindrome(n):
    num_str = str(n)
    return num_str == num_str[::-1]
# 3. Reverse the number
def reverse_number(n):
    return int(str(n)[::-1])
# 4. Analyze the number and print the results
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:    print(f"{number} is not a palindrome.")
print(f"The reverse of {number} is {reverse_number(number)}.")

