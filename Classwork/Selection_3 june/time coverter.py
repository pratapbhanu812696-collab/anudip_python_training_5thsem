#time converter 
number = int(input("Enter the number of seconds: "))
days = number // 86400
hours = (number % 86400) // 3600
minutes = (number % 3600) // 60
seconds = number % 60
print(f"{number} seconds is equal to {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
 
