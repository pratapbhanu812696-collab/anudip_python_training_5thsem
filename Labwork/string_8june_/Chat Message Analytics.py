# ------------------------------------------
# Chat Message Analytics
# ------------------------------------------

message = "Python is awesome and Python is easy to learn"

# Task 1: Count total characters
print("Total Characters =", len(message))

words = message.split()

# Task 2: Count total words
print("Total Words =", len(words))

# Task 3: Find longest word
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word =", longest)

# Task 4: Find shortest word
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest Word =", shortest)

# Task 5: Count Python occurrences
count = 0

for word in words:
    if word == "Python":
        count += 1

print("Occurrences of Python =", count)

# Task 6: Words having more than 4 characters
long_words = []

for word in words:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters =", long_words)

# Task 7: Display words starting with vowel
print("Words Starting With Vowel:")

for word in words:
    if word[0].lower() in "aeiou":
        print(word)

# Task 8: Count vowels and consonants
vowels = 0
consonants = 0

for ch in message.lower():

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)v
