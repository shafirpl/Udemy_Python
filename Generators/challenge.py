

def yes_or_no():
    l = ['yes', 'no']
    count = 0

    # while True:
    #   if(count == 0):
    #       yield l[0]
    #       count = 1

    #   else:
    #       yield l[1]
    #       count = 0

    # gives an error
    if(count == 0):
      yield l[0]
      count = 1

    else:
      yield l[1]
      count = 0


gen = yes_or_no()
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
print(next(gen))  # 'yes'
print(next(gen))  # 'no'
