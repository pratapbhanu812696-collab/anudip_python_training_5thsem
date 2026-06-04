#Longest Increasing Sequence
number = int(input("Enter the number of elements in the sequence: "))
sequence = list(map(int, input("Enter the sequence of numbers: ").split()))
if len(sequence) != number:
    print("The number of elements does not match the specified count.")
else:
    longest_length = 1
    current_length = 1

    for i in range(1, number):
        if sequence[i] > sequence[i - 1]:
            current_length += 1
        else:
            longest_length = max(longest_length, current_length)
            current_length = 1

    longest_length = max(longest_length, current_length)  # Check at the end of the loop
    print("Length of the longest increasing sequence:", longest_length)

