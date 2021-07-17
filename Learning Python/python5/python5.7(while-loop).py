##############################################################################################################
#                                             WHILE LOOP
'''
syntax-->
while<condition>:
    execute block of code
'''
'''
i=0
while i <6:
    print(f"value of i is {i}")
    i+=1
#output-
#value of i is 0
#value of i is 1
#value of i is 2
#value of i is 3
#value of i is 4
#value of i is 5

list=['1','2','3','4.0',"5","six"]
value=""
while value not in list:
    value = input("try it again")
    if value =="bye":
        print("game over")
        break
print("you are out")

#output1-
# try it again5
#you are out

#output2-
#try it again ESC
#game over
#you are out

#output3-
#try it againbye
#game over
#you are out

#NOTE- python is case sensitive. 
'''