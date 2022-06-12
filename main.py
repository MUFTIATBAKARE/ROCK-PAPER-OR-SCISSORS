import random

#R FOR ROCK
#P FOR PAPER
#S FOR SCISSORS

while True:
    choices = ["R", "P", "S"]

    computer = random.choice(choices)
    player = None


    while player not in choices:
        player = input("R, P, OR S?: ").upper()
        
        if player not in (choices):
            print("Error, try again")
        
        if player == computer:
            print("CPU:",computer)
            print("Player:",player)
            print("It's a tie!")

        elif player =="R":
            if computer == "P":
                print("CPU:",computer)
                print("Player:",player)
                print("Computer win!")
            if computer == "S":
                print("CPU:",computer)
                print("Player:",player)
                print("You win!")
        
        elif player =="S":
            if computer == "R":
                print("CPU:",computer)
                print("Player:",player)
                print("Computer win!")
            if computer == "P": 
                print("CPU:",computer)
                print("Player:",player)
                print("You win!")
   
        elif player =="P":
            if computer == "S":
                print("CPU:",computer)
                print("Player:",player)
                print("Computer win!")
            if computer == "R": 
                print("CPU:",computer)
                print("Player:",player)
                print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
            break

print("Bye!")