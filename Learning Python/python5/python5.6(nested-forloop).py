###############################################################################################################
#                                   NESTED FOR LOOP
'''
for i  in range(1,5):
    for j in range (1,3):
        print(f"this is i-{i}this is j-{j}this is i*j-{i*j}")
    print("************************************") 

#output-
#this is i-1this is j-1this is i*j-1
#this is i-1this is j-2this is i*j-2
#************************************
#this is i-2this is j-1this is i*j-2
#this is i-2this is j-2this is i*j-4
#************************************
#this is i-3this is j-1this is i*j-3
#this is i-3this is j-2this is i*j-6
#************************************
#this is i-4this is j-1this is i*j-4
#this is i-4this is j-2this is i*j-8
#************************************


###########################################################################################################
#                                          CONTINUE
shopping_list=['milk','chocklate','bread','weed','mariona']

for i in shopping_list:
    print("buy "+i)

#output-
#buy milk
#buy chocklate
#buy bread
#buy weed
#buy mariona

#NOTE- now we will try to use "continue" 

for i in shopping_list:
    if i == 'weed':
        print("no not weed")
        continue #after this line compiler will go to for i in ... line.
    print("buy "+i) # it will continue tis untill weed comes.
    print("*************************************************")

#output-
#buy milk
#*************************************************
#buy chocklate
#*************************************************
#buy bread
#*************************************************
#no not weed
#buy mariona
#*************************************************


########################################################################################################
#                                     BREAK
for i in shopping_list:
    if i == 'weed':
        print("no not weed")
        break #after this line compiler will go to for i in ... line. and circuit will break.
    print("buy "+i) # it will continue tis untill weed comes. aftr weed list will be terminated.
    print("*************************************************")

#output-
#buy milk
#*************************************************
#buy chocklate
#*************************************************
#buy bread
#*************************************************
#no not weed

'''
#NOTE-now we will look at what position the index was.

shopping_list=['milk','chocklate','bread','weed','mariona']
item_to_find = 'weed'
position = None  # none here is a constant that represents nothing.

for index in range (len(shopping_list)):
    if shopping_list[index] == item_to_find:
        position = index
        print(f"the position is {position}")
#output- the position is 3

shopping_list=['milk','chocklate','bread','weed','mariona']
item_to_find = 'weed'
position = None  # none here is a constant that represents nothing.
if item_to_find in shopping_list:
        position = shopping_list.index(item_to_find)
        print(f"the position is {position}")
#output- the position is 3