# 1. Database containing exactly 30 players
players = {
    "Virat": {"runs": 645, "matches": 12, "wickets": 0},
    "Rohit": {"runs": 540, "matches": 11, "wickets": 0},
    "Bumrah": {"runs": 45, "matches": 10, "wickets": 28},
    "Hardik": {"runs": 380, "matches": 12, "wickets": 14},
    "Jadeja": {"runs": 310, "matches": 12, "wickets": 16},
    "Rahul": {"runs": 410, "matches": 11, "wickets": 0},
    "Shami": {"runs": 15, "matches": 7, "wickets": 24},
    "Siraj": {"runs": 20, "matches": 10, "wickets": 15},
    "Kuldeep": {"runs": 35, "matches": 9, "wickets": 18},
    "Gill": {"runs": 480, "matches": 12, "wickets": 0},
    "Iyer": {"runs": 526, "matches": 11, "wickets": 0},
    "Sky": {"runs": 320, "matches": 9, "wickets": 1},
    "Pant": {"runs": 405, "matches": 10, "wickets": 0},
    "Axar": {"runs": 210, "matches": 8, "wickets": 11},
    "Ashwin": {"runs": 180, "matches": 6, "wickets": 9},
    "Warner": {"runs": 510, "matches": 11, "wickets": 0},
    "Head": {"runs": 560, "matches": 10, "wickets": 4},
    "Maxwell": {"runs": 400, "matches": 9, "wickets": 8},
    "Zampa": {"runs": 30, "matches": 11, "wickets": 22},
    "Cummins": {"runs": 190, "matches": 11, "wickets": 15},
    "Starc": {"runs": 85, "matches": 10, "wickets": 17},
    "De Kock": {"runs": 590, "matches": 10, "wickets": 0},
    "Markram": {"runs": 410, "matches": 10, "wickets": 3},
    "Klaasen": {"runs": 430, "matches": 10, "wickets": 0},
    "Coetzee": {"runs": 40, "matches": 8, "wickets": 20},
    "Maharaj": {"runs": 60, "matches": 10, "wickets": 14},
    "Rachin": {"runs": 578, "matches": 10, "wickets": 6},
    "Mitchell": {"runs": 552, "matches": 10, "wickets": 1},
    "Santner": {"runs": 120, "matches": 10, "wickets": 16},
    "Boult": {"runs": 25, "matches": 10, "wickets": 15}
}

# --- HELPER LOGIC (No Built-in Sorting Allowed) ---
# Calculate Average Runs once to use across multiple requirements
total_runs = 0
for p in players:
    total_runs += players[p]["runs"]
avg_runs = total_runs / len(players)

while True:
    print("\n" + "="*50)
    print("      CRICKET TOURNAMENT ANALYTICS SYSTEM")
    print("="*50)
    print("1. Display All Player Statistics")
    print("2. Find Highest Run Scorer")
    print("3. Find Lowest Run Scorer")
    print("4. Calculate Average Runs")
    print("5. Find Player with Maximum Wickets")
    print("6. Find All-Rounders (Runs > 300 & Wickets > 5)")
    print("7. Display Players Scoring Above Average")
    print("8. Categorize Players")
    print("9. Generate Team Statistics")
    print("10. Display Top 5 Batsmen")
    print("11. Display Top 5 Bowlers")
    print("12. View Award Winners & Tournament Report")
    print("13. Exit")
    print("="*50)
    
    choice = input("Enter your choice (1-13): ")
    
    if choice == "1":
        print(f"\n{'Player':<15}{'Matches':<10}{'Runs':<10}{'Wickets':<10}")
        print("-" * 45)
        for name, stats in players.items():
            print(f"{name:<15}{stats['matches']:<10}{stats['runs']:<10}{stats['wickets']:<10}")
            
    elif choice == "2":
        max_runs = -1
        top_batsman = ""
        for name, stats in players.items():
            if stats["runs"] > max_runs:
                max_runs = stats["runs"]
                top_batsman = name
        print(f"\nHighest Run Scorer: {top_batsman} ({max_runs} runs)")
        
    elif choice == "3":
        min_runs = 99999
        lowest_batsman = ""
        for name, stats in players.items():
            if stats["runs"] < min_runs:
                min_runs = stats["runs"]
                lowest_batsman = name
        print(f"\nLowest Run Scorer: {lowest_batsman} ({min_runs} runs)")
        
    elif choice == "4":
        print(f"\nAverage Runs Scored by Players: {avg_runs:.2f}")
        
    elif choice == "5":
        max_wickets = -1
        top_bowler = ""
        for name, stats in players.items():
            if stats["wickets"] > max_wickets:
                max_wickets = stats["wickets"]
                top_bowler = name
        print(f"\nPlayer with Maximum Wickets: {top_bowler} ({max_wickets} wickets)")
        
    elif choice == "6":
        print(f"\nAll-Rounders (Runs > 300 and Wickets > 5):")
        print(f"{'Player':<15}{'Runs':<10}{'Wickets':<10}")
        print("-" * 35)
        for name, stats in players.items():
            if stats["runs"] > 300 and stats["wickets"] > 5:
                print(f"{name:<15}{stats['runs']:<10}{stats['wickets']:<10}")
                
    elif choice == "7":
        print(f"\nPlayers Scoring Above Average ({avg_runs:.2f}):")
        print(f"{'Player':<15}{'Runs':<10}")
        print("-" * 25)
        for name, stats in players.items():
            if stats["runs"] > avg_runs:
                print(f"{name:<15}{stats['runs']:<10}")
                
    elif choice == "8":
        print(f"\nPlayer Performance Categories:")
        print(f"{'Player':<15}{'Runs':<10}{'Category':<20}")
        print("-" * 45)
        for name, stats in players.items():
            if stats["runs"] >= 500:
                cat = "Star Performer"
            elif stats["runs"] >= 350:
                cat = "Good Performer"
            elif stats["runs"] >= 150:
                cat = "Average Performer"
            else:
                cat = "Poor Performer"
            print(f"{name:<15}{stats['runs']:<10}{cat:<20}")
            
    elif choice == "9":
        total_m = 0
        total_w = 0
        for name, stats in players.items():
            total_m += stats["matches"]
            total_w += stats["wickets"]
        print("\n--- Team Statistics Summary ---")
        print(f"Total Matches Played combined: {total_m}")
        print(f"Total Runs Scored: {total_runs}")
        print(f"Total Wickets Taken: {total_w}")
        
    elif choice == "10":
        # Manual bubble sort to find top 5 batsmen
        plist = []
        for name, stats in players.items():
            plist.append([name, stats["runs"]])
            
        n = len(plist)
        for i in range(n):
            for j in range(0, n-i-1):
                if plist[j][1] < plist[j+1][1]: # Descending order
                    plist[j], plist[j+1] = plist[j+1], plist[j]
                    
        print("\nTop 5 Batsmen:")
        for i in range(5):
            print(f"{i+1}. {plist[i][0]} - {plist[i][1]} runs")
            
    elif choice == "11":
        # Manual bubble sort to find top 5 bowlers
        plist = []
        for name, stats in players.items():
            plist.append([name, stats["wickets"]])
            
        n = len(plist)
        for i in range(n):
            for j in range(0, n-i-1):
                if plist[j][1] < plist[j+1][1]: # Descending order
                    plist[j], plist[j+1] = plist[j+1], plist[j]
                    
        print("\nTop 5 Bowlers:")
        for i in range(5):
            print(f"{i+1}. {plist[i][0]} - {plist[i][1]} wickets")
            
    elif choice == "12":
        # Building Award Winners Dictionary
        max_r, max_w = -1, -1
        top_bat, top_bowl = "", ""
        for name, stats in players.items():
            if stats["runs"] > max_r:
                max_r = stats["runs"]
                top_bat = name
            if stats["wickets"] > max_w:
                max_w = stats["wickets"]
                top_bowl = name
                
        awards = {
            "Golden Bat": {"Player": top_bat, "Stat": f"{max_r} Runs"},
            "Golden Ball": {"Player": top_bowl, "Stat": f"{max_w} Wickets"}
        }
        
        print("\n🏆 AWARD WINNERS DICTIONARY 🏆")
        for award, info in awards.items():
            print(f"{award}: {info['Player']} ({info['Stat']})")
            
        print("\n📜 TOURNAMENT CHALLENGE REPORT 📜")
        print(f"The tournament featured {len(players)} players battling across matches.")
        print(f"A grand total of {total_runs} runs were recorded with an individual average of {avg_runs:.1f} runs.")
        print(f"The elite batting milestone was dominated by {top_bat}, while {top_bowl} terrorized lineups with the ball.")
        
    elif choice == "13":
        print("\nExiting System. Thank you!")
        break
    else:
        print("\nInvalid option! Please enter a number from 1 to 13.")
