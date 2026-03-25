#  PYTHON TASKS DAY 04

# 1 MINI PROJECT 
print("----- Mini Project 1: Employee Management System -----")
# Concepts: Dictionary, List, Functions
# Build a system to manage employees.

print()
# [ {},{},{}]
# list to store employess(dictonary)
employees=[ ]

# Funtion to add employees

def add_employee(name,age, role, salary) :
    emp = {
        "name" : name,
        "age"  : age,
        "role" : role,
        "salary" : salary
        }
    employees.append(emp)
    print("sucessfully added")



# Store multiple employees (list of dictionaries)
# Each employee: name, age, role, salary
add_employee( "harsha",23,"devops",47000)

# here added new employees 

add_employee("Rahul", 25, "Developer", 55000)
add_employee('hari',22,"Ai",100000)

print(employees)


# Function to update employee
def update_employee(index, key, value):
    if 0 <= index < len(employees):
        employees[index][key] = value
        print("Employee updated successfully!")
    else:
        print("Invalid employee index!")

update_employee (0,"salary", 100000) # here salary is updated from 47000 to 100000

# deletion = employees.pop(1)
# print(deletion)
# Function to delete employee
def delete_employee(index):
    if 0 <= index < len(employees):
        employees.pop(index)
        print("Employee deleted successfully!")
    else:
        print("Invalid employee index!")


delete_employee(5) 
# if index(1) output is Employee deleted successfully!
# if index(5) output is Invalid employee index!
print(employees)

"""
# OUTPUT
----- Mini Project 1: Employee Management System -----

sucessfully added
sucessfully added
sucessfully added
[{'name': 'harsha', 'age': 23, 'role': 'devops', 'salary': 47000}, {'name': 'Rahul', 'age': 25, 'role': 'Developer', 'salary': 55000}, {'name': 'hari', 'age': 22, 'role': 'Ai', 'salary': 100000}]
Employee updated successfully!
Invalid employee index!
[{'name': 'harsha', 'age': 23, 'role': 'devops', 'salary': 100000}, {'name': 'Rahul', 'age': 25, 'role': 'Developer', 'salary': 55000}, {'name': 'hari', 'age': 22, 'role': 'Ai', 'salary': 100000}]

"""
print()

print(" -----Mini Project 2: Student Report Card----- ")

print()

# Concepts: Dictionary, Functions, Formatting
# function create student
def student(name, sub1, sub2, sub3):
    return {
        "name": name,
        "sub1": sub1,
        "sub2": sub2,
        "sub3": sub3
    }


# funtion to calculate report card
def report_card(stu):
    total = stu["sub1"] +stu["sub2"] + stu["sub3"]
    average = total/3

    # caluculating for grade
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"
    
    # printing the report card format

    print("\n ---- STUDENT REPORT CARD ----")
    print("STUDENT NAME :",stu["name"])
    print("SUB 1 MARKS  :", stu["sub1"])
    print("SUB 2 MARKS  :", stu["sub2"])
    print("SUB 3 MARKS  :", stu["sub3"])
    print("TOTAL MARKS  :", total)
    print("AVERAGE      :", round(average)) # here we can't mention like points all so we used
    print("GRADE.       :", grade)

s1 = student("Harsha", 85, 88, 96)
s2 = student("Naveen", 90,91,88)
report_card(s1)
report_card(s2)


"""
------ OUTPUT------

-----Mini Project 2: Student Report Card----- 


 ---- STUDENT REPORT CARD ----
STUDENT NAME : Harsha
SUB 1 MARKS  : 85
SUB 2 MARKS  : 88
SUB 3 MARKS  : 96
TOTAL MARKS  : 269
AVERAGE      : 90
GRADE.       : A

 ---- STUDENT REPORT CARD ----
STUDENT NAME : Naveen
SUB 1 MARKS  : 90
SUB 2 MARKS  : 91
SUB 3 MARKS  : 88
TOTAL MARKS  : 269
AVERAGE      : 90
GRADE.       : A

"""

print()

print(" ----- Mini Project 3: Shopping Cart System----- ")

print()
#Concepts: List, Dictionary, Loop
# list to store items

cart = []

# function top add product to list 
def ad_product(name, price, quantity):
    item = {
        "name":name,
        "price":price,
        "quantity":quantity
    }
    cart.append(item)
    print(f"{name} added to cart!")

# function to display cart

def dis_cart():
    if not cart:
        print("cart is empty")
        return
    print("\n----- Cart Items -----")
    total = 0

    for i, item in enumerate(cart):
        item_total = item["price"] * item["quantity"]
        total += item_total

        print(f"{i}. {item['name']} | Price: {item['price']} | Qty: {item['quantity']} | Total: {item_total}")

    print("----------------------")
    print(f"Total Bill: {total}")

# Function to remove item
def remove_item(index):
    if 0 <= index < len(cart):
        removed = cart.pop(index)
        print(f"{removed['name']} removed from cart!")
    else:
        print("Invalid index!")

# Example usage

ad_product("snacks", 50000, 1)
ad_product("Mouse", 500, 2)
ad_product("Keyboard", 1500, 1)
ad_product("bottle",100,1)
dis_cart()

remove_item(1)   # removes Mouse

dis_cart()

"""
----- OUTPUT -----
----- Mini Project 3: Shopping Cart System----- 

snacks added to cart!
Mouse added to cart!
Keyboard added to cart!
bottle added to cart!

----- Cart Items -----
0. snacks | Price: 50000 | Qty: 1 | Total: 50000
1. Mouse | Price: 500 | Qty: 2 | Total: 1000
2. Keyboard | Price: 1500 | Qty: 1 | Total: 1500
3. bottle | Price: 100 | Qty: 1 | Total: 100
----------------------
Total Bill: 52600
Mouse removed from cart!

----- Cart Items -----
0. snacks | Price: 50000 | Qty: 1 | Total: 50000
1. Keyboard | Price: 1500 | Qty: 1 | Total: 1500
2. bottle | Price: 100 | Qty: 1 | Total: 100
----------------------
Total Bill: 51600

"""

print()

print("-----Mini Project 4: Login & User Validation-----")

print()

print("----- Login System -----")

# Store users (dictionary)

users = {
    "harsha": "1234",
    "rajesh": "abcd",
    "hari": "pass"
}

# Take input from users 
username = input("Enter username: ")
password = input("Enter password: ")

# Validate using condition

if username in users and users[username] == password:
    print("Login Successful ")
else:
    print("Invalid Username or Password Check Once")


"""
----- OUTPUT----

----- Mini Project 4: Login & User Validation -----

----- Login System -----
Enter username: rahul
Enter password: 1234
Invalid Username or Password Check Once

----- Login System -----
Enter username: harsha
Enter password: 1234
Login Successful 

"""

print()
print("----- Mini Project 5: Unique Visitor Counter -----")

print()

# Concepts: Set

# Set to store unique visitors
visitors = set()

# Add visitors to set
visitors.add("Harsha")
visitors.add("Rahul")
visitors.add("Hari")
visitors.add("Harsha")   # duplicate (ignored)

# Display visitors
print("Visitors:",visitors)

# Total unique visitors
print("Total Unique Visitors:",len(visitors))

"""
-----OUTPUT----

----- Mini Project 5: Unique Visitor Counter -----

Visitors: {'Harsha', 'Hari', 'Rahul'}
Total Unique Visitors: 3

"""
print()

print("----- Mini Project 6: String Formatter Tool -----")



# input from users
name = input("Enter your name: ")
product = input("Enter product name: ")

# Formatted sentence
print(f"\nHello {name}, you purchased {product} successfully!")

# Padding examples

print("Left   :", name.ljust(15))
print("Right  :", name.rjust(15))
print("Center :", name.center(15))
"""


----output----

----- Mini Project 6: String Formatter Tool -----
Enter your name: harshavardhan
Enter product name: 10

Hello harshavardhan, you purchased 10 successfully!
Left   : harshavardhan  
Right  :   harshavardhan
Center :  harshavardhan 

"""
print()
print("----- Mini Project 7: Bank Account System-----")
print()

# Concepts: Functions, Dictionary
#

accounts = {}

def create():
    name = input("Name: ")
    balance = float(input("Balance: "))
    accounts[name] = balance

def deposit():
    name = input("Name: ")
    amount = float(input("Amount: "))
    if name in accounts:
        accounts[name] += amount

def withdraw():
    name = input("Name: ")
    amount = float(input("Amount: "))
    if name in accounts and accounts[name] >= amount:
        accounts[name] -= amount

def check():
    name = input("Name: ")
    if name in accounts:
        print("Balance:", accounts[name])

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit")
    choice = input("Choice: ")

    if choice == '1':
        create()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check()
    elif choice == '5':
        break

"""
----- OUTPUT -----

----- Mini Project 7: Bank Account System-----


1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit
Choice: 1
Name: harsha
Balance: 1000

1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit
Choice: 4
Name: harsha
Balance: 1000.0

1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit
Choice: 2
Name: harsha
Amount: 1000

1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit
Choice: 4
Name: harsha
Balance: 2000.0

1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit
Choice: 5

"""

print()
print("----- Mini Project 8: Voting System----- ")

print()

#Concepts: Dictionary, Loop
# count votes for students

# Dictionary to store candidates and votes

votes = {}
 # while loop to perfom the conditions and votings and add candidates
 # here all the details will be stored in dictonary
while True:
    print("\n1.Add Candidate 2.Vote 3.Show Winner 4.Exit")
    choice = input("Choice: ")

    if choice == '1':
        name = input("Candidate name: ")
        votes[name] = 0

    elif choice == '2':
        name = input("Vote for: ")
        if name in votes:
            votes[name] += 1
        else:
            print("Candidate not found")

    elif choice == '3':
        if votes:
            winner = max(votes, key=votes.get)
            print("Winner:", winner, "Votes:", votes[winner])
        else:
            print("No candidates")

    elif choice == '4':
        break

"""
----OUTPUT----

----- Mini Project 8: Voting System----- 


1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 1
Candidate name: harsha

1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 1
Candidate name: rockey

1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 2 
Vote for: harsha

1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 2
Vote for: harsha

1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 2
Vote for: harsha

1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 2
Vote for: rockey

1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 3
Winner: harsha Votes: 3

1.Add Candidate 2.Vote 3.Show Winner 4.Exit
Choice: 4
"""

print()

print("---- Mini Project 9: Course Enrollment System-----")
print()

# list to store the data of students
students = []   

while True:
    print("\n1.Add 2.Update 3.Display 4.Exit")
    ch = input("Choice: ")

    # Add student 
    if ch == '1':
        name = input("Name: ")
        courses = input("courses : ").split(',')
        
        student = {"name": name, "courses": courses}  # dictionary
        students.append(student)  # add to list

    # Update courses
    elif ch == '2':
        name = input("Name: ")
        for s in students:
            if s["name"] == name:
                new_course = input("add course: ")
                s["courses"].append(new_course)

    # Display student
    elif ch == '3':
        name = input("Name: ")
        for s in students:
            if s["name"] == name:
                print("courses:", s["courses"])

    elif ch == '4':
        break

"""
---- OUTPUT----

---- Mini Project 9: Course Enrollment System-----


1.Add 2.Update 3.Display 4.Exit
Choice: 1
Name: harsha
courses : devops

1.Add 2.Update 3.Display 4.Exit
Choice: 1
Name: vijay 
courses : AI

1.Add 2.Update 3.Display 4.Exit
Choice: 1
Name: ricky
courses : developer

1.Add 2.Update 3.Display 4.Exit
Choice: 2
Name: harsha
add course: AI

1.Add 2.Update 3.Display 4.Exit
Choice: 3
Name: harsha
courses: ['devops', 'AI']

1.Add 2.Update 3.Display 4.Exit
Choice: 4

"""

print()

print("---- Mini Project 10: Number Utility Tool----")

print()
#Concepts: Functions, Formatting
# work with numbers

# function to convert the number entered

def convert(num):
    print("Binary:", bin(num))
    print("Octal:", oct(num))
    print("Hex:", hex(num))

def format_number(num):
    print("with commas:", f"{num:,}")

def scientific(num):
    print("scientific notation:", f"{num:.2e}")

while True:
    print("\n1.cconvert 2.format 3.scientific 4.Exit")
    ch = input("Choice: ")

    if ch == '1':
        n = int(input("enter number: "))
        convert(n)

    elif ch == '2':
        n = int(input("enter number: "))
        format_number(n)

    elif ch == '3':
        n = float(input("enter number: "))
        scientific(n)

    elif ch == '4':
        break


"""
----- OUTPUT-----

---- Mini Project 10: Number Utility Tool----


1.cconvert 2.format 3.scientific 4.Exit
Choice: 1
enter number: 10000
Binary: 0b10011100010000
Octal: 0o23420
Hex: 0x2710

1.cconvert 2.format 3.scientific 4.Exit
Choice: 2
enter number: 123456789
with commas: 123,456,789

1.cconvert 2.format 3.scientific 4.Exit
Choice: 3
enter number: 143263868
scientific notation: 1.43e+08

1.cconvert 2.format 3.scientific 4.Exit
Choice: 4
"""