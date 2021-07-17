####################################################################################################################
#                                   FOR LOOP

name = 'harry'
for character in name:
    print(character)

#output-
#h
#a
#r
#r
#y

##############################################################################################################
#                                 STEPPING USING FOR LOOP
'''
no = "9,233;372:036 854,775;807"
seprator = ""

for char in no:
    if not char.isnumeric():
        seprator = seprator + char
print(seprator)
values = "".join(char if char not in seprator else " " for char in no).split()
print([int(val) for val in values])
#output-
# ,;: ,;
#[9, 233, 372, 36, 854, 775, 807]


no = input("enter the no series with seprator you want")
seprator = ""

for char in no:
    if not char.isnumeric():
        seprator = seprator + char
print(seprator)
values = "".join(char if char not in seprator else " " for char in no).split()
print(sum([int(val) for val in values]))
#here we added sum() before int which will print the sum of all the numbers.
'''
##############################################################################################################
#                                 ITERATING OVER RANGE IN LOOP

for i in range(1,5):
    print( f"the value of i is - {i}" )

#output-
# the value of i is - 1
# the value of i is - 2
# the value of i is - 3
# the value of i is - 4

# NOTE- here the last letter in the range is not printed that means when range was 1to5 it printed 4 times only.

for i in range(1,5):
    print( f"the value of i is - {i}" )

#output-
# the value of i is - 1
# the value of i is - 2
# the value of i is - 3
# the value of i is - 4

for i in range(5,1):
    print( f"the value of i is - {i}" )

#output- there will be no output.


for i in range (0,10,2):
    print( f"the value of i is - {i}" )
#output- this will slice the range and give the 2nd value consecutively.
#the value of i is - 0
#the value of i is - 2
#the value of i is - 4
#the value of i is - 6
#the value of i is - 8

#moving backwards
for i in range (10,0,-2):
    print( f"the value of i is - {i}" )
#output-
#the value of i is - 10
#the value of i is - 8
#the value of i is - 6
#the value of i is - 4
#the value of i is - 2

#NOTE- we have done sone code before where we wrote 16 <=age<=65 but the correct way to do that is
#for age in range (16,66):
