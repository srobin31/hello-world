# Shawn Robin
# 9/29/14
# Rock, Paper, Scissors

import random

#intro
print("This program will simulate a game of rock, paper, scissors against the computer.")

#menu
print("""\nPress the following leters to:
Choose rock (r)
Choose paper (p)
Choose scissors (s)""")

#assigning variables
user = 0
cpu = 0
hand = input
end = input

#while loop
while user < 5 and cpu < 5:
    cpu_hand = random.randint(1,3)
    # assigning the random number chosen by the computer to moves within the game
    if cpu_hand == 1:
        cpu_hand = "rock"
    elif cpu_hand == 2:
        cpu_hand = "paper"
    elif cpu_hand == 3:
        cpu_hand = "scissors"
        
    # asking user for move    
    hand = input("\nWhat would you like to do? ")
    
    # invalid key pressed by user   
    while hand != "r" and hand != "p" and hand != "s":
        print("Invalid Option")
        hand = input("\nPlease enter a valid key. ")

    # assigning key pressed by the user to moves within the game
    if hand == "r":
        hand = "rock"
    elif hand =="p":
        hand = "paper"
    elif hand == "s":
        hand = "scissors"

    # when computer's choice is the same as the user's        
    if cpu_hand == hand:
        # printing results
        print("\nYou tied. You chose " +hand+ ". The computer chose " +cpu_hand+ ".")
        print("\nThe score is now:")
        print("You:" , user)
        print("Computer:" , cpu)

    # when the computer chooses rock and user chooses paper 
    elif cpu_hand == "rock" and hand == "paper":
        # +1 point to the user
        user += 1
        # printing results
        print("\nYou won. You chose " +hand+ ". The computer chose " +cpu_hand+ ".")
        print("\nThe score is now:")
        print("You:" , user)
        print("Computer:" , cpu)

    # when the computer chooses rock and user chooses scissors        
    elif cpu_hand == "rock" and hand == "scissors":
        # +1 point to the computer
        cpu += 1
        # printing results
        print("\nYou lost. You chose " +hand+ ". The computer chose " +cpu_hand+ ".")
        print("\nThe score is now:")
        print("You:" , user)
        print("Computer:" , cpu)

    # when the computer chooses paper and user chooses rock    
    elif cpu_hand == "paper" and hand == "rock":
        # +1 point to the computer
        cpu += 1
        # printing results
        print("\nYou lost. You chose " +hand+ ". The computer chose " +cpu_hand+ ".")
        print("\nThe score is now:")
        print("You:" , user)
        print("Computer:" , cpu)

    # when the computer chooses paper and user chooses scissors
    elif cpu_hand == "paper" and hand == "scissors":
        # +1 point to the user
        user += 1
        # printing results
        print("\nYou won. You chose " +hand+ ". The computer chose " +cpu_hand+ ".")
        print("\nThe score is now:")
        print("You:" , user)
        print("Computer:" , cpu)

    # when the computer chooses scissors and user chooses rock
    elif cpu_hand == "scissors" and hand == "rock":
        # +1 point to the user
        user += 1
        # printing results
        print("\nYou won. You chose " +hand+ ". The computer chose " +cpu_hand+".")
        print("\nThe score is now:")
        print("You:" , user)
        print("Computer:" , cpu)

    # when the computer chooses scissors and user chooses paper
    elif cpu_hand == "scissors" and hand == "paper":
        # +1 point to the computer
        cpu += 1
        # printing results
        print("\nYou lost. You chose " +hand+ ". The computer chose " ,cpu_hand,".")
        print("\nThe score is now:")
        print("You:" , user)
        print("Computer:" , cpu)
   
    end = input
    # while loop
    while end != "y" and cpu < 5 and user < 5:
        # asking the user if they'd like to continue playing 
        end = input("\nWould you like to play again? (y/n) ")
        if end == "n":
            cpu += 5
            user += 5
        # invalid key pressed by user
        elif end != "y" and end != "n":
            print("Invalid Option")

# final game results        
if cpu > user:
        print("\nThe game is over. You lost. Better luck next time.")
elif user > cpu:
        print("\nThe game is over. Yay! You won!")
elif user == cpu:
        print("\nThe game is over. You tied.")
