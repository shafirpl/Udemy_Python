from random import randint
choice = "y"


while choice == "y":
    actualNum = randint(1, 10)
    num = input("Guess a number between 1 and 10:")
    num = int(num)
    if(num == actualNum):
        print("You won!")
        choice = input("Do you wnat to keep playing? (y/n):")
    else:
        while (num != actualNum):
            if(num > actualNum):
                print("Too high, try again")
                num = input("Guess a number between 1 and 10:")
                num = int(num)
            else:
                print("Too low, try again")
                num = input("Guess a number between 1 and 10:")
                num = int(num)

        print("You won!")
        choice = input("Do you wnat to keep playing? (y/n):")


if(choice == "n"):
    print("\nThanks for playing. Bye!")
