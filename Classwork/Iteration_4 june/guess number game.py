#Guess the Number Game
number = int(input("Enter a number: "))
if number < 0:
    print("Negative numbers are not allowed. Please enter a positive number.")
elif number == 0:
    print("Zero is not a valid guess. Please enter a positive number.")
else:
    print(f"You entered: {number}. Let's see if you can guess the number!")
