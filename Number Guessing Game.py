import math
import random

lower = int(input("Enter LOWER Bound of the range:- "))
upper = int(input("Enter UPPER Bound of the range:- "))

x = random.randint(lower,upper)
f = round(math.log(upper-lower+1,2))
print("You've only",f,"chances to guess the integer!!")

count = 0

while(count < f):
    count +=1
    guessed = int(input("Guess a Number:- "))

    if x == guessed:
        print("Congratulations you did it in ",count," try")
        break
    elif x > guessed:
        print("You guessed too small!")
    elif x < guessed:
        print("You guessed too high!")

if count >= f:
    print("\nThe number is ",x)
    print("\tBetter Luck Next time!")
//end
