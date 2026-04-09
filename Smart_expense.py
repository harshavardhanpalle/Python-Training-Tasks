# --------- SMART EXPENSE MANAGER (Real-Time Project) ---------
#  --------- FINAL TASK -----------
# ---------------------------------

#Build a Smart Expense Management System using:


#Track daily expenses
#Categorize spending
#Analyze where money is going

print("----- Smart Expense Manager (Real-Time Project) ----- \n")

import mysql.connector
from functools import reduce

print("----- Smart Expense Manager -----\n")

# DB CONNECTION
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="786111888",
        database="smartexpense_db"
    )
    return conn


# ---- USER CLASS ----
# here again add tables
# PYTHON FEATURES
# 1.User creation

class User:
    def __init__(self, name):
        self.__name = name   # encapsulation

    def save(self):
        conn = connect_db()
        cursor = conn.cursor()

        sql = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(sql, (self.__name,))
        conn.commit()

        print("User inserted")


# ---- EXPENSE CLASS ----

class Expense(User):
    def __init__(self, user_id, amount, category, description, date):
        super().__init__("temp")
        self.__user_id = user_id
        self.__amount = amount
        self.__category = category
        self.__description = description
        self.__date = date

    def save(self):
        conn = connect_db()
        cursor = conn.cursor()

        sqle = """
        INSERT INTO expenses (user_id, amount, category, description, date)
        VALUES (%s,%s,%s,%s,%s)
        """

        cursor.execute(sqle, (
            self.__user_id,
            self.__amount,
            self.__category,
            self.__description,
            self.__date
        ))

        conn.commit()
        print("Expense inserted")


# ---- FUNCTIONS ----

# 1. ADD USER
def add_user():
    name = input("Enter name: ")
    user = User(name)
    user.save()


# 2. ADD EXPENSE
def add_expense():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    print("\nUsers list:")
    for u in users:
        print(u)

    uid = int(input("Enter user_id: "))
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    desc = input("Enter description: ")
    date = input("Enter date (YYYY-MM-DD): ")
    exp = Expense(uid, amount, category, desc, date)
    exp.save()


# 3. VIEW EXPENSES
def view_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    sql = """
    SELECT users.name, expenses.amount, expenses.category, expenses.description
    FROM users
    LEFT JOIN expenses ON users.user_id = expenses.user_id
    """

    cursor.execute(sql)
    rows = cursor.fetchall()
    print("\nAll Expenses:\n")
    for row in rows:
        print(row)


# 4. FILTER
def filter_expenses():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT amount, category, date FROM expenses")
    rows = cursor.fetchall()

    expenses = [
        {"amount": r[0], "category": r[1], "date": str(r[2])}
        for r in rows
    ]

    choice = input("Enter category: ")
    result = list(filter(lambda x: x["category"] == choice, expenses))
    print("\nFiltered result:")
    for r in result:
        print(r)


# 5. TOTAL
def total_expense():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM expenses")
    rows = cursor.fetchall()
    amounts = list(map(lambda x: x[0], rows))
    total = reduce(lambda a, b: a + b, amounts, 0)
    print("\nTotal Expense:", total)


# 6. CATEGORY WISE
def category_wise():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT category, amount FROM expenses")
    rows = cursor.fetchall()
    expenses = [{"category": r[0], "amount": r[1]} for r in rows]
    categories = set(map(lambda x: x["category"], expenses))

    result = {
        c: sum([x["amount"] for x in expenses if x["category"] == c])
        for c in categories
    }

    print("\nCategory wise:")
    for k, v in result.items():
        print(k, ":", v)


# 7. HIGHEST
def highest_expense():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT amount FROM expenses")
    rows = cursor.fetchall()
    amounts = [x[0] for x in rows]
    high = reduce(lambda a, b: a if a > b else b, amounts)

    print("\nHighest Expense:", high)


# 8. MONTHLY
def monthly_report():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT date, amount FROM expenses")
    rows = cursor.fetchall()

    report = {}

    for d, a in rows:
        month = str(d)[:7]
        report[month] = report.get(month, 0) + a

    print("\nMonthly report:")
    for k, v in report.items():
        print(k, ":", v)


# 9. INSIGHT
def smart_insight():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT category, amount FROM expenses")
    rows = cursor.fetchall()

    data = {}

    for c, a in rows:
        data[c] = data.get(c, 0) + a

    max_cat = max(data, key=data.get)

    print("\nInsight:")
    print("You are spending too much on", max_cat)


# ----------- MENU -----------

while True:
    print("\n------ MENU ------")
    print("1. Add User")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Filter")
    print("5. Total")
    print("6. Category Wise")
    print("7. Highest")
    print("8. Monthly")
    print("9. Insight")
    print("0. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        add_user()
    elif ch == 2:
        add_expense()
    elif ch == 3:
        view_expenses()
    elif ch == 4:
        filter_expenses()
    elif ch == 5:
        total_expense()
    elif ch == 6:
        category_wise()
    elif ch == 7:
        highest_expense()
    elif ch == 8:
        monthly_report()
    elif ch == 9:
        smart_insight()
    elif ch == 0:
        print("Exit")
        break
    else:
        print("Invalid choice")



"""

OUTPUT
----- Smart Expense Manager (Real-Time Project) ----- 

----- Smart Expense Manager -----

------ MENU ------
1. Add User
2. Add Expense
3. View Expenses
4. Filter
5. Total
6. Category Wise
7. Highest
8. Monthly
9. Insight
0. Exit
Enter choice: 3

All Expenses:

('Harsha', 999.0, 'Food', 'Lunch')
('Harsha', 500.0, 'Travel', 'Bus')
('Harsha', 2000.0, 'Food', 'something')
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
('haarsha', None, None, None)

------ MENU ------
1. Add User
2. Add Expense
3. View Expenses
4. Filter
5. Total
6. Category Wise
7. Highest
8. Monthly
9. Insight
0. Exit
Enter choice: 

"""
