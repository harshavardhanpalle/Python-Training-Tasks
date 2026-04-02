# TASK 07

# Task 1: Use super() properly

print("----- Task 1: Use super() properly -----\n")


#User should have name and id
class User:
    def __init__ (self,name,id):
        self.name = name
        self.id = id

class Student(User):
    def __init__(self,name,id,dept,fees):
        super().__init__(name,id)
        self.dept = dept
        self.fees = fees


class Faculty(User):
    def __init__ (self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
    
class Tempfaculty(Faculty):
    def __init__(self,name,id,salary,duration):
        super().__init__(name,id,salary)
        self.duration = duration

#created objects for classes
s = Student("harsha",10,"csse",10000)
f = Faculty("Yash",1,50000)
tf = Tempfaculty("hari",11,300000,3)

## printing
print( s.name, s.id, s.dept, s.fees)

print(f.name, f.id, f.salary)

print(tf.name, tf.id, tf.salary, tf.duration)

"""
OUTPUT
----- Task 1: Use super() properly -----

harsha 10 csse 10000
Yash 1 50000
hari 11 300000 3

"""
print()
# Task2

print("----- Task 2: Apply Abstraction -----\n")

from abc import ABC ,abstractmethod

class AbstractUser(ABC):
    @abstractmethod
    def get_details(self):
        pass

class student(AbstractUser):

    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age= age
        #print("thankyou for comming")

    def get_details(self):
        print(self.name, self.id,self.age)

class faculty (AbstractUser):
    def __init__ (self,name,id,age,salary):
        self.name = name 
        self.id = id
        self.age= age
        self.salary = salary
    def get_details(self):
        print(self.name, self.id,self.age,self.salary)

s = student("Vardhan",10,24)
f = faculty("Vijay",22,54,1000000)

s.get_details()
f.get_details()

"""
OUTPUT

----- Task 2: Apply Abstraction -----

Vardhan 10 24
Vijay 22 54 1000000

"""


# Task 3
print()

print("----- Task 3: Sorting using key ------\n")

class Student:
    def __init__ (self,name,fees):
        self.name = name
        self.fees = fees


class Faculty:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

students = [

    Student("harsha",100000),
    Student("vicky",90000),
    Student("raj",50000),
    Student("vijay",220000) ]

facultys = [
    Faculty("vijaykumar",100000),
    Faculty("jojho",50000),
    Faculty("ricky",60000)
]


students.sort( key = lambda x : x.fees)

for s in students :
    print(s.name,s.fees)

print()

facultys.sort(key = lambda x: x.salary)

for f in facultys:
    print(f.name,f.salary)


"""
OUTPUT

----- Task 3: Sorting using key ------

raj 50000
vicky 90000
harsha 100000
vijay 220000

jojho 50000
ricky 60000
vijaykumar 100000.    

"""

#Task 4
print()

print("----- Task 4: Use map() ------ \n")

class Student:
    def __init__ (self,name,id):
        self.name = name
        self.id = id

students = [

    Student("harsha",10),
    Student("vicky",9),
    Student("raj",6),
    Student("vijay",22) ]

names = list(map(lambda s:s.name,students))
print(names)

"""
OUTPUT
----- Task 4: Use map() ------ 

['harsha', 'vicky', 'raj', 'vijay']

"""


#task 5

print()

print("----- Task 5: Use filter()----- \n")

class Student:
    def __init__ (self,name,fees):
        self.name= name
        self.fees = fees

class Faculty:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


students = [

    Student("harsha",100000),
    Student("vicky",90000),
    Student("raj",50000),
    Student("vijay",220000) ]

facultys = [
    Faculty("vijaykumar",100000),
    Faculty("jojho",50000),
    Faculty("ricky",60000)
]

 # filter function creates a lost of items for which a funtion returns True
high_fee_students = list(filter(lambda s:int(s.fees) > 50000,students))

high_salary_fact = list(filter(lambda f:int(f.salary) > 30000,facultys))


print("students with high fees")
for s in high_fee_students:
    print(s.name, s.fees)

print()

print('faculty wirh High salary')
for f in high_salary_fact:
    print(f.name,f.salary)

"""
OUTPUT 
----- Task 5: Use filter()----- 

students with high fees
harsha 100000
vicky 90000
vijay 220000

faculty wirh High salary
vijaykumar 100000
jojho 50000
ricky 60000

"""

#task  6
print()

print("-----  Task 6: Use reduce() ----- \n")

from functools import reduce

class Student:
    def __init__ (self,name,fees):
        self.name= name
        self.fees = fees

students = [

    Student("harsha",100000),
    Student("vicky",90000),
    Student("raj",50000),
    Student("vijay",220000) ]


totalfees = reduce(lambda acc ,s:acc + int(s.fees) ,students,0)

print(totalfees)

"""
OUTPUT

-----  Task 6: Use reduce() ----- 

460000

"""

# Task 7

print("----- Task 7: Higher Order Function -----\n")

class users:
    def __init__ (self,name,fees):
        self.name = name
        self.fees = fees
          
       
def process_users(user,func):
    return list(map(func, user))
# replace with  return list(filter(func, user)) to get filter operation
      
user = [
    users("harsha",10000),
    users("vicky",2000),
    users("ricky",37000) ]

print('using map() \n')
names = process_users(user, lambda u: u.name)
print(names)

"""
OUTPUT
----- Task 7: Higher Order Function -----

using map() 

['harsha', 'vicky', 'ricky']

"""
# FINAL CHALLENGE

print("\n-----  Final Challenge (Important 🔥) ----- \n \n")

 # Build a mini system:

#list to store mutiple students 
from functools import reduce

class student():
    def __init__(self,name,fees):
        self.name = name
        self.fees = fees
    def get_details(self):
        return f"{self.name} -> Fees :{self.fees}"

class Faculty:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def get_details(self):
        return f"{self.name} -> Salary :{self.salary}"

students = [

    student("harsha",100000),
    student("vicky",90000),
    student("raj",50000),
    student("vijay",220000),
    student("hari",30000),
    student("yash",40000) ]


facultys = [
    Faculty("vijaykumar",100000),
    Faculty("jojho",50000),
    Faculty("ricky",60000)
]

#All details (get_details())

print("======= THIS IS STUDENTS DEATILS =======\n")
students_details = list(map(lambda s :s.get_details(),students))
for s in students_details:
    print(s)

print("\n ======= FACULTY DETAILS ======= \n")
faculty_details = list(map(lambda f: f.get_details(),facultys))
for f in faculty_details:
    print(f)


 # sorting data

print("\n====== SORTED STUDENTS BY FEES ======\n")
sort_student = sorted(students,key = lambda s:s.fees)
for s in sort_student:
    print(s.get_details())

print("\n====== SORTED FACULTY BY SALARY ======\n")
sort_faculty = sorted(facultys ,key = lambda f: f.salary )
for f in sort_faculty:
    print(f.get_details())


#Filtered data
print("\n====== FILTER DATA (STUDENTS BY FEES ======\n")
filter_data_highfee = list(filter(lambda s: s.fees > 60000, students))
for s in filter_data_highfee:
    print(s.get_details())

print("\n====== FACULTY WITH HIGH SALARY======\n")
high_sal_faculty = list(filter(lambda f: f.salary > 50000, facultys))
for f in high_sal_faculty:
    print(f.get_details())

print("\n====== TOTAL ======")
total_fee = reduce(lambda acc ,s:acc +s.fees,students,0)
total_salary = reduce (lambda acc ,f : acc +f.salary,facultys,0)

print("\nTotal fees of students :",total_fee)
print("Total Salary of faculty :",total_salary)

# Use at least 3 functional programming concepts together
print("\n COMBIMNED FUNCTIONAL PROGRAMMING CONCEPTS TOGETHER\n")
# reduce 
# map
# filter
""" here filter executes first like fees>50000
    and then map extracts only fees
    then reduce calculates total
"""

total_highfee = reduce(lambda acc,fees: acc + fees,
               map( lambda s :s.fees,
                   filter(lambda s:s.fees> 50000,students )),0)

print("TOTAL HIGH FEE :",total_highfee)

"""
OUTPUT
-----  Final Challenge (Important 🔥) ----- 
 

======= THIS IS STUDENTS DEATILS =======

harsha -> Fees :100000
vicky -> Fees :90000
raj -> Fees :50000
vijay -> Fees :220000
hari -> Fees :30000
yash -> Fees :40000

 ======= FACULTY DETAILS ======= 

vijaykumar -> Salary :100000
jojho -> Salary :50000
ricky -> Salary :60000

====== SORTED STUDENTS BY FEES ======

hari -> Fees :30000
yash -> Fees :40000
raj -> Fees :50000
vicky -> Fees :90000
harsha -> Fees :100000
vijay -> Fees :220000

====== SORTED FACULTY BY SALARY ======

jojho -> Salary :50000
ricky -> Salary :60000
vijaykumar -> Salary :100000

====== FILTER DATA (STUDENTS BY FEES ======

harsha -> Fees :100000
vicky -> Fees :90000
vijay -> Fees :220000

====== FACULTY WITH HIGH SALARY======

vijaykumar -> Salary :100000
ricky -> Salary :60000

====== TOTAL ======

Total fees of students : 530000
Total Salary of faculty : 210000

 COMBIMNED FUNCTIONAL PROGRAMMING CONCEPTS TOGETHER

TOTAL HIGH FEE : 410000

"""