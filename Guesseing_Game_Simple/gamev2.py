print("Rock....")
print("Paper....")
print("Scissors....")

player1 = input("Player 1, make your move: ")
# This multiplied by 20 means that this line will be 
# printed 20 times, and since we have \n, that means 
# every line will be seperate

print("****N0 CHEATING!\n" *20)
player2 = input("Player 2, make your move: ")

#we don't have to put () after if, but
# i am doing it for stylies and being consistent
# with other languages

if (player1 == player2):
    print("It's a tie")

elif (player1 == "rock"):
    if player2 == "scissors" :
        print("Player 1 wins")
    elif player2 == "paper":
        print("player 2 wins")

elif (player1 == "paper"):
    if(player2 == "rock"):
        print("Player 1 wins")
    elif(player2 == "scissors"):
        print("Player 2 wins")

elif (player1 == "scissors"):
    if(player2 == "rock"):
        print("Player 2 wins")
    elif (player2 == "paper"):
        print("Player 1 wins")
    
else:
    print("something went wrong")
