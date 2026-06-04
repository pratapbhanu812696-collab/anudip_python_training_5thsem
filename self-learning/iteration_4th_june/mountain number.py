#Mountain Number is a number whose digits first increase and then decrease
number = input("Enter a number: ")
if len(number) < 3:
    print(number, "is not a mountain number.")
else:
    i = 0
    length = len(number)

    # 1. Climb the mountain (digits must strictly increase)
    while i + 1 < length and number[i] < number[i+1]:
        i += 1

    # The peak cannot be the very first digit or the very last digit
    if i == 0 or i == length - 1:
        print(number, "is not a mountain number.")
    else:
        # 2. Descend the mountain (digits must strictly decrease)
        while i + 1 < length and number[i] > number[i+1]:
            i += 1

        # If we successfully reached the end of the string, it's a mountain!
        if i == length - 1:
            print(number, "is a mountain number.")
        else:
            print(number, "is not a mountain number.")
