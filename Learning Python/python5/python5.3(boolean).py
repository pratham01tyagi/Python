###################################################################################################################
#                                             BOLLEAN
'''
bollean can hold only 2 values true or false that is 1 & 0.
also python is case sensitive T means true and F means false.
"not" is used to reverse a bollean value as not true = false.
in bollean also we have precedance of characters as here "and" has high precedance over "or"
'''

temp=50
day= 'a'
raning=True
if temp==50 and day =='a' and not raning:
    print("hello")
else:
    print("bye")
#output-bye

if (temp==50 and day =='a') or not raning:
    print("hello")
else:
    print("bye")
#output-hello


#getting output in bollean
name='tim'
print(name=='tim')
#output-True

# truth value-
'''
any object can be tested for truth value, for use in a if or while condition.
constant sefine to be false are None and False.
0 of any type int decimal or float all are considered as False.
'',{},(),[],set(),range(0) they are also considered as False.
 
'''
name= 'ram'
if name:
    print(f"{name}")
else:
    print("bye")

#####################################################################################################################