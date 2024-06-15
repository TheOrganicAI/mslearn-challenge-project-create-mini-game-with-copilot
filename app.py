# Import necessary modules

# Define a function to get the computer's move
# The computer should randomly choose one of the options: rock, paper, or scissors

# Define a function to determine the winner
# This function should take the player's move and the computer's move as arguments
# Determine the winner based on the rules:
# - Rock beats scissors
# - Scissors beat paper
# - Paper beats rock
# Return 'win' if the player wins, 'lose' if the player loses, and 'tie' if it's a tie

# Define a function to get the player's move
# Prompt the player to enter a move: rock, paper, or scissors
# Convert the input to lowercase and check if it's a valid move
# If the move is invalid, inform the player and prompt again

# Define the main function to play the game
# This function should include the main game loop:
# - Get the player's move
# - Get the computer's move
# - Determine the winner
# - Display the result
# - Ask if the player wants to play again
# - Keep track of the player's score
# - Display the score at the end of the game

# Start the game
# Call the main game function if the script is run directly

import random

def get_player_move():
    """Prompt the player for a move until a valid move is entered."""
    valid_moves = ['rock', 'paper', 'scissors']
    move = input("Enter your move (rock, paper, scissors): ").lower()
    while move not in valid_moves:
        print("Invalid move. Please choose rock, paper, or scissors.")
        move = input("Enter your move (rock, paper, scissors): ").lower()
    return move

def get_computer_move():
    """Randomly select a move for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_move, computer_move):
    """Determine the winner based on the player's and computer's moves."""
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "scissors" and computer_move == "paper") or \
         (player_move == "paper" and computer_move == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a game of rock, paper, scissors."""
    player_score = 0
    computer_score = 0

    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()
        print(f"Computer's move: {computer_move}")
        result = determine_winner(player_move, computer_move)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {player_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_game()
