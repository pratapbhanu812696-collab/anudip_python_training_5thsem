Secret Code Validator
#A secret code is a string that contains only the characters "a", "b", and "c".
#A secret code is valid if it contains at least one "a", at least one "b", and at least one "c".
#Write a function that takes a string as input and returns True if the string is a valid secret code, and False otherwise
number = input("Enter the secret code: ")
def is_valid_secret_code(code):
    if 'a' in code and 'b' in code and 'c' in code:
        return True
    else:
        return False
if is_valid_secret_code(number):
    print("The secret code is valid.")
else:    print("The secret code is invalid.")

