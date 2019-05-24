print("Rock....")
print("Paper....")
print("Scissors....")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

#we don't have to put () after if, but 
# i am doing it for stylies and being consistent
# with other languages

if (player1 == "rock" and player2=="scissors"):
    print("player1 wins!")

elif (player1 == "rock" and player2 == "paper"):
    print("Player2 wins")

elif (player2 == "rock" and player1 == "paper"):
    print("Player1 wins")

elif (player2 == "rock" and player1== "scissors"):
    print("player2 wins!")

elif(player1=="scissors" and player2=="paper"):
    print("player 1 wins")

elif(player2 == "scissors" and player1 == "paper"):
    print("player 2 wins")


elif (player1==player2):
    print("It's a tie")

else:
    print("something went wrong")
