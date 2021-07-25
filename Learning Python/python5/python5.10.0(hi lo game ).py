###############################################################################################################
#                                          Hi Lo GAME
low = int(input("enter the lowest value you want to enter."))
high = int(input("enter the highest value you want to enter."))
print(f"bro think of a no b/w {low}-{high}")
input("hit enter")
guess= low
while True:
    guess = low+(high-low)//2
    hi_lo= input(f"bro i thought of {guess}."
                  "if you want me to think high or low enter "
                 "h or l or if i was right pal then enter c".casefold())
    if hi_lo == 'h':
        #here lower will become guess + 1
        low= guess+1
    elif hi_lo == 'l':
        high = guess -1
        #here higher is guess -1
    elif hi_lo == 'c':
        print("i was born to be a genius i know. as you guessed such a silly no {0}".format(guess))
        break
    else:
        print("mr.dum enter between 'h' 'l' or 'c' otherwise i will KYA..." )
    guess += 1
# in python we dont have case or switch statments.
# also if we are getting a syntax error and we write "pass" there than the error will be gone.
