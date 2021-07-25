##############################################################################################################
#                               AUGIMENT_ASSINGMENT
# It's a shorthand way of assigning values to a variable.
# the combination, in a single statment, of a binary operation and an assingment statment.

#NOTE-the line guess+=1 is same as guess = guess +1 
#but more efficient than guess = guess +1 hence if we are operating it in a loo for million times than 
#it could lead to a delay of a second hence the 1st way is more efficient.


a=10
b='b'
# some augmented assingments-->

#NOTE- run each assingment seprately.
a +=1 
print(a)        # 11

a -=1 
print(a)        #9

a *=2            #20
print(a)

a /=3             #3.33333333...conversion from int to float.
print(a)

a //=2
print(a)          #5


a **=2            #100-as it raise 10^2--still represents a float.

print(a)

a %=2             # is exactly divisible by 2
print(a)

b*=5
print(b)           #it will print b 5 times.

b+='c'
print(b)           #bc
