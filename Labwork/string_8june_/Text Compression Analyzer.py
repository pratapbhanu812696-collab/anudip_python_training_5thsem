# ------------------------------------------
# Text Compression Analyzer
# ------------------------------------------

text = "AAABBBCCCDDDAAA"

print("Original Text =", text)

# Task 1 & 2
freq = {}

for ch in text:

    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character Frequencies:")

for ch in freq:
    print(ch, "->", freq[ch])

# Task 3
unique = []

for ch in text:

    if ch not in unique:
        unique.append(ch)

print("Unique Characters =", unique)

# Task 4
max_char = ""
max_count = 0

for ch in freq:

    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch

print("Most Frequent Character =", max_char)

# Task 5: Compressed Output
compressed = ""

count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count += 1

    else:
        compressed += text[i] + str(count)
        count = 1

compressed += text[-1] + str(count)

print("Compressed Output =", compressed)

# Task 6: Compression Ratio
original_length = len(text)
compressed_length = len(compressed)

ratio = (compressed_length / original_length) * 100

print("Original Length =", original_length)
print("Compressed Length =", compressed_length)
print("Compression Ratio =", ratio, "%")
