from random import random

def flipCoin():
    # generate random numbers from 0 to 1
    r = random()
    if (r>0.5):
        return "Head"
    else:
        return "Tails"


# def flipCoin():
# 	if random() > 0.5:
# 		return "HEADS"
# 	else:
# 		return "TAILS"




print(flipCoin())

