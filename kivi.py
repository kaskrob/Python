def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"

    if player1 == 'rock':
        if player2 == 'scissors':
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1 == 'scissors':
        if player2 == 'paper':
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1 == 'paper':
        if player2 == 'rock':
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"

print("Welcome to Rock-Paper-Scissors!")
print("Player 1, please choose: rock, paper, or scissors.")
player1_choice = input("Player 1: ")

print("Player 2, please choose: rock, paper, or scissors.")
player2_choice = input("Player 2: ")

winner = determine_winner(player1_choice, player2_choice)
print(winner)
