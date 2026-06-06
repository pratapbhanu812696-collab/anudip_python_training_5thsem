# List of batsman's scores
scores = [45, 78, 12, 100, 67, 8, 90, 55]

# Part 1: Count half-centuries and centuries
half_century = 0
century = 0

for score in scores:
    if score >= 100:
        century += 1
    elif score >= 50:
        half_century += 1

print("Half-Centuries =", half_century)
print("Centuries =", century)

# Part 2: Find highest score
highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

print("Highest Score =", highest)

# Part 3: Display scores below 20
print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score)

# Part 4: Calculate average score
total = 0

for score in scores:
    total += score

average = total / len(scores)

print("Average Score =", average)
