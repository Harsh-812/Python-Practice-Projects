import random

def roll():
    min_number = 1
    max_number = 6
    roll = random.randint(min_number, max_number)
    return roll

#value = roll()
#print(value)

while True:
    players = input("Enter the number of players(2 to 4): ")
    if players.isdigit():
        players=int(players)
        if 2 <= players <=4:
            break
        else:
            print("Players must be between 2 and 4")
    else:
        print("Invalid. Try again")


max_score=50
players_score=[0 for _ in range(players)]

#print(players_score)

while max(players_score) < max_score:
    for players_idx in range(players):
        print("\nPlayer number", players_idx + 1, "turn has just started")
        print("Your Total score is:", players_score[players_idx], "\n")
        current_score = 0
        while True:
            should_roll=input("Would you like to roll(y)?:")
            if should_roll.lower() != "y":
                break

            dice_value = roll()
            if (dice_value == 1):
                print("You rolled a 1! Your turn is over.")
                current_score = 0
                break
            else:
                current_score += dice_value
                print("You rolled a: ", dice_value)

            print("Your score is: ", current_score)  

        players_score[players_idx] += current_score 
        print("Your Total Score is: ", players_score[players_idx])   

max_score = max(players_score)  
winner_idx = players_score.index(max_score)  
print("Player number", winner_idx+1, "has won with the total score of ", max_score)    


