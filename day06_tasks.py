# ----- OOP Practice Tasks (Python)-----
# Task 1: Encapsulation (User Class)

print("----- Task 1: Encapsulation (User Class) -----")
print()
class User:
    def __init__(self,user_name,pwd):
        self.__user_name= user_name
        self.__pwd = pwd
    def set_user (self,user_name,pwd):
        self.__user_name = username
        self._pwd = pwd

        return self.__user_name,self.__pwd
    def get_user(self):
        return self.__user_name

    def register(self):
        print(f"Registering user:{self.__user_name}")
    def login(self):
        print("Logging in:" + self.__user_name)

p1 = User("john","1234455")
p1.register()
p1.login()

print()
"""
OUTPUT
----- Task 1: Encapsulation (User Class) -----

Registering user:john
Logging in:john
"""


# TASK 2
print("-----Task 2: Inheritance (User → Student, Faculty)-----")

print()

class User:
    def __init__(self,name):
        self.name = name
    def register(self):
        print(self.name,"registed successfully")
    def login(self):
        print(self.name,"login successfully")
class Student(User):
    def student_greet(self):
        print("Hello Student")

class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

class TempFaculty(Faculty):
    def tempfaculty_greet(self):
        print("Hello Temp Faculty")
    
p1=User("john")
p2=Student("Johnny")
p3=Faculty("BODDY")
p4=TempFaculty("jackey")

## calling methods
p1.register()
p1.login()
print()

## student(child class) can access from parents class (User)
p2.register() # this method is from parent class
p2.login()
p2.student_greet() # this method is from child class only
print() # this is for creating space in output

# faculty child class is taking from parent class 
p3.register()
p3.login() # this is from parent class as we did not write in child class so we take from parent classs
p3.faculty_greet()
print()

p4.register()
p4.login()
p4.faculty_greet() # this is from a parent called faculty greet
p4.tempfaculty_greet() # this is multi level inherit from parent called faculty greet

"""
OUTPUT

-----Task 2: Inheritance (User → Student, Faculty)-----

john registed successfully
john login successfully

Johnny registed successfully
Johnny login successfully
Hello Student

BODDY registed successfully
BODDY login successfully
Hello Faculty

jackey registed successfully
jackey login successfully
Hello Faculty
Hello Temp Faculty

"""
print()
# TASK 3

print("----- Task 3: Method Overriding ----- ")

class User:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(self.name,"Welcome User")
    
class Student(User):
    def greet(self):
        print("Welcome Student")

class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
# here child class provides its own implementation
# of a method that already exists in parent class (User)


student = Student("Harsha")

faculty=Faculty("Vicky")

student.greet()
faculty.greet()

"""
OUTPUT

----- Task 3: Method Overriding ----- 
Welcome Student
Welcome Faculty

"""

print()
#TASK 4
print("---- Task 4: Method Chaining ----")


#creating class user
class User:
    def __init__(self,name):
        self.name =name
    def register(self):
        print("registerd successfully")
    def login (self):
        print(self.name)
        print("logined success")
    def greet(self):
        print("enjoy everyone")

user = User("Harsha")
user.login()
user.greet()
user.register()

"""
OUTPUT
---- Task 4: Method Chaining ----
Harsha
login success
enjoy everyone
registerd successfully

"""
print()
#TASK 5
print(" ----- Task 5: Combined Task (Real-Time) -----")

print()

class User:
    users_count = 0
    def __init__(self,username,pwd):
        self.__username= username # encapsulation of data of users
        self.__pwd = pwd
        User.users_count += 1 # increment as per required
        
    def get_username(self):
        return self.__username

    
    def register(self):
        print(self.__username,"registerd successfully")
        return self 
    def login (self):
        print(self.__username,"logined success")
        return self
    def greet(self):
        print(self.__username,"Welcome User")
        return self
    
class Student(User):
    def greet(self):
        print("welcome Student")
        return self  # method overriding

class Faculty(User):
    def greet(self):
        print("Welcome faculty")
        return self

users1 = User("harsha","1234566877")

students1 = Student("rockey", "111122345")

facultys1 = Faculty("Yash", "2222232wew")

users1.greet()
users1.login()
users1.register()
print()

# mthod chaining

students1.login().greet().register()
print()

facultys1.login().greet().register()
print()

print("Total users created :",User.users_count)

"""
OUTPUT
----- Task 5: Combined Task (Real-Time) -----

harsha Welcome User
harsha logined success
harsha registerd successfully

rockey logined success
welcome Student
rockey registerd successfully

Yash logined success
Welcome faculty
Yash registerd successfully

Total users created : 3


"""