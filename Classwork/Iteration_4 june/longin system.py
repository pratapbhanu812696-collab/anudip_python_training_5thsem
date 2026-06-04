#Login System strong password checker
number = input("Enter a password: ")
while True:
    if len(number) < 8:
        print("Password must be at least 8 characters long.")
        break
    elif not any(char.isdigit() for char in number):
        print("Password must contain at least one digit.")
        break
    elif not any(char.isupper() for char in number):
        print("Password must contain at least one uppercase letter.")
        break
    elif not any(char.islower() for char in number):
        print("Password must contain at least one lowercase letter.")
        break
    else:
        print("Password is strong.")
        break
