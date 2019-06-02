# https://www.udemy.com/the-modern-python3-bootcamp/learn/lecture/8794296#questions

x = input("Hey how is it going?\n")

if(x == "stop copying me"):
    print("You win")

while (x != "stop copying me"):
    x = input(f"{x}\n")
    if(x == "stop copying me"):
        print("You win")
