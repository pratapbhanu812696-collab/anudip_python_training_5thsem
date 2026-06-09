# ------------------------------------------
# Product Review Analyzer
# ------------------------------------------

review = "This product is excellent excellent excellent and very useful"

words = review.split()

# Task 1: Count total words
print("Total Words =", len(words))

# Task 2: Create frequency dictionary
freq = {}

for word in words:

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\nWord Frequencies:")

for word in freq:
    print(word, "->", freq[word])

# Task 3: Most frequent word
max_word = ""
max_count = 0

for word in freq:

    if freq[word] > max_count:
        max_count = freq[word]
        max_word = word

print("\nMost Frequent Word =", max_word)

# Task 4: Words appearing once
once = []

for word in freq:

    if freq[word] == 1:
        once.append(word)

print("Words Appearing Once =", once)

# Task 5: Count words having more than 5 characters
count = 0

for word in words:

    if len(word) > 5:
        count += 1

print("Words Longer Than 5 Characters =", count)

# Task 6: Display words in reverse order
print("Words In Reverse Order:")

for i in range(len(words)-1, -1, -1):
    print(words[i])

# Task 7: Create unique words list
unique = []

for word in words:

    if word not in unique:
        unique.append(word)

print("Unique Words =", unique)
