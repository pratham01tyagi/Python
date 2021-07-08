##########################################################################################################################################
#                                                    DATA TYPE
'''
PYTHON HAVE SEVERAL BUILT-IN DATA TYPES, THAT CAN BE CLASSIFIED AS -
1.NUMERIC
2.ITERATION
3.SEQUENCE(WHICH ARE ALSO ITERATION)
      3.1 string type
      3.2 list
      3.3 tuple
      3.4 range
      3.5 bytes & bytearray.
4.MAPPING
5.FILE
6.CLASS
7.EXCEPTION

# Here we will study numeric 1st and also the sequence type--
'''

##########################################################################################################################################
#                                                      NUMERIC DATATYPE
'''
here  we have 3 numeric data types:
1.int 
2.float   eg-2.2222222222 upto 308 decimal  etc.
3.complex 


#NOTE--> we cant use an float in plase of int hence the python is data type specific.
'''

##########################################################################################################################################
#                                                     SEQUENCE DATATYPE
'''
# It is defined as ordered set of items.example- 
#1.In string we have set of char forming a string
#2.In list we have set of int,float,string,even lists itself form a list -->L=[1,2,[3,4,5],6,"hard rock"] here L is a list.
#3.in python Tuples can contain int, float ,str and also other touples also called touple nesting-->t =(1,2,3,4,'int',1.4,2.46)

#because of sequence is ordered, we can use indexing to acess individual items in the sequence.
'''



#                                                 STRING DATATYPE(Sequence datatype part)

'''
#      012345 --------Indexing.
#    -(654321)--------Negative Indexing.  
name= 'XYZGHT'
print(len(name))         #output-6 .this will tell the length of the string
print(name)              #printing whole string
print(name[0])           #printing element at given index no.
print(name[-1])          #output-T .printing element by negative indexing
# it could also be done in different was like-
print(name[1+1])         #output-Z
print(name[1*1])         #output-Y

# Slicing the String-
print(name[0:6])   #output-XYZGHT
#NOTE- here one must note that the last digit 6 wont be printed example-
print(name[0:1])    #output-X
print(name[:1])     #output-X also note here we did't gave start value so its 0 by default same with the end value.
print(name[:])      # output- XYZGHT same concept with end value 

# Slicing the String with negative indexing-
print(name[-1:2])   #output- this will give nothing as it could not give result in reverse.
print(name[2:-1])   #output-ZGH
print(name[-6:-1])


#step in a slice in string-
name='0123456789'
print(name)
print(name[0:6:2])     #output-024
#NOTE- this is called step in a slice here we told python that start selecting string from 0-5 and then told 
#it that now put a slicer at step  2nd position and print 1st position which will give-(024)
print(name[0:6:3])     #output-03
#NOTE- this is called step in a slice here we told python that start selecting string from 0-5 and then told 
# it that now put a slicer at step  3nd position and print 1st & 2nd position which will give-(03)
number="9,123,345;567'789:987"
print(number[1::4])   #this will give us all the dilameters frome data.
# we will study these 3 lines later.
seprator=number[1::4]
values = "".join(char if char not in seprator else " "for char in number).split() # we will study this later. 
print([int(val) for val in values])        #output--[9, 123, 345, 567, 789, 987]


#Slicing Stings Backwords-
name='0123456789'
print(name[9:0:-1])    #output-987654321
print(name[9::-1])     #output-9876543210
string='abcdefghijklmnopqrstuvwxyz'
print(string[25::-1])   #output-zyxwvutsrqponmlkjihgfedcba
print(string[25:0:-1])  #output-zyxwvutsrqponmlkjihgfedcb
print(string[16:13:-1]) #output-qpo
print(string[4::-1])    #output-edcba
print(string[25:17:-1]) #output-zyxwvuts
#OR
print(string[:-9:-1])   #output-zyxwvuts
print(string[-4:])      #output-wxyz


#                                                 STRING OPERATIONS
a='hi1'
b='hi2'
print(a+b)     #OUTPUT-hi1hi2  # ADDING STRINGS
print(a*5)     #OUTPUT-hi1hi1hi1hi1hi1  #MULTIPLYING STRINGS
print(a*5+"helloooo")     #OUTPUT-hi1hi1hi1hi1hi1helloooo
day='friday'      # we will use in opreator to check wether that part of string is there in string or not.
print('day' in day)   #True
print('dey' in day)   #False
print('fri' in day)   #True
print('thu' in day)   #False


#                                                  STRING REPLACEMENT FIELD
no=12
no1=100
print("the no is -"+str(no)+".") 
print(type(no))  
#here using string function we have changed the datatype of "no" from int to str only in print() function temporarily.
#OR 
#-----> this is called string replacement field
print("the no is {0} hello{0}".format(no)) #output-the no is 12 hello12
# here now there is no need to convert the no to string 
print("There are {0} days in {1},{2},{3},{4}.".format(31,"jan","march","may","june"))
#output-There are 31 days in jan,march,may,june. -----> this is called string replacement field
#it could aslo be done as.
print("jan:{2},feb:{0},march{2},april{1}.".format(29,30,31))  #output- jan:31,feb:29,march31,april30.
#OR
print("""
jan:{2}
feb:{0}
march:{2}
april:{1}.
""".format(29,30,31))
#output-
#jan:31
#feb:29
#march:31
#april:30.


#                                             STRING FORMATING
for i in  range(1,10):
    print("no {0} squared is {1} and cubed is {2}".format(i,i**2,i**3)) 
    #i**N means i to the power N.
    #     
#output-
#no 1 squared is 1 and cubed is 1
#no 2 squared is 4 and cubed is 8
#no 3 squared is 9 and cubed is 27
#no 4 squared is 16 and cubed is 64
#no 5 squared is 25 and cubed is 125
#no 6 squared is 36 and cubed is 216
#no 7 squared is 49 and cubed is 343
#no 8 squared is 64 and cubed is 512
#no 9 squared is 81 and cubed is 729

#----------------------------------------------------------------------------

for i in  range(1,10):
    print("no {0:2} squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3)) 
    #here NOTE that we have written{0:2},{1:4} here 0,1 are the .format no but 2,4 are the field width to make space 
    #and help the data look clean as shown bellow also it could be {0:3},{0:10}any no depending on space wanted.

#output- (here the values are right aligned by default)
#no  1 squared is    1 and cubed is    1
#no  2 squared is    4 and cubed is    8
#no  3 squared is    9 and cubed is   27
#no  4 squared is   16 and cubed is   64
#no  5 squared is   25 and cubed is  125
#no  6 squared is   36 and cubed is  216
#no  7 squared is   49 and cubed is  343
#no  8 squared is   64 and cubed is  512
#no  9 squared is   81 and cubed is  729

#--------------------------------------------------------------------------------------------

for i in  range(1,10):
    print("no {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i,i**2,i**3)) 
    #here we have put < symbole before 2,3,4 to make values present there left aligned.

#output-
#no 1  squared is 1   and cubed is 1
#no 2  squared is 4   and cubed is 8
#no 3  squared is 9   and cubed is 27
#no 4  squared is 16  and cubed is 64
#no 5  squared is 25  and cubed is 125
#no 6  squared is 36  and cubed is 216
#no 7  squared is 49  and cubed is 343
#no 8  squared is 64  and cubed is 512
#no 9  squared is 81  and cubed is 729

#------------------------------------------------------------------------------------------------

for i in  range(1,10):
    print("no {0:^2} squared is {1:^3} and cubed is {2:^5}".format(i,i**2,i**3)) 
    #here we have put ^ symbole before 2,3,4 to make values present there center aligned.

#output-
#no 1  squared is  1  and cubed is   1
#no 2  squared is  4  and cubed is   8
#no 3  squared is  9  and cubed is  27
#no 4  squared is 16  and cubed is  64
#no 5  squared is 25  and cubed is  125
#no 6  squared is 36  and cubed is  216
#no 7  squared is 49  and cubed is  343
#no 8  squared is 64  and cubed is  512
#no 9  squared is 81  and cubed is  729


print("value of pi is-{0:12}".format(22/7))
#output-value of pi is-3.142857142857143
# general format it vill give upto 15 decimal places.
print("value of pi is-{0:12f}".format(22/7))
#output-value of pi is-    3.142857
#Her upto 6 decimal places due to f.
print("value of pi is-{0:12.30f}".format(22/7))
#output-value of pi is-3.142857142857142793701541449991
#this will give upto 30 decimal places. here we are giving field value but precision of 30 is also needed 
print("value of pi is-{0:12.50f}".format(22/7))
#output-value of pi is-3.14285714285714279370154144999105483293533325195312
#here value upto 50 decimal places are given. with only 12 field value. HERE PRECISION IS GIVEN IMPO. OVER FIELD WIDTH.
print("value of pi is-{0:52.50f}".format(22/7))
#output-value of pi is-3.14285714285714279370154144999105483293533325195312
#as here the field width is 50< the effect will start. as done in bellow examples. here both precision and F.width are taken care of.
print("value of pi is-{0:72.50f}".format(22/7))
#output-value of pi is-                    3.14285714285714279370154144999105483293533325195312
print("value of pi is-{0:92.50f}".format(22/7))
#output-value of pi is-                                        3.14285714285714279370154144999105483293533325195312

#NOTE- we can even make these long numeric values to be at right side by putting{0:<92.50}


#                                        FORMATED STRING(F-strings)
# it is defined by putting the the letter f before the opening quotes.
# it is alo a way to format the strings.
name='tim'
age=12
#print(name+"is"+age+"years old")
#if we will print above statment it will give error hence we would put the f before "" and put variable into {} as shown bellow.
print(name+ f" is {age} years old")    # no need to write .format() now.
#output-tim is 12 years old
print(type(age)) #output-<class 'int'>
print(f"the value of pi is -{22 / 7:12.50}")
#output-the value of pi is -3.1428571428571427937015414499910548329353332519531
'''

#                                     STRING INTERPOLATION
# it is alo a way to format the strings.
# this is similar to C programing.
name='tim'
age=12
print(name+" is %d years old"%age)
#output - tim is 12 years old
age=12.003
print(name+" is %f years old"%age)
#output-tim is 12.003000 years old
age=24
major="years"
minor="months"
print("my age is %d%s,%d%s"%(age,major,6,minor))
#output-my age is 24years,6months
print("PI value is %f"%(22/7))
#output-PI value is 3.142857
print("PI value is %60.30f"%(22/7))
#output-PI value is                             3.142857142857142793701541449991

#NOTE--> visit Python library refrance to study about string formatting operations. 

########################################################################################################################################