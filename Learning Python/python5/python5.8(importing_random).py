###############################################################################################################
#                                    RANDOM & IMPORT

import random
highest = int(input("enter the highest range :"))
ans = random.randint(0, highest)
#here we are calling "randint" function from "random" module by dot notation.

guess = 0
print(f"enter no betwen 0 to {highest} ")
while guess != ans:
        guess = int(input(f"enter no"))
        if guess == ans:
            print(f"you guessed it right the answer is {ans}")
        else:
            if ans<guess:
                print("guess low")
                
            else:
                print("guess high")
                

                
            
            
            
