#score player 11 palyer 
player_score =[]
#input  of score form user
for i in range(11):
    score = int(input("Enter the score of player {}: ".format(i+1)))
    player_score.append(score)
#display the score of each player
print("\n.......Player Scores......")
print("score of 11 players:", player_score)
#find the highest score
max_score = max(player_score)
for i in range(1, len(player_score) + 1):
    if player_score[i - 1] == max_score:
        print("Player {} has the highest score of {}".format(i, max_score))
