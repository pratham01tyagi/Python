#############################################################################################################
#                                      CHECKING IN

'''
name = 'harry'
letter = input("enter your name")
if letter in name:
    print("hi")
else:
    print("bye")
#output1-
#enter your name hi
#bye

#output2-
#enter your name har
#bye

#output3-
#enter your namehar                   # here we entered the har without space hence it gave "hi"
#hi
'''

#############################################################################################################
#                                      NOT IN
'''
activity = input("what would you like to do ")
if "cinema" not in activity:
    print("bye")
else:
    print("welcome")
#output-
#what would you like to do Cinema      # as here "C" is in caps hence this is comming to be bye.
#bye


activity = input("what would you like to do ")
if "cinema" not in activity.casefold():  # .casefold() will convert words in caps to lower and then check
    print("bye")
else:
    print("welcome")

#OUTPUT-
#what would you like to do CINEMA
#welcome
'''