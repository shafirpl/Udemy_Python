print("How Old Are You?")
# This input function takes string, so
# in order to work with this variable, we
# need to convert this variable

# also it is usually standard that we take the value, and 
# later convert it to an int or something
age = input()

# checking to see if age is empty or not
# and if it is, don't do anything
# The reason we haven't still converted because 
# if the user entered an empty string, 
# The conversion will create an error
# So we need to convert it after we check
# whether it is an empty string or not
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband!")

    elif age >= 21:
        print("You are good to enter and can drink!")

    else:
        print("You canoot come in")

else:
    print("Please enter an age:")
    
