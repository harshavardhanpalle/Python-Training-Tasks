# Day 2 Tasks
#Bitwise Operator Tasks (1–8)

#Create two variables a = 10 and b = 6.
print()
print("----- Bitwise Operator Tasks (1 - 8)-----")
a = 10
b = 6
print(a&b) # bitwise AND 10(1010)

#Create two variables x = 12 and y = 5.
x = 12
y = 5
print(x|y) #bitwise OR 12(1100) | 5(1010) = 13(1101))

#Create a variable num = 8
num = 8
result = ~num #bitwise not ~8 (1000) = -9
#here 0 -> 1 and 1-> 0 and Bitwise NOT flips all bits in Python ~n = -(n + 1)
print(result) # -(num + 1)= -9


#Create two variables a = 15 and b = 9.
a = 15 
b = 9
#bitwise Xor 15(1111) XOR 9(1001) = 6(0110)
print(a^b) # here same ^ same  = 0 and diff ^diff = 1

#Create a variable num = 7.
num = 7
result =num << 2 # left shift by 2 ,7 << 2 = 28 (0111 << 2 = 11100)
print(result)

##Create a variable num = 20
num = 20
result = num >> 1 #right shift by 1 .20(10100) >> 1= 10(00101) 
print(result)


#Take two numbers from user input and print AND result.
num1 = int(input("Enter first number: "))
num2 = int(input("enter second number :"))
result = num1 & num2 # AND  = &
print(result)


#ake two numbers from user input and print XOR result.

n1 = int(input("Enter first number: "))
n2 = int(input("enter second number :"))
res = n1  ^ n2 #xor = ^
print (res)

"""
      OUTPUT
----- Bitwise Operator Tasks (1 - 8)-----
2
13
-9
6
28
10
Enter first number: 10
enter second number :2
2
Enter first number: 3
enter second number :5
6
"""

print()

print("-----String Tasks (9 - 14)-----")

print()
#Create a string "hi" and print it 4 times using replication.
str = "hi"
print( str * 4) 

#Create a string "python" and print it 3 times.
str2 ='python'
print(str2 * 3)

#Create two strings "super" and "man" and combine them using + operator.
str1 = "Super"
str2 = "man"
print(str1 + str2) #print("super" + "man")

#Create three strings "hello", " ", "world" and print "hello world".
str1 = "hello"
str2 = " "
str3 = "world"
print(str1 + str2 + str3) # here python will not create space so we defined empty space here
# print("hello " +" " + "world")

#Take a name from user input and print it 5 times.
name = (input("enter your name :"))
print(name * 5)

#Take two strings from user input and concatenate them.
s1 = input(" enter first string: ")
s2 = input("enter second string: ")
print(s1 + s2) # or this can be like print(s1 = " " + s2) for any space required


"""
OUTPUT
-----String Tasks (9 - 14)-----

hihihihi
pythonpythonpython
Superman
hello world
enter your name :harsha
harshaharshaharshaharshaharsha
 enter first string: the
enter second string: stackly
thestackly


"""
print()

print("-----Input & Type Casting Tasks (15–20)-----")

print()

#Take a name from user input and print its data type.
name = input("enter your name :")
print(type(name))

#Take age from user input and convert it into integer.
age = input("enter your age: ")
result = int(age)
print(result)
print(type(result))

#Take two numbers from user input and print their sum.
num1 = int(input("enter number 1: "))
num2 = int(input("enter second 2:"))
sum = num1 + num2
print(sum)

#Take two marks from user input and print their average.
mark1= float(input("enter mark 1:"))
mark2= float(input("enter mark 2:")) # here float is considered because if any half mark given
average = (mark1 +mark2) / 2
print(average)

#Take two numbers from user input and print 3*a*2 + b - 2.
a = int(input("enter number a  = ")) 
b = int(input("enter number b ="))
print(3*a*2 + b - 2)

#Take a number from user input and print its data type before and after type casting.
num = input(" enter your number :")
print(type(num) )
result = int(num) # typecasting from str to int 
print(type(result))

"""
OUTPUT
-----Input & Type Casting Tasks (15–20)-----

enter your name :harsha
<class 'str'>
enter your age: 23
23
<class 'int'>
enter number 1: 10
enter second 2:10
20
enter mark 1:10
enter mark 2:20.5
15.25
enter number a  = 3
enter number b =2
18
enter your number :10
<class 'str'>
<class 'int'>
"""

print()
print("----- Unit Digit Tasks (21–25) -----")

print()
# 21.Take a number as string input and print the last digit.
number = input("enter your number :")
result = number[len(number)- 1] #bye using negative indexing number [-1]
print("last digit:",result) # print(number[-1]) can also give us last digit


#22.Take a number and print the unit digit using % operator.
num = int(input("enter your number :"))
unit  =  num %10 # here modules is used to get remainder which is unit digit
print("unit digt :",unit) 

#23.Take a number and remove the last digit using // operator.
num = int(input("enter number : "))
res = num  // 10
print(" Removed last  digit:",res)

#24.Take a number and print the second last digit.
num = int(input("enter your number :"))
second_last = (num //10) % 10
print(second_last) 

#25.Take a 5 digit number and print its last digit.
num = int(input("enter your 5 digit number :"))
lastdigit = num % 10 
print("last digit:",lastdigit)

"""

OUTPUT 
----- Unit Digit Tasks (21–25) -----

enter your number :2345
last digit: 5
enter your number :5432
unit digt : 2
enter number : 23457
 Removed last  digit: 2345
enter your number :9823
2
enter your 5 digit number :12345
last digit: 5
"""

print()

print("-----If Statement Tasks (26–30)-----")

print()
#26.Create a program that checks if 10 ≥ 5 and prints a message.

if 10 >= 5:
    print("10 is greater than or equal to 5")


#27.Take a number from user input and check if it is greater than 50.
num = int(input("enter a number :"))
if num > 50:
    print("the number is greater than 50")
else :
    print("the number is less than 50  or equal to 50")

#28.Take age from user input and check if age ≥ 18.
age = int(input("enter your age :"))
if age >= 18:
    print("your age is greater than or equal to 18")
else :
    print("you age is less than 18 ")

#29.Take a number and check if it is greater than 100.
num = int(input("enter a number :"))
if num > 100:
    print("the number is greater than 100")


#30.Take a number and check if number ≥ 0.
num = int(input("your number :"))
if num >=0 :
    print("your number is greater than  or equal to 0")
 
 """
 OUTPUT

-----If Statement Tasks (26–30)-----

10 is greater than or equal to 5
enter a number :55
the number is greater than 50
enter your age :19
your age is greater than or equal to 18
enter a number :101
the number is greater than 100
your number :2
your number is greater than  or equal to 0
"""

print()

print("-----If-Else Tasks (31-34) -----")

print()

#31.Take a number and check if it is even or odd.
num = int(input("enter a number :"))
if num % 2 == 0:
    print("the number is even ")
else : print("number is odd")


#32.Take marks from user input and check if pass or fail (pass ≥ 35).
marks = float (input(" enter your marks :"))
if marks >= 35 :
    print("you are pass and marks are greater than  or equal to 35")
else :
    print("you are fail and marks are less than 35 ") 


#33.Take a number and check if it is positive or negative.
num = int( input("enter number :"))
if num > 0 :
    print("number is positive or greater than 0")
else :
    print("number is negative")

#34.Take a number and check if it is greater than 10 or not.
num = int(input("enter nnumber :"))
if num > 10:
    print("number is greater than 10")
else:
    print("number is less than or equal to 10")
"""
OUTPUT

-----If-Else Tasks (31-34) -----

enter a number :3
number is odd
 enter your marks :35
you are pass amd marks are greater than  or equal to 35
enter number :-1
number is negative
enter nnumber :11
number is greater than 10
"""

print()

print("-----Nested If Tasks (35 - 37)-----")

print()
##35.Create a program for job eligibility:
age = int(input("enter age:"))
height = float(input("enter height in cm :"))
weight = float(input("enter weight  in kg even grams:"))

if age >=18:
    if height >= 160:
        if weight >= 60:
            print("you are eligible for this job")
        else:
            print("You are not eligible for this job: weight too low")
    else:
        print("You are not eligible fot this job: height too low")
else :
    print("you are not eligible for this job")
    

#36.Create a college admission program:
marks = float(input("enter your marks :"))
age = int(input("enter age:"))
if marks >= 60:
    if age >= 17:
        print("you are eligible for college admission")
    else:print("you arer not eligible for admission : age is low")
else:
    print("you are not eligible for college admission :marks are low")


#37.Create a sports selection program:

age = int(input("enter age:"))
height = float(input("enter height in cm :"))
weight = float(input("enter weight  in kg even grams:"))

if age >=16:
    if height >= 150:
        if weight >= 50:
            print("you are eligible for this sports selection")
        else :
            print("you are under weight")
    else:
        print("you height doesnt meet selection process")
else :
    print("you are not eligible for this sports selction ,age is low")

"""
OUTPUT

-----Nested If Tasks (35 - 37)-----

enter age:19
enter height in cm :165
enter weight  in kg even grams:65
you are eligible for this job
enter your marks :56
enter age:18
you are not eligible for college admission :marks are low
enter age:16
enter height in cm :155
enter weight  in kg even grams:51
you are eligible for this sports selection
    
"""
print()

print("-----Match Statement Tasks (38 - 40)-----")

print()

#38.Take a number (1-7) and print day name using match.
day = int(input("enter your day :"))
match day:
    case 1 :print("Monday")
    case 2 :print("tuesday")
    case 3 :print("wednesday")
    case 4 :print("thursday")
    case 5 :print("Friday")
    case 6 :print("saturday")
    case 7 :print("sunday")
    case _:
        print("invalid number")

        
#39.Take a number (1-3) and print: 1 → Red 2 → Blue 3 → Green
number = int(input("enter your numberr :"))
match number :
    case 1: print("red")
    case 2: print("blue")
    case 3: print("green")
    case _:
        print("you number is greater than 3 ") 

#Take a number (1-4) and print: 1 → Apple 2 → Mango 3 → Orange 4 → Banana

number = int(input("enter your number :"))
match number :
    case 1: print("Apple")
    case 2: print("Mango")
    case 3: print("Orange")
    case 4: print("Banana")
    case _:
        print("invalid number")

"""
 OUTPUT
-----Match Statement Tasks (38-40)-----

enter your day :2
tuesday
enter your numberr :3
green
enter your number :4
Banana

"""