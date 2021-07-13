###########################################################################################################################################
#                                                    if statment
#else could be only one but elif could be many.
'''
name = input("hi! what's your name?")
age = int(input(f"what is your age {name}"))
if age >=18:
    print(f"{name} you can vote!")
else:
    print("sorry {0} come after {1} years".format(name ,18-age))
print("Thanks for visiting")

# this is how to use if statment also note syntax is 
#if condition :
#          statments
#else:
#         statments
'''
###########################################################################################################################################
#                              elif statment & nesting of if else
name = input("hi! what's your name ? ")
age = int(input(f"what is your age {name}"))
if age >18:
    print(f"{name} you can vote!")
elif age == 18:
    voterid=input( f"do you have your VOTER ID with you {name}")
    if  'yes' in voterid:
        print("you can vote!")
    else:
        print(f"{name} vait for your VOTER ID")
else:
    print("sorry {0} come after {1} years".format(name ,18-age))
print("Thanks for visiting")

# this is how to use if statment also note syntax is 
#if condition :
#          statments
#elif:
#         statments
#else:
#         statments