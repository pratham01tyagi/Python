'''######################################## code by pratham tyagi################################################################'''
'''hi this is my 1st coading worksheet in this i will teach python 
we will start with basics first'''
'''##############################################################################################################################'''
#To use PRINT FUNCTION -->
'''print is a function used to print something present in it note that its a function and bellow is the given syntax of it.
also note if we started a string in print function then it must be enclosed in the same type of comas wether ' or " not mixed'''

'''
print("Hello this is Pratham Tyagi")
print()                       
# this will print blank line...
print('Hello this is Pratham Tyagi')
print("hello ","my name is ","pratham tyagi")
print(1+5)
print(10000*7)
print(1001/2)                 
# /--> this will return us the value in float...
print(1001//2)                
# //--> this will return us the value in int format...
'''

'''################################################################################################################################'''
# to use STRINGS -->

'''
print("Hello this is Pratham Tyagi")
print('Hello this is Pratham Tyagi')
print("hello ","my name is ","pratham tyagi")
print("hello "+"my name is "+'pratham "tyagi"')  
# this is called string concatination. Also note i wrote tyagi in "" but at out i have single comas to make python see the difference.
# now we will be storing string in the variable and then using them
name="xyz"
print( 'he is '+'             '+name )
# now we will be storing string in the variable and then using them here variable will be taken as input
name= input("hey! pal, what's your name?")                     # we are taking input for our variable here ...
print( 'he is '+'             '+name )


'''
'''################################################################################################################################'''

#studying about ESCAPE CHARACTER -->

'''
# using split_string (\n) to split line ...
split_string=" Hello this is \n Pratham\n Tyagi"          
print(split_string)

# using tabbed_string(\t) to tabb(provide space) in between...
tabbed_string= "1\t2\t3\t4\t100"
print(tabbed_string)

#trying to use double and single quotes both in the print function with the help of \"\"or \'\'...
# if outer quotes are " then internal quote must be -->\"\"
print("hi!this is 'the king\"pratham tyagi\" the great  '")
# if outer quotes are ' then internal quote must be -->\'\'
print('hi!this is "the king\'pratham tyagi\' the great  "')

# if in some programe we find ourself stuck to find that we need to use use both type of Quotes " and' then we could use """ tripple""" quotes there
print("""hi this is "pratham 'tyagi'the great." """)
# here there is no need of split string as...
variable="""hi
this 
is 
pratham"""
print(variable)
# here there is DO NOT need to split string ,then put \ before them...
variable="""hi \
this \
is 
pratham"""
print(variable)

# using raw string or \\ ...
#have a look at the given bellow print function here \u \t and \n seems to be strings to the compiler hence to clarify this we have 2 ways.
print("C:\Users\timer\notes.txt") 
#1.using raw string(here we put r before starting"")-->
print(r"C:\Users\timer\notes.txt")
#2.using \\ string(here we put \\ in place of \)-->
print("C:\\Users\\timer\\notes.txt")

'''
