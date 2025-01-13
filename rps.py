#Nick Hu
#1/7/2025
#RPS


#Initialize
import random
wins = 0 #Tracks player's wins
losses = 0 #Tracks player's losses
ties = 0 #Tracks player's ties
#Functions

def RPS():
    print("Welcome to Rock Paper Scissor.")
    while True:
        global wins
        global losses
        global ties
        #Step 1 collect players move
        print("Make your move!")
        player = int(input("Rock(1), Paper(2), Scissor(3), Go:"))
        #Step 2 Generate a move for the computer
        computer = (random.randint(1,3))
        if computer == 1:
            computer = "rock"
            print("The computer's move is Rock!")
        elif computer == 2:
            computer = "paper"
            print("The computer's move is Paper!")
        elif computer == 3:
            computer = "scissor"
            print("The computer's move is Scissor!")
        #Step 3 Determine the outcome
        if computer == "rock" and player == 1:
            print("Tie")
            ties = ties + 1
        if computer == "rock" and player == 2:
            print("You win")
            wins = wins + 1
        if computer == "rock" and player == 3:
            print("You lose")
            losses = losses + 1
        if computer == "paper" and player == 1:
            print("You lose")
            losses = losses + 1
        if computer == "paper" and player == 2:
            print("Tie")
            ties = ties + 1
        if computer == "paper" and player == 3:
            print("You win")
            wins = wins + 1
        if computer == "scissor" and player == 1:
            print("You win")
            wins = wins + 1
        if computer == "scissor" and player == 2:
            print("You lose")
            losses = losses + 1
        if computer == "scissor1" and player == 3:
            print("Tie")
            ties = ties + 1
        #Step 4 Loop the program until player wants to quit
        playagain = input("Would you like to play again?")
        if playagain.lower() == "yes":
            print("restarting....")
        else:
            print("Thanks for playing")
            #tracks your stats
            print("You currently have " + str(wins) + " wins.")
            print("You currently have " + str(losses) + " losses")
            print("You currently have " + str(ties) + " ties")
            break

#Main
RPS()
