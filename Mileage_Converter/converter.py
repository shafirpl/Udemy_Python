print("How many kilometers did you cycle today?")
kms = input()
# This input function takes string, so 
# in order to work with this variable, we 
# need to convert this variable

# The reason this print statement works because right 
# now kms is a string. If we convert it at the begining like
# this kms = float(input()); then it would not compile and
# throw us an error. That is why we are converting kms
# later down the path
print("Ok, you said" + " " + kms)

# https: // www.programiz.com/python-programming/methods/built-in/round
# That url describes the round function

miles = float(kms)/1.60934
miles = round(miles,2)

print(f"That is equal to {miles} miles ")
