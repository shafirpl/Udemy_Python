# import random
# in this way, we had to do rand_num = random.randint(0,2)
# so another better way is this one
from random import randint

# by doing this, we don't have to use random.randint, we 
# can just do randint


print("Rock....")
print("Paper....")
print("Scissors....")

# This will make the input case insensitive, what
# we are doing here is just taking input
# and making it a lower case using lower()
player = input("Player 1, make your move: ").lower()
computer = "rock"

rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"

elif rand_num == 1:
    computer = "paper"

else:
    computer = "scissors"

#print("Computer chose:"+computer)
print(f"Computer chose: {computer}")




#we don't have to put () after if, but
# i am doing it for stylies and being consistent
# with other languages

if (player == computer):
    print("It's a tie")

elif (player == "rock"):
    if computer == "scissors":
        print("Player 1 wins")
    else:
        print("Computer wins")

elif (player == "paper"):
    if(computer == "rock"):
        print("Player 1 wins")
    else:
        print("Computer wins")

elif (player == "scissors"):
    if(computer == "paper"):
        print("Player 1 wins")
    else:
        print("Computer wins")

else:
    print("something went wrong")
