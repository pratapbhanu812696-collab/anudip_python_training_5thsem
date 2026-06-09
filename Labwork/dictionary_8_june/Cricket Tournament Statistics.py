runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

orange_cap_winner = ""
max_runs = -1
lowest_scorer = ""
min_runs = 99999
total_tournament_runs = 0
below_400 = []
between_400_600 = 0

print("Players Scoring More Than 500 Runs:")
for player, score in runs.items():
    total_tournament_runs += score
    
    # 1. More than 500 runs
    if score > 500:
        print(player)
        
    # 2. Orange Cap winner
    if score > max_runs:
        max_runs = score
        orange_cap_winner = player
        
    # 3. Lowest scorer
    if score < min_runs:
        min_runs = score
        lowest_scorer = player
        
    # 5. Below 400 list
    if score < 400:
        below_400.append(player)
        
    # 6. Count between 400 and 600
    if 400 <= score <= 600:
        between_400_600 += 1

print(f"\nOrange Cap Winner: {orange_cap_winner} ({max_runs})")
print(f"Lowest Scorer: {lowest_scorer} ({min_runs})")
print(f"Total Tournament Runs: {total_tournament_runs}")
print(f"Players Scoring Below 400: {below_400}")
print(f"Players Between 400 and 600 Runs: {between_400_600}")
