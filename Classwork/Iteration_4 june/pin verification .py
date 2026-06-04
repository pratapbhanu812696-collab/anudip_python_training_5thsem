#pin verification 
pin = input("Enter your 4-digit PIN: ")
if len(pin) == 4 and pin.isdigit():
    print("PIN accepted.")
else:    print("Invalid PIN! Please enter a 4-digit numeric PIN.")

