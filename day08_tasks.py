#  --------- FINAL TASK -----------
# ---------------------------------
print("----- Smart Expense Manager (Real-Time Project) ----- \n")


#Build a Smart Expense Management System using:


#Track daily expenses
#Categorize spending
#Analyze where money is going


import mysql.connector
from functools import reduce

print("works well")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="786111888",
    
)

print("connected")

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS smartexpense_db")
cursor.execute("USE smartexpense_db")

# here again add tables
# PYTHON FEATURES
# 1.User creation
print("\n----- 1.User creation -----\n")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users  (
               user_id INT PRIMARY KEY AUTO_INCREMENT,
               name VARCHAR(50))""")

cursor.execute("""CREATE TABLE expenses (
    exp_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount FLOAT,
    category VARCHAR(50),
    description VARCHAR(100),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id))""")

conn.commit()
print("Database Created, Tables Created")



print()
print("\n ------ 2. Add Expense ----- \n")


sql = "INSERT INTO users (name) VALUES (%s)"
values = [("Harsha",), ("Vardhan",), ("Naven",), ("Vijay",), ("Kumar",)]

cursor.executemany(sql, values)
conn.commit()
print("User table inserted\n")
"""
 expenses for every user and 
   for every category there description why money is spent so we mentioned that 
  for every user there will be certain expenses on each category so for every one mentioned 
  their ecategory and department of spent
"""
sqle = """
INSERT INTO expenses (user_id, amount, category, description, date)
VALUES (%s, %s, %s, %s, %s)
"""
# here values are inserted in list
values = [
    # Harsha (user_id = 1)
    (1, 200, "Food", "Lunch", "2026-04-01"),
    (1, 500, "Travel", "Bus", "2026-04-02"),
    (1, 1000, "Shopping", "Clothes", "2026-04-03"),

    # Vardhan (user_id = 2)
    (2, 300, "Food", "Dinner", "2026-04-01"),
    (2, 700, "Travel", "Train", "2026-04-02"),
    (2, 1500, "Shopping", "Shoes", "2026-04-03"),

    # Naven (user_id = 3)
    (3, 250, "Food", "Snacks", "2026-04-01"),
    (3, 400, "Travel", "Auto", "2026-04-02"),
    (3, 800, "Shopping", "Accessories", "2026-04-03"),

    # Vijay (user_id = 4)
    (4, 350, "Food", "Breakfast", "2026-04-01"),
    (4, 600, "Travel", "Taxi", "2026-04-02"),
    (4, 1200, "Shopping", "Watch", "2026-04-03"),

    # Kumar (user_id = 5)
    (5, 280, "Food", "Lunch", "2026-04-01"),
    (5, 450, "Travel", "Bus", "2026-04-02"),
    (5, 900, "Shopping", "Bag", "2026-04-03"),
]

cursor.executemany(sqle, values)
conn.commit()

print("expenses inserted\n")

"""
# to see the data in tables

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print(row)



cursor.execute("SELECT * FROM expenses")

rows = cursor.fetchall()

for row in rows:
    print(row)

"""

# VIEW Expenses
print("\n ----- 3. View Expenses ----- \n")
sql = """
SELECT users.name, expenses.amount, expenses.category, expenses.description
FROM users
LEFT JOIN expenses ON users.user_id = expenses.user_id
"""

cursor.execute(sql)
rows = cursor.fetchall()

# this for seeing the view 
for row in rows:
    print(row)

# here we can't perform directly on the tabe so we converted into form of dic {key : value} 
# so this expenses we created  by this creating single dict (expense)
# we can perform all the function map ,reduce,filter, here only

cursor.execute("SELECT amount, category, date FROM expenses")
rows = cursor.fetchall()

expenses = [
    {"amount": row[0],"category": row[1], "date": str(row[2])}
    for row in rows
]


print("\n ----- 4. Filter Expenses ----- \n ")

# filter () by using category food
food_expense = list(filter(lambda x: x["category"] == "Food", expenses ))
print("Filter category(Food) :",food_expense )

print()
# filter () by using category date
By_date = list(filter(lambda x: x["date"] == "2026-04-01",expenses))
print("Filter category(date):",By_date)

print()
# list comprehension category Food
food_list = [x for x in expenses if x['category'] =='Food']
print("The listcomprehension using filter - category(Food) :")
for item in food_list:
    print(item)

print()
# list comprehension category Date
#
date_list = [x for x in expenses if x['date'] == "2026-04-02"]
print("The listcomprehension category (date):")
for i in date_list:
    print(i)

print()


# 5. Total Expense Calculation
print("----- 5. Total Expense Calculation ----- \n")

# using map
amounts = list(map(lambda x: x["amount"], expenses))

total_exp = reduce(lambda acc, x: acc+x , amounts)
print("Total Expense :",total_exp)

print()

# 6.category wise spending
print("\n ----- 6.category wise spending ----- \n ")
# here it maps all the categories in the data
categories = set(map(lambda x : x["category"] , expenses))

category_total = {
    categor: sum([x["amount"] for x in expenses if x["category"] == categor])
    for categor in categories
}
print("Category_wise spending of users:\n")
for ke ,val in category_total.items():
    print(f"{ke} : {val}")

print()


# 7 Update , Delete
# updating using sql
print("\n -----7.Delete / Update Expense -----\n")

# update
updat_query = "UPDATE expenses SET amount = %s WHERE exp_id = %s"
cursor.execute(updat_query,(999,1))
conn.commit() # conn is my mysql connection to database

print("Expense Updated")

# Delete
delete_query ="DELETE FROM expenses WHERE exp_id = %s"
cursor.execute(delete_query,(3,))
conn.commit()

print("Deleted Expense of Id 3")

# to close connection
conn.close()

"""
OUTPUT
----- Smart Expense Manager (Real-Time Project) ----- 

works well
connected

----- 1.User creation -----

Database Created, Tables Created

------ 2. Add Expense -----

expenses inserted

User table inserted


----- 3. View Expenses ----- 

('Harsha', 999.0, 'Food', 'Lunch')
('Harsha', 500.0, 'Travel', 'Bus')
('Vardhan', 300.0, 'Food', 'Dinner')
('Vardhan', 700.0, 'Travel', 'Train')
('Vardhan', 1500.0, 'Shopping', 'Shoes')
('Naven', 250.0, 'Food', 'Snacks')
('Naven', 400.0, 'Travel', 'Auto')
('Naven', 800.0, 'Shopping', 'Accessories')
('Vijay', 350.0, 'Food', 'Breakfast')
('Vijay', 600.0, 'Travel', 'Taxi')
('Vijay', 1200.0, 'Shopping', 'Watch')
('Kumar', 280.0, 'Food', 'Lunch')
('Kumar', 450.0, 'Travel', 'Bus')
('Kumar', 900.0, 'Shopping', 'Bag')

 ----- 4. Filter Expenses ----- 
 
Filter category(Food) : [{'amount': 999.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 300.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 250.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 350.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 280.0, 'category': 'Food', 'date': '2026-04-01'}]

Filter category(date): [{'amount': 999.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 300.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 250.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 350.0, 'category': 'Food', 'date': '2026-04-01'}, {'amount': 280.0, 'category': 'Food', 'date': '2026-04-01'}]

The listcomprehension using filter - category(Food) :
{'amount': 999.0, 'category': 'Food', 'date': '2026-04-01'}
{'amount': 300.0, 'category': 'Food', 'date': '2026-04-01'}
{'amount': 250.0, 'category': 'Food', 'date': '2026-04-01'}
{'amount': 350.0, 'category': 'Food', 'date': '2026-04-01'}
{'amount': 280.0, 'category': 'Food', 'date': '2026-04-01'}

The listcomprehension category (date):
{'amount': 500.0, 'category': 'Travel', 'date': '2026-04-02'}
{'amount': 700.0, 'category': 'Travel', 'date': '2026-04-02'}
{'amount': 400.0, 'category': 'Travel', 'date': '2026-04-02'}
{'amount': 600.0, 'category': 'Travel', 'date': '2026-04-02'}
{'amount': 450.0, 'category': 'Travel', 'date': '2026-04-02'}

----- 5. Total Expense Calculation ----- 

Total Expense : 9229.0


 ----- 6.category wise spending ----- 
 
Category_wise spending of users:

Travel : 2650.0
Shopping : 4400.0
Food : 2179.0


 ----- 7.Delete / Update Expense -----

Expense Updated
Deleted Expense of Id 3

## 
"""






# OOPS IMPLEMENTATION
# CREATE CLASSES user and expenses

print("----- IMPORTANT TASK ------\n")

print("OOPS Implementation ")

from abc import ABC, abstractmethod
from functools import reduce

# abstract class

class Report(ABC):
    @abstractmethod
    def report_generate(self):
        pass

#User class using encapsulation __

class User:
    def __init__(self,userid,name):
        self.__userid = userid  # encapsulation private
        self.__name = name
    def get_userid(self):
        return self.__userid
    def get_name(self):
        return self.__name

# Expense class ( we used inheritance ,method overriding,super usage)

class Expense(User):
    def __init__(self,userid,name,expenses):
        super().__init__(userid,name)   # we use super to inherit from parent class
        self._expenses = expenses       # here we are not doing encapsulation we are protecting it
    
    # method overriding
    def get_name(self):
        return super().get_name()
    def get_expenses(self):
        return self._expenses
    

# for report class is created

class Expensereport(Expense,Report):
    def __init__(self,userid,name,expenses):
        super().__init__(userid,name,expenses)

    # here monthly report data of expenses 
    def monthly_report(self):
        months_data = {}

        for expens in self._expenses:
            # here indexing to take till month only 
            # because we are calculating month wise yyyy-mm
            month = expens["date"] [:7]
            months_data[month] = months_data.get(month,0) + expens["amount"]
        return months_data
    
    # here highest expense using reduce
    def high_expense(self):
        return reduce(lambda x , y : x if x["amount"] > y["amount"] else y,self._expenses)
    
    # smart insight 
    def insight(self):
        category_total = {}

        for expens in self._expenses:
            categ = expens["category"]
            category_total[categ] = category_total.get(categ,0) + expens["amount"]

        max_category = max(category_total, key = category_total.get)

        return f"You are spending too much on {max_category} this month"
    
    #
    def report_generate(self):
        print("\n ----- Expense Report ----- \n")
        print("User :", self.get_name())
        print("\nMonthly Spending :\n")
        for ke,val in self.monthly_report().items():
            print(f"{ke} : {val}")
        
        print("\n Highest Expense :\n")
        print(self.high_expense())

        print("\n Smart Insight:\n")
        print(self.insight())


    
expenses = [
    {"amount" : 200, "category": "Food", "date": "2026-03-01"},
    {"amount": 2100, "category": "Food", "date": "2026-04-01"},
    {"amount": 1100, "category": "Travel", "date": "2026-04-02"},
    {"amount": 1000, "category": "Shopping", "date": "2026-04-03"},
    {"amount": 300, "category": "Food", "date": "2026-05-01"}
    
]

report = Expensereport(1,"harsha",expenses)
report.report_generate()

"""

OUTPUT 
----- IMPORTANT TASK ------

OOPS Implementation 

# expense report asked by trainer

 ----- Expense Report ----- 

User : harsha

Monthly Spending :

2026-03 : 200
2026-04 : 4200
2026-05 : 300

 Highest Expense :

{'amount': 2100, 'category': 'Food', 'date': '2026-04-01'}

 Smart Insight:

You are spending too much on Food this month
"""
