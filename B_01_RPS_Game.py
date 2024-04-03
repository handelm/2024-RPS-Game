# Create a game of Rock Paper Scissors

import random

# Displays instruction


def instructions():
    print('''
    ------- Instructions ------
   
    - Player start each round by typing either, rock, paper, scissors.
    -Rock crushes scissors
    -scissors cut paper
    -paper covers rock. 
    -See who wins each round!
    
    - if you want to stop playing type 'xxx'
    ''')


print("program continues")


def play_round(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# display game


def play_game():
    print("-------->>>>>Welcome<<<<<-------- to Rock-Paper-Scissors!")

# Ask if they want to see the instructions
    want_instructions = input("Press <Enter> to read the instructions or type 'no' then press enter to continue ")
    if want_instructions == "":
        instructions()
# ask how many rounds they want to play
    num_rounds = int(input("How many rounds do you want to play? "))
    player_score = 0
    computer_score = 0

    for round_num in range(1, num_rounds + 1):
        print("------------------------------")
        player_choice = input("Enter your choice (rock, paper, or scissors): ")

        while player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            player_choice = input("Enter your choice (rock, paper, or scissors): ")

        result = play_round(player_choice)
        print(result)

        if result == "You win!":
            player_score += 1

        elif result == "Computer wins!":
            computer_score += 1
# print end results
    print("------------------------------")
    print("Game over!")
    print("-----End Results-----")
    print("PLAYER score:", player_score)
    print("COMPUTER score:", computer_score)
    print("------------------------------")


play_game()


