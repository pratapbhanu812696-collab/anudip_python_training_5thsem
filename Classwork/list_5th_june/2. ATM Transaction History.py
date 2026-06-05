# Initial transaction history
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# Initialize variables
current_balance = 0
deposit_list = []
withdrawal_list = []

largest_deposit = 0
largest_withdrawal = 0  # To store the magnitude/absolute value of the largest withdrawal

# Process transactions
for amt in transactions:
    # Calculate ongoing current balance
    current_balance += amt
    
    if amt > 0:
        # Process deposits
        deposit_list.append(amt)
        if amt > largest_deposit:
            largest_deposit = amt
    else:
        # Process withdrawals
        withdrawal_list.append(amt)
        # Convert to positive using abs() to easily find the largest raw amount withdrawn
        if abs(amt) > largest_withdrawal:
            largest_withdrawal = abs(amt)

# Display the results
print(f"Current Balance: {current_balance}")
print(f"Deposits: {deposit_list}")
print(f"Withdrawals: {withdrawal_list}")
print(f"Largest Deposit: {largest_deposit}")
print(f"Largest Withdrawal: {largest_withdrawal}")
