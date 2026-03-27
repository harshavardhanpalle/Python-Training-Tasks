# DAY 5 Tasks

print("----- Task 1: User Info Manager (Functions + Dictionary) ------ ")

print()
# as per dictonary is used to store users so we created dict
mydict={}
def create_user(name,age,role):
    mydict ={
        "name" : name.title(),
        "age" : age,
        "role" : role
    }
    return mydict
users =[] # list is created to store the users input
# input from users
users.append(create_user("harsha",24,"Devops"))
users.append(create_user("hari",22,"AI"))
users.append(create_user("vicky",23,"Developer"))

# to print list an to access through the list for loop is used
for user in users:
    print(user)

"""
# ----- OUTPUT -----

----- Task 1: User Info Manager (Functions + Dictionary) ------ 

{'name': 'Harsha', 'age': 24, 'role': 'Devops'}
{'name': 'Hari', 'age': 22, 'role': 'AI'}
{'name': 'Vicky', 'age': 23, 'role': 'Developer'}

"""

print()

print(" ----- Task 2: Dynamic Calculator (*args) -----")

print()

#  * args is agruments that can store n number of inputs ,inputs can be either strings or integers
def calculate_total(*numbers):
        
        total = sum(numbers) # total += num
        average = total/ len(numbers) if numbers else 0
       # print("average of arguments :",average)
        return total,average

total, avg = calculate_total(2, 3, 4, 5, 6, 78, 9)
print("Total:", total)
print("Average:", avg)

"""
 ----- OUTPUT -----
----- Task 2: Dynamic Calculator (*args) -----

Total: 107
Average: 15.285714285714286

"""

        
print()
print("----- Task 3: Keyword Config System (**kwargs)----- ")

print()
# ** kwargs is keyvalue pair arguments ,it can also store n number inputs but only with key : pair

def system_config(**settings):
     for key , value in settings.items():
          print(f"{key} : {value}")

system_config(mode = "debug",version = "1.0")

"""
----- OUTPUT -----
----- Task 3: Keyword Config System (**kwargs)----- 

mode = debug
version = 1.0

"""

print()

print("----- Task 4: Factorial Service (Recursion) -----")

print()

def factorial(n):
     if n == 0 :
          return 1
     if n < 0:
          print("ERROR : factorial not defined in negative numbers ")
          return None
     return n * factorial(n-1)

print(factorial(5)) # 120 = 5 * 4 * 3 * 2 * 1
print(factorial(-1))  
# ERROR : factoriak not defined in negative numbers 
# None
print(factorial(0)) # 1

print()
print("----- Task 5: Memory Optimization (Generator) ----- ")
print()
# it doesn't store everything generates valvue only when needed

def square_list(n) :
     result = []
     for i in range(n):
          result.append(i ** 2)  # for nomal list we use append 
     return result

lst = square_list(5)
print(lst)
print(type(lst))

def square_generator(n):
     for i in range(n):
          yield i * i   # for generator we use yield 
          # yield turns function into genarator means pause function and ....
         #.  .... give one value at a time the continue later

generator = square_generator(5)
print(generator)
print(type(generator))

"""
----- OUTPUT -----
----- Task 5: Memory Optimization (Generator) ----- 

[0, 1, 4, 9, 16]
<class 'list'>
<generator object square_generator at 0x102ef69b0>
<class 'generator'>

"""

print()

print("----- Task 6: Exception Handling Module -----  ")

print()
# not passing parameters because we have been asking user to enter inputs
def divide ():

    try:
        num = int(input("enter your numerator :"))
        den = int(input("enter your denominator :"))
        result = num / den
        print("result :",result)
        return result
    
    except ZeroDivisionError:
         print("error : cannot divide by zero ")
    
    except ValueError:
         print("Error:Invalid input")

    finally :
         print("program completed")

# calling function with out argumnets because we have asking user to enter inputs while executing
divide()

"""
----- OUTPUT -----
----- Task 6: Exception Handling Module -----  

enter your numerator :10
enter your denominator :5
result : 2.0
program completed


enter your numerator :10
enter your denominator :0
error : cannot divide by zero 
program completed


"""

print()

print("----- Task 7: File Handling ----- ")

print()


import os
os.chdir("/Users/harshapalle/Desktop")  # change to folder you can write
with open("team_data.txt", "w") as f:  # mode is W write
    f.write("Hello World") 


users = [
    {"name": "Harsha", "age": 24, "role": "Devops"},
    {"name": "Hari", "age": 22, "role": "AI"},
    {"name": "Vicky", "age": 23, "role": "Developer"}
]

with open("team_data.txt", "w") as file:
    for user in users:
        file.write(f"Name: {user['name']}, Age: {user['age']}, Role: {user['role']}\n")


with open("team_data.txt", "r") as file:  # read mode
    for line in file:
        print(line.strip())

print(file.closed) # TRUE

"""
----- OUTPUT -----


----- Task 7: File Handling ----- 

Name: Harsha, Age: 24, Role: Devops
Name: Hari, Age: 22, Role: AI
Name: Vicky, Age: 23, Role: Devloper
True

"""
