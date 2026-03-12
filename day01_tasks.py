#. Day 1 Python_Training _Tasks
print()
#Task 1 – Print Formatting

print("-----Print Formatting-----")
print ("Hello","World","Welcome","Python", end="  \n")
print("Laptop","Mouse","Keyboard",sep= " | ")

print()
#Task 2 – Variables

print("-----Variables-----")
name = "Ravi"
age = 22
city = "Chennai"
print( name ,age,city ,sep= "-" )

print()
#Task 3 – Multiple Assignment

print("-----Multiple Assignment-----")
"""name = "Meena"
age = 20
student  = True"""

name ,age, student = "Meena" ,20,True
print(name,age,student)

print()
#Task 4 – Indexing

print("-----Indexing-----")
# Indexing starts from 0 ..... to ..n-1
word = "Python"
print(word[0]) #first letter  is P index is 0
print(word[2]) #Third letter is  T  index is 2
print(word[-1]) #last letter is n  
""" This can also be done like [len(word) - 1] """

print()
#Task 5 – Arithmetic Operators

print("-----Arthmetic Operators-----")

a = 25 + 10 ; print(a) # addition
b = 50 -20 ; print(b) # subtraction
c = 8 * 5 ; print(c)  # multiply
d = 100 /10 ;print(d) #division
e = 10 % 3 ; print(e)  # Gives Remainder
f = 2**4 ; print(f) # exponent
g = 20 // 3 ; print(g) #floor division gives only integer values


print()
# Task 6 – BODMAS Expression

print("-----BODMASS Expression-----")

print(3+2*5**2)
"""Here 5**2 = 25 and 2 *25 = 50 and 50 + 3 = 53"""

print()
#Task 7 – Assignment Operator

print("-----Assignment Operator-----")
num = 50
num += 25 #num = num+ 25 ,num = 50 + 25 = 75
print(num)

num1 = 100
num1 /= 10
print(num1) # num1 = num1 / 10 = 100/10 = 10.0

print()
#Task 8 – Comparison Operators

print("-----Comparison Operators-----")

print(10 > 5) #True
print(20 < 15) #False
print(5 == 5) # true 
print(10 != 8) # True
print(7 >= 7)#true
print(6 <= 2) #false

print()
#Task 9 – String Comparison

print("-----String Compariosn-----")
a = "apple"
b = "Apple"
print( a == b ) #false
""" Because python is case sensitive and a == A  is False 
     as ASCII values
     a = 97 and A = 65 
     a(97 )!= A(65) """

print()
#Task 10 – Logical Operators
print("-----Logical Operators-----")

print(10>5 and 5==5) # True and true = true
print(5 > 10 or 10 == 10) # false or true = true
print(not(5 > 2)) #not(true) = false


print()
#Task 11 – Membership Operator

print("-----Membership Operator-----")
numbers = [10,20,30,40,50]
print(20 in numbers) #true
print( 60 in numbers) #false
print(30 not in numbers) #false

print()
#Task 12 – Swap Variables

print("-----Swap Variables-----")
a = 10
b = 20
 #swap using single line swap
a,b = b,a
print("a = ",a)
print("b = ",b)
""" temp = a
    a = b
    b = temp
     using temporary variable"""

print()
#Task 13 – Bitwise XOR

print("-----Bitwise XOR-----")
a = 6 
b = 3
""" Here 6 bitwise  is 0110
         3 bitwise is  0011  then when XOR is 5 (0101) 
          ' here same ^ same = 0 ,different ^ different = 1' """

print(a ^ b)


print()

"""----OUTPUT----
-----Print Formatting-----
Hello World Welcome Python  
Laptop | Mouse | Keyboard

-----Variables-----
Ravi-22-Chennai

-----Multiple Assignment-----
Meena 20 True

-----Indexing-----
P
t
n

-----Arthmetic Operators-----
35
30
40
10.0
1
16
6

-----BODMASS Expression-----
53

-----Assignment Operator-----
75
10.0

-----Comparison Operators-----
True
False
True
True
True
False

-----String Compariosn-----
False

-----Logical Operators-----
True
True
False

-----Membership Operator-----
True
False
False

-----Swap Variables-----
a =  20
b =  10

-----Bitwise XOR-----
5

"""
