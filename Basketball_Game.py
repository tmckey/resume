#Game created for fun!

import random

# Intro
print("Welcome to Trevor's Basketball Game!")
player_name = input("Enter your player name:\n")

# Game variables
player_score = 0
opponent_score = 0

# Start of the game
print(f"Alright, {player_name}! Get ready for basketball.")

while True:
    print("\nCurrent Score:")
    print(f"{player_name}: {player_score} | Opponent: {opponent_score}")

    # Player's action
    action = input("\nChoose your move: shoot/dribble/defend\n").lower()

    if action == "shoot":
        shot_result = random.choice(["made", "missed"])
        if shot_result == "made":
            print(f"You made the shot! +2 points.")
            player_score += 2
            # Opponent gets a random number of points only if the player misses
            opponent_points = random.randint(0, 3)
            print(f"The opponent scores {opponent_points} points.")
            opponent_score += opponent_points
        else:
            print("You missed the shot. No points.")
            # If it's a turnover, opponent scores
            opponent_points = random.randint(1, 3)
            print(f"Opponent scores {opponent_points} points due to a turnover.")
            opponent_score += opponent_points
        
    elif action == "dribble":
        print("You dribble the ball, trying to find an opening.")
        opponent_action = random.choice(["steal", "block"])
        
        if opponent_action == "steal":
            print("Opponent steals the ball. Turnover!")
            # If it's a turnover, opponent scores
            opponent_points = random.randint(1, 3)
            print(f"Opponent scores {opponent_points} points due to a turnover.")
            opponent_score += opponent_points
        else:
            print("You successfully dribble past the opponent.")
            # Add points for successful dribble
            dribble_points = random.randint(2, 3)
            print(f"You gained {dribble_points} points for either a layup, pull up, or three!")
            player_score += dribble_points
    
    elif action == "defend":
        opponent_action = random.choice(["shoot", "dribble"])
        print(f"Opponent attempts to {opponent_action}.")
        
        if opponent_action == "shoot":
            shot_result = random.choice(["made", "missed"])
            if shot_result == "made":
                print("Opponent made the shot. +2 points for them.")
                opponent_score += 2
            else:
                print("Opponent missed the shot. Good defense!")
        else:
            print("You defend well, preventing the opponent from advancing.")

    else:
        print("Invalid move. Choose a valid move: shoot/dribble/defend")

    # Check if the game is over
    if player_score >= 10:
        print(f"Congratulations, {player_name}! You won the game with a score of {player_score}-{opponent_score}.")
        break
    elif opponent_score >= 10:
        print(f"Sorry, {player_name}. You lost the game with a score of {player_score}-{opponent_score}. Better luck next time.")
        break