# Day 03 Python traninig tasks
print()
# Task :

print("----- Section 1: Loop Basics (1-10)------")

print()
# 1.Print numbers from 1 to 50 using for loop

for i in range(1,51): # (start ,stop)
    print(i, end= " ")

print()
print()
#2. Print even numbers from 1 to 100
for i in range(1,101): # or can belike (2,101,2) {start,stop,step}
    if i % 2==0:
        print(i,end= " ")

print()
print()
#3.Print odd numbers from 1 to 100:
for i in range(1,101): # like (1,101,2) (start,stop,step)
    if i % 2 == 1:
        print(i,end=" ")

print()    
print()
#4.Print multiplication table of 7
for i in range(1,11):
    print (f"7 * {i} = {7 * i}")

print()
#5.Find sum of numbers from 1 to 100
n = 100
sum = n*(n+1)/2  #here it add the all number from 1 to 100
print(sum) #5050.0

print()
#6.Print numbers in reverse from 50 to 1
for i in range(50,0,-1):
    print( i, end=" ")

print()
print()
#7.Count how many numbers are divisible by 3 (1–100)
a=[] #count=0
for i in range(1,101):
    if i % 3 ==0:
        a.append(i) #count+= 1
print(len(a)) #33 #print(count)

#8.Print squares of numbers from 1 to 10
for i in range(1,11):
    print(i **2,end=" ")

print()
print()
#9.Print cube of first 10 numbers
for i in range(1,11):
    print(i ** 3, end=" ")

print()
print()
#10.Take input n, print numbers from 1 to n
n = int(input("enter your number:"))
for i in range(1,n):
    print(i, end=" ")
"""
#.   OUTPUT

----- Section 1: Loop Basics (1-10)------

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 

1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 

7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
7 * 10 = 70

5050.0

50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 

33
1 4 9 16 25 36 49 64 81 100 

1 8 27 64 125 216 343 512 729 1000 
enter your number:23
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
"""
print(end="\n\n")

print("-----Section 2: While Loop (11 - 15)-----")

print()
#11.Print numbers from 1 to 20 using while
i=0
while i < 21:
    print(i,end=" ")
    i = i+1

print(end="\n\n")

#12.Find factorial of a number using while
n = int(input("enter number:"))
fact = 1
i = 1
while  i <=n :
    fact = fact*i # 3 * (3-2)= 3*2=6 or n *(n-1)*1 
    i=i+1 # increment for the loop
print(f"factorial of {n} is {fact}")

#13.Reverse a number using while
num = 1234
rev=0
while num>0:
    digit = num %10
    rev = rev *10 +digit
    num = num //10
print("reverse order :",rev) #4321

#14.Count digits in a number
count = 0
number = 123456
while number > 0:
    number = number //10
    count +=1
print("number of digits :",count)

#15:Keep asking input until user enters "stop"
while True:
    user_input = input("enter you number( type 'stop' to quit):")
    if user_input.lower()=="stop":
        print("stop the program or loop")
        break
    print(f"you input entered :{user_input}")
"""
#OUTPUT
-----Section 2: While Loop (11 - 15)-----

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

enter number:3
factorial of 3 is 6
reverse order : 4321
number of digits : 6
enter you number( type 'stop' to quit):a
you input entered :a
enter you number( type 'stop' to quit):d
you input entered :d
enter you number( type 'stop' to quit):b
you input entered :b
enter you number( type 'stop' to quit):e
you input entered :e
enter you number( type 'stop' to quit):g
you input entered :g
enter you number( type 'stop' to quit):f
you input entered :f
enter you number( type 'stop' to quit):stop
stop the program or loop

"""
print()

print("-----Section 3: Nested Loop (16–20)-----")
print()
# 16 Print Pattern:

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end='')
    print( )
    
print()
#17.print Pattern
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

print()
#18. Print multiplication table (1 to 5) using nested loop
print(" multiplication table (1 to 5)")
for i in range(1,6):
    print( end='\n')
    for j in range(1,11):
        print(f"{i} * {j} = {i * j}")
print()

#19.print abc
for i in range(1,4):   
    for j in["A","B","C"]:
        print(j,end='')
    print()

print()
#20.print
num = 1
for i in range(3):
    for j in range(3):
        print(num , end="")
        num +=1
    print( )
"""
#. OUTPUT
-----Section 3: Nested Loop (16–20)-----

*
**
***
****

1
12
123
1234

 multiplication table (1 to 5)

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
1 * 10 = 10

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20

3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
3 * 10 = 30

4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
4 * 10 = 40

5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

ABC
ABC
ABC

123
456
789

"""
print()

print("-----Section 4: String Basics (21–25)-----")
print()

#21.Count total characters in a string
string = "harshavardhan"
count= 0
for i in string:
    
    count = count+1
print("no of characters: ", count) #len(str) #13

#22.count vowels in a string
strr= "acbaeiouhar"
vowel = ['a','e','i','o''u']
count = 0
for char in strr:
    if char in vowel:
        count += 1

print("no of vowels :",count)


#23 .Count consonants in a string
strr= "acbaeiouhar"
vowel = ['a','e','i','o''u']
count = 0
for char in strr:
    if char.isalpha() and char not in vowel:
        count += 1

print("no of Consonants :",count)

#24 : reverse a string using loop
string = "nahdravahsrah" 
#rev= " "
for i in string[::-1]:  # for i in string #rev = i+rev
    print(i,end='')

print()
# 25 :Check if string is palindrome
s= input("enter :")
#s = "madam"

if s ==s[::-1]:
    print("palindrome")
else :
    print("not palindrome")
"""
#OUTPUT
-----Section 4: String Basics (21–25)-----

no of characters:  13
no of vowels : 5
no of Consonants : 6
harshavardhan
enter :122221
palindrome

"""
print()
print("-----Section 5: String Slicing (26–30)-----")
print()

#26.Print first 5 characters of a string
string ="Harshavardhan"
print(string[0:5]) #Harsh

#27 Print last 3 characters
print(string[-3:]) #han

#28.Print string in reverse using slicing
print(string[::-1])

#29.#Print every 2nd character
print(len(string))#(start,stop,step)
print(string[0::2]) # stop we don,t know so left it as empty

#30 .Remove first and last character from string

print(string[1:-1])

"""
#OUTPUT
-----Section 5: String Slicing (26–30)-----

Harsh
han
nahdravahsraH
13
Hrhvrhn
arshavardha

"""

print()
print("-----Section 6: List Basics (31–35)-----")
print()

#31.Create a list of 5 numbers and print sum
lst = [1,4,56,7,8]
total=0
for i in lst :
    total += i
print(total) 
print("sum of number in list:",sum(lst))

#32 :Maximun value in list
print("maximun value:",max(lst))

#33.Minimun value in list
print("minimum value :",min(lst))

#34.count total elements in list
count = 0
for i in lst:
    count += 1
print(count) #len(lst)

#35 check if element exists in list
x = 1
if x in lst:
    print("yes in list")
else:
    print("not in list")

"""
#OutPut
-----Section 6: List Basics (31–35)-----

76
sum of number in list: 76
maximun value: 56
minimum value : 1
5
yes in list
"""


print()
print("-----Section 7: List Operations (36–40)-----")
print()

#36Add 3 elements using append()
list =[ ]
a= list.append(2)
b= list.append(4)
c= list.append(7)
print("list add with 3 elemtnts: ",list)

#37 Insert element at specific index

d = list.insert(2,20)
print("20 is inserted with indexing:",list)

#38 Remove element using remove()
numbers = [1, 2, 10, 3, 4, 5]
numbers.remove(10)   # removes the first occurrence of 10
print(numbers)


#39 Reverse list without using .reverse(

print(numbers)
print("revered list:",numbers[::-1])


#40 Sort list without using .sort()
list = [5, 2, 9, 1, 7]

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i] ,list[j]= list[j] ,list[i]

print('sorted list:',list)
"""
#output
-----Section 7: List Operations (36–40)-----

list add with 3 elemtnts:  [2, 4, 7]
20 is inserted with indexing: [2, 4, 20, 7]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
revered list: [5, 4, 3, 2, 1]
sorted list: [1, 2, 5, 7, 9]

"""