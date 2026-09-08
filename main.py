# ============================================================
# PYTHON OOP PRACTICE
# Classes, Objects, Methods and Constructors
# ============================================================


# 1. Student class and object
# class Student:
#     def display(self):
#         print("Student Name:", "Nakshtra")
#         print("Age:", 21)
#         print("Course:", "MCA")


# student1 = Student()
# student1.display()


# print("\n-----------------------------")


# 2. Employee class with display() method
# class Employee:
#     def display(self):
#         print("Employee Name:", "Rahul")
#         print("Salary:", 30000)
#         print("Department:", "IT")


# employee1 = Employee()
# employee1.display()


# print("\n-----------------------------")


# # 3. Car class with start() and stop()
# class Car:
#     def start(self):
#         print("Car Started")

#     def stop(self):
#         print("Car Stopped")


# car1 = Car()
# car1.start()
# car1.stop()


# print("\n-----------------------------")


# # 4. Mobile class with call() and message()
# class Mobile:
#     def call(self):
#         print("Calling...")

#     def message(self):
#         print("Sending Message...")


# mobile1 = Mobile()
# mobile1.call()
# mobile1.message()


# print("\n-----------------------------")


# # 5. Book class with display()
# class Book:
#     def display(self):
#         print("Book Title:", "Python Programming")
#         print("Author:", "John")
#         print("Price:", 500)


# book1 = Book()
# book1.display()


# print("\n-----------------------------")


# # 6. BankAccount with deposit() and withdraw()
# class BankAccount:
#     def deposit(self):
#         print("Amount Deposited Successfully")

#     def withdraw(self):
#         print("Amount Withdrawn Successfully")


# account1 = BankAccount()
# account1.deposit()
# account1.withdraw()


# print("\n-----------------------------")


# # 7. Calculator class
# class Calculator:
#     def add(self, a, b):
#         print("Addition:", a + b)

#     def subtract(self, a, b):
#         print("Subtraction:", a - b)

#     def multiply(self, a, b):
#         print("Multiplication:", a * b)

#     def divide(self, a, b):
#         if b != 0:
#             print("Division:", a / b)
#         else:
#             print("Cannot divide by zero")


# calc1 = Calculator()

# calc1.add(10, 5)
# calc1.subtract(10, 5)
# calc1.multiply(10, 5)
# calc1.divide(10, 5)


# print("\n-----------------------------")


# # 8. College class
# class College:
#     def college_details(self):
#         print("College Name:", "GFCCT College")
#         print("City:", "Pune")
#         print("Course:", "MCA")


# college1 = College()
# college1.college_details()


# print("\n-----------------------------")


# # 9. Product class
# class Product:
#     def display(self):
#         print("Product Name:", "Laptop")
#         print("Price:", 50000)
#         print("Quantity:", 2)


# product1 = Product()
# product1.display()


# print("\n-----------------------------")


# # 10. Customer class
# class Customer:
#     def show_customer(self):
#         print("Customer Name:", "Amit")

#     def place_order(self):
#         print("Order Placed Successfully")

#     def cancel_order(self):
#         print("Order Cancelled Successfully")


# customer1 = Customer()
# customer1.show_customer()
# customer1.place_order()
# customer1.cancel_order()


# print("\n-----------------------------")


# # 11. Laptop class
# class Laptop:
#     def power_on(self):
#         print("Laptop Power ON")

#     def power_off(self):
#         print("Laptop Power OFF")


# laptop1 = Laptop()
# laptop1.power_on()
# laptop1.power_off()


# print("\n-----------------------------")


# # 12. Teacher class
# class Teacher:
#     def display_details(self):
#         print("Teacher Name:", "Bhumika")
#         print("Subject:", "Python")
#         print("Experience:", "5 Years")


# teacher1 = Teacher()
# teacher1.display_details()


# print("\n-----------------------------")


# # 13. Company class
# class Company:
#     def company_details(self):
#         print("Company Name:", "Microsoft")
#         print("Location:", "Pune")
#         print("Employees:", 500)


# company1 = Company()
# company1.company_details()


# print("\n-----------------------------")


# # 14. Movie class
# class Movie:
#     def display(self):
#         print("Movie Name:", "3 Idiots")
#         print("Actor:", "Aamir Khan")
#         print("Actress:", "Kareena Kapoor")
#         print("Rating:", 9)


# movie1 = Movie()
# movie1.display()


#print("\n============================================================")
#==================CONSTRUCTOR PROGRAMS=============================



# # 15. Student using constructor
# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Course:", self.course)


# student2 = Student("Nakshtra", 21, "MCA")
# student2.display()


# print("\n-----------------------------")


# # 16. Employee using constructor
# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def display(self):
#         print("Employee Name:", self.name)
#         print("Salary:", self.salary)
#         print("Department:", self.department)


# employee2 = Employee("Rahul", 40000, "IT")
# employee2.display()


# print("\n-----------------------------")


# # 17. Car using constructor
# class Car:
#     def __init__(self, company, model, price):
#         self.company = company
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Company:", self.company)
#         print("Model:", self.model)
#         print("Price:", self.price)


# car2 = Car("Tata", "Harrier", 1800000)
# car2.display()


# print("\n-----------------------------")


# # 18. Mobile using constructor
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)


# mobile2 = Mobile("Samsung", "S24", 70000)
# mobile2.display()


# print("\n-----------------------------")


# # 19. Book using constructor
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)


# book2 = Book("Python Basics", "James", 600)
# book2.display()


# print("\n-----------------------------")


# # 20. Product using constructor - Total Price
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         total = self.price * self.quantity
#         print("Product Name:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
#         print("Total Price:", total)


# product2 = Product("Keyboard", 1000, 3)
# product2.total_price()


# print("\n-----------------------------")


# # 21. BankAccount using constructor
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient Balance")

#     def display_balance(self):
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)


# account2 = BankAccount("Rahul", 10000)

# account2.deposit(2000)
# account2.withdraw(3000)
# account2.display_balance()


# print("\n-----------------------------")


# # 22. Rectangle - Area and Perimeter
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Area:", self.length * self.width)

#     def perimeter(self):
#         print("Perimeter:", 2 * (self.length + self.width))


# rectangle1 = Rectangle(10, 5)
# rectangle1.area()
# rectangle1.perimeter()


# print("\n-----------------------------")


# # 23. Circle - Area and Circumference
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print("Area:", 3.14 * self.radius * self.radius)

#     def circumference(self):
#         print("Circumference:", 2 * 3.14 * self.radius)


# circle1 = Circle(7)
# circle1.area()
# circle1.circumference()


# print("\n-----------------------------")


# # 24. Student - Total and Percentage
# class Student:
#     def __init__(self, name, mark1, mark2, mark3):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3

#     def result(self):
#         total = self.mark1 + self.mark2 + self.mark3
#         percentage = total / 3

#         print("Student Name:", self.name)
#         print("Total:", total)
#         print("Percentage:", percentage)


# student3 = Student("Nakshtra", 80, 85, 90)
# student3.result()


# print("\n-----------------------------")


# # 25. Employee - Annual Salary
# class Employee:
#     def __init__(self, name, monthly_salary):
#         self.name = name
#         self.monthly_salary = monthly_salary

#     def annual_salary(self):
#         annual = self.monthly_salary * 12

#         print("Employee Name:", self.name)
#         print("Monthly Salary:", self.monthly_salary)
#         print("Annual Salary:", annual)


# employee3 = Employee("Amit", 30000)
# employee3.annual_salary()


# print("\n-----------------------------")


# # 26. ShoppingCart - Total Bill
# class ShoppingCart:
#     def __init__(self, product_name, price, quantity):
#         self.product_name = product_name
#         self.price = price
#         self.quantity = quantity

#     def total_bill(self):
#         total = self.price * self.quantity

#         print("Product:", self.product_name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
#         print("Total Bill:", total)


# cart1 = ShoppingCart("Shoes", 2000, 2)
# cart1.total_bill()


# print("\n-----------------------------")


# # 27. Laptop using constructor
# class Laptop:
#     def __init__(self, brand, ram, storage, price):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price

#     def display(self):
#         print("Brand:", self.brand)
#         print("RAM:", self.ram)
#         print("Storage:", self.storage)
#         print("Price:", self.price)


# laptop2 = Laptop("HP", "16GB", "512GB SSD", 65000)
# laptop2.display()


# print("\n-----------------------------")


# # 28. Customer using constructor
# class Customer:
#     def __init__(self, customer_id, name, mobile, city):
#         self.customer_id = customer_id
#         self.name = name
#         self.mobile = mobile
#         self.city = city

#     def display(self):
#         print("Customer ID:", self.customer_id)
#         print("Name:", self.name)
#         print("Mobile:", self.mobile)
#         print("City:", self.city)


# customer2 = Customer(101, "Priya", "9876543210", "Pune")
# customer2.display()


# print("\n-----------------------------")


# # 29. Salary - HRA, DA and Gross Salary
# class Salary:
#     def __init__(self, employee_name, basic_salary):
#         self.employee_name = employee_name
#         self.basic_salary = basic_salary

#     def calculate(self):
#         hra = self.basic_salary * 0.20
#         da = self.basic_salary * 0.10
#         gross_salary = self.basic_salary + hra + da

#         print("Employee Name:", self.employee_name)
#         print("Basic Salary:", self.basic_salary)
#         print("HRA:", hra)
#         print("DA:", da)
#         print("Gross Salary:", gross_salary)


# salary1 = Salary("Rahul", 30000)
# salary1.calculate()


# print("\n-----------------------------")


# # 30. Result - Five subjects
# class Result:
#     def __init__(self, name, m1, m2, m3, m4, m5):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5

#     def calculate_result(self):
#         total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
#         percentage = total / 5

#         if (
#             self.m1 >= 35
#             and self.m2 >= 35
#             and self.m3 >= 35
#             and self.m4 >= 35
#             and self.m5 >= 35
#         ):
#             result = "PASS"
#         else:
#             result = "FAIL"

#         print("Student Name:", self.name)
#         print("Total:", total)
#         print("Percentage:", percentage)
#         print("Result:", result)


# result1 = Result("Nakshtra", 80, 75, 90, 85, 88)
# result1.calculate_result()


# print("\n-----------------------------")


# # 31. Product - Discount
# class Product:
#     def __init__(self, name, price, discount):
#         self.name = name
#         self.price = price
#         self.discount = discount

#     def final_price(self):
#         discount_amount = self.price * self.discount / 100
#         final = self.price - discount_amount

#         print("Product Name:", self.name)
#         print("Original Price:", self.price)
#         print("Discount:", self.discount, "%")
#         print("Final Price:", final)


# product3 = Product("Mobile", 30000, 10)
# product3.final_price()


# print("\n-----------------------------")


# # 32. Electricity Bill
# class ElectricityBill:
#     def __init__(self, customer_name, units):
#         self.customer_name = customer_name
#         self.units = units

#     def calculate_bill(self):

#         if self.units <= 100:
#             bill = self.units * 5

#         elif self.units <= 200:
#             bill = (100 * 5) + ((self.units - 100) * 7)

#         else:
#             bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

#         print("Customer Name:", self.customer_name)
#         print("Units Consumed:", self.units)
#         print("Electricity Bill:", bill)


# bill1 = ElectricityBill("Amit", 250)
# bill1.calculate_bill()


# print("\n-----------------------------")


# # 33. Travel
# class Travel:
#     def __init__(self, passenger_name, source, destination, ticket_price):
#         self.passenger_name = passenger_name
#         self.source = source
#         self.destination = destination
#         self.ticket_price = ticket_price

#     def display_ticket(self):
#         print("Passenger Name:", self.passenger_name)
#         print("Source:", self.source)
#         print("Destination:", self.destination)
#         print("Ticket Price:", self.ticket_price)


# travel1 = Travel("Nakshtra", "Pune", "Mumbai", 500)
# travel1.display_ticket()


# print("\n-----------------------------")


# # 34. Three Bank Accounts
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def display(self):
#         print("Account Holder:", self.name)
#         print("Balance:", self.balance)


# account1 = BankAccount("Rahul", 10000)
# account2 = BankAccount("Amit", 20000)
# account3 = BankAccount("Priya", 15000)

# account1.display()
# print()

# account2.display()
# print()

# account3.display()


# print("\n-----------------------------")


# # 35. Rectangle with methods to calculate area and perimeter
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# rectangle2 = Rectangle(20, 10)

# print("Rectangle Area:", rectangle2.area())
# print("Rectangle Perimeter:", rectangle2.perimeter())


