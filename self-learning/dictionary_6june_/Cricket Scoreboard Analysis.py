# Cricket Scoreboard Analysis

scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Task 1: Display players scoring 50 or more
print("Players scoring 50 or more:")

for player in scores:
    if scores[player] >= 50:
        print(player)

# Task 2: Count centuries
count = 0

for player in scores:
    if scores[player] >= 100:
        count += 1

print("Centuries =", count)

# Task 3: Find highest scorer
highest_player = ""
highest_score = 0

for player in scores:
    if scores[player] > highest_score:
        highest_score = scores[player]
        highest_player = player

print("Highest Scorer =", highest_player)

# Task 4: Players scoring below 30
low_scores = []

for player in scores:
    if scores[player] < 30:
        low_scores.append(player)

print("Players below 30 runs =", low_scores)

# Task 5: Players scoring between 50 and 99
count = 0

for player in scores:
    if 50 <= scores[player] <= 99:
        count += 1

print("Players scoring between 50 and 99 =", count)
