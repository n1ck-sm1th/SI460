#Nicholas Smith

import sys

length = len(sys.argv)
if (length != 2):
    print("usage: isprime.py ###")
    
number = int(sys.argv[1])
if number > 512:
    print("Choose a number less than 512")
    sys.exit()
elif number > 1:
    #From geeksforgeeks 
    for i in range(2, (number//2)+1):
      
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (number % i) == 0:
            print("Not Prime!")
            break
    else:
        print("Prime!")
else:
    print("Not Prime!")