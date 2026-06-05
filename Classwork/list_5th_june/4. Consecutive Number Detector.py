# Initial list of numbers
numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# Initialize a list to store the pairs for the additional challenge
consecutive_pairs = []

# Loop up to len(numbers) - 1 so we don't go out of bounds
for i in range(len(numbers) - 1):
    current_num = numbers[i]
    next_num = numbers[i + 1]
    
    # Check if the next number is exactly 1 greater than the current number
    if next_num - current_num == 1:
        # Print the immediate result
        print(f"{current_num} and {next_num} are consecutive")
        
        # Additional Challenge: Store the pair as a tuple or a small list
        consecutive_pairs.append((current_num, next_num))

# Display the stored pairs list
print("---")
print(f"Stored Consecutive Pairs: {consecutive_pairs}")
