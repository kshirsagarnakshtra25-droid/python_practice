# ============================================================
#              PYTHON OOP PRACTICE
#       CLASS, OBJECT, INSTANCE VARIABLES,
#       INSTANCE METHODS AND SELF KEYWORD
# ============================================================


# ============================================================
#              CLASS, OBJECT & INSTANCE VARIABLES
# ============================================================


# 1. Student Class
# class Student:
#     name = "Nakshtra"
#     age = 21
#     marks = 85


# student1 = Student()

# print("----- Student Details -----")
# print("Name:", student1.name)
# print("Age:", student1.age)
# print("Marks:", student1.marks)

# print()


# 2. Employee Class
# class Employee:
#     name = "Atharv"
#     salary = 50000
#     department = "IT"


# employee1 = Employee()

# print("----- Employee Details -----")
# print("Name:", employee1.name)
# print("Salary:", employee1.salary)
# print("Department:", employee1.department)

# print()


# # 3. Car Class - Two Objects
# class Car:
#     brand = ""
#     model = ""
#     price = 0


# car1 = Car()
# car1.brand = "Tata"
# car1.model = "Sierra"
# car1.price = 1200000

# car2 = Car()
# car2.brand = "Hyundai"
# car2.model = "Creta"
# car2.price = 1800000

# print("----- Car Details -----")

# print("Car 1")
# print("Brand:", car1.brand)
# print("Model:", car1.model)
# print("Price:", car1.price)

# print()

# print("Car 2")
# print("Brand:", car2.brand)
# print("Model:", car2.model)
# print("Price:", car2.price)

# print()


# # 4. Book Class
# class Book:
#     title = "Python Programming"
#     author = "John"
#     price = 500


# book1 = Book()

# print("----- Book Details -----")
# print("Title:", book1.title)
# print("Author:", book1.author)
# print("Price:", book1.price)

# print()


# # 5. Mobile Class
# class Mobile:
#     brand = "Samsung"
#     model = "Galaxy S25"
#     price = 80000


# mobile1 = Mobile()

# print("----- Mobile Details -----")
# print("Brand:", mobile1.brand)
# print("Model:", mobile1.model)
# print("Price:", mobile1.price)

# print()


# # 6. Product Class
# class Product:
#     product_name = "Laptop"
#     price = 60000
#     quantity = 2


# product1 = Product()

# print("----- Product Details -----")
# print("Product Name:", product1.product_name)
# print("Price:", product1.price)
# print("Quantity:", product1.quantity)

# print()


# # 7. Person Class - Three Objects
# class Person:
#     name = ""
#     age = 0
#     city = ""


# person1 = Person()
# person1.name = "Rahul"
# person1.age = 22
# person1.city = "Pune"

# person2 = Person()
# person2.name = "Priya"
# person2.age = 21
# person2.city = "Mumbai"

# person3 = Person()
# person3.name = "Amit"
# person3.age = 23
# person3.city = "Kolhapur"

# print("----- Person Details -----")

# print(person1.name, person1.age, person1.city)
# print(person2.name, person2.age, person2.city)
# print(person3.name, person3.age, person3.city)

# print()


# # 8. Laptop Class
# class Laptop:
#     brand = "HP"
#     ram = "16GB"
#     storage = "512GB SSD"
#     price = 65000


# laptop1 = Laptop()

# print("----- Laptop Details -----")
# print("Brand:", laptop1.brand)
# print("RAM:", laptop1.ram)
# print("Storage:", laptop1.storage)
# print("Price:", laptop1.price)

# print()


# # 9. Movie Class
# class Movie:
#     name = "3 Idiots"
#     actor = "Aamir Khan"
#     actress = "Kareena Kapoor"
#     rating = 9


# movie1 = Movie()

# print("----- Movie Details -----")
# print("Movie:", movie1.name)
# print("Actor:", movie1.actor)
# print("Actress:", movie1.actress)
# print("Rating:", movie1.rating)

# print()


# # 10. BankAccount Class
# class BankAccount:
#     account_holder = "Nakshtra"
#     account_number = "123456789"
#     balance = 50000


# account1 = BankAccount()

# print("----- Bank Account Details -----")
# print("Account Holder:", account1.account_holder)
# print("Account Number:", account1.account_number)
# print("Balance:", account1.balance)

# print()


# # 11. Teacher Class - Two Objects
# class Teacher:
#     name = ""
#     subject = ""
#     salary = 0


# teacher1 = Teacher()
# teacher1.name = "Chetan"
# teacher1.subject = "Python"
# teacher1.salary = 45000

# teacher2 = Teacher()
# teacher2.name = "Priya"
# teacher2.subject = "Java"
# teacher2.salary = 50000

# print("----- Teacher Details -----")

# print("Teacher 1")
# print("Name:", teacher1.name)
# print("Subject:", teacher1.subject)
# print("Salary:", teacher1.salary)

# print()

# print("Teacher 2")
# print("Name:", teacher2.name)
# print("Subject:", teacher2.subject)
# print("Salary:", teacher2.salary)

# print()


# # 12. CollegeStudent Class
# class CollegeStudent:
#     name = "Nakshtra"
#     roll_no = 101
#     course = "MCA"
#     year = 1


# college_student1 = CollegeStudent()

# print("----- College Student Details -----")
# print("Name:", college_student1.name)
# print("Roll No:", college_student1.roll_no)
# print("Course:", college_student1.course)
# print("Year:", college_student1.year)

# print()


# # 13. HospitalPatient Class
# class HospitalPatient:
#     name = "Rahul"
#     age = 30
#     disease = "Fever"
#     room_no = 205


# patient1 = HospitalPatient()

# print("----- Hospital Patient Details -----")
# print("Name:", patient1.name)
# print("Age:", patient1.age)
# print("Disease:", patient1.disease)
# print("Room No:", patient1.room_no)

# print()


# # 14. Laptop Class - Five Objects
# class LaptopFive:
#     brand = ""
#     ram = ""
#     storage = ""
#     price = 0


# laptop1 = LaptopFive()
# laptop1.brand = "HP"
# laptop1.ram = "8GB"
# laptop1.storage = "512GB"
# laptop1.price = 55000

# laptop2 = LaptopFive()
# laptop2.brand = "Dell"
# laptop2.ram = "16GB"
# laptop2.storage = "512GB"
# laptop2.price = 65000

# laptop3 = LaptopFive()
# laptop3.brand = "Lenovo"
# laptop3.ram = "16GB"
# laptop3.storage = "1TB"
# laptop3.price = 70000

# laptop4 = LaptopFive()
# laptop4.brand = "Asus"
# laptop4.ram = "8GB"
# laptop4.storage = "512GB"
# laptop4.price = 60000

# laptop5 = LaptopFive()
# laptop5.brand = "Acer"
# laptop5.ram = "16GB"
# laptop5.storage = "1TB"
# laptop5.price = 75000

# print("----- Five Laptop Details -----")

# print(laptop1.brand, laptop1.ram, laptop1.storage, laptop1.price)
# print(laptop2.brand, laptop2.ram, laptop2.storage, laptop2.price)
# print(laptop3.brand, laptop3.ram, laptop3.storage, laptop3.price)
# print(laptop4.brand, laptop4.ram, laptop4.storage, laptop4.price)
# print(laptop5.brand, laptop5.ram, laptop5.storage, laptop5.price)

# print()


# # 15. Bike Class
# class Bike:
#     brand = "Royal Enfield"
#     model = "Classic 350"
#     color = "Black"
#     price = 200000


# bike1 = Bike()

# print("----- Bike Details -----")
# print("Brand:", bike1.brand)
# print("Model:", bike1.model)
# print("Color:", bike1.color)
# print("Price:", bike1.price)

# print()


# # 16. Company Class
# class Company:
#     company_name = "Microsoft"
#     location = "Hyderabad"
#     employees = 5000


# company1 = Company()

# print("----- Company Details -----")
# print("Company:", company1.company_name)
# print("Location:", company1.location)
# print("Employees:", company1.employees)

# print()


# # 17. Course Class
# class Course:
#     course_name = "Python"
#     duration = "6 Months"
#     fees = 30000


# course1 = Course()

# print("----- Course Details -----")
# print("Course:", course1.course_name)
# print("Duration:", course1.duration)
# print("Fees:", course1.fees)

# print()


# # 18. Restaurant Class
# class Restaurant:
#     name = "Food Palace"
#     location = "Pune"
#     rating = 4.5


# restaurant1 = Restaurant()

# print("----- Restaurant Details -----")
# print("Name:", restaurant1.name)
# print("Location:", restaurant1.location)
# print("Rating:", restaurant1.rating)

# print()


# # 19. Flight Class
# class Flight:
#     flight_no = "AI101"
#     source = "Mumbai"
#     destination = "Delhi"
#     price = 6000


# flight1 = Flight()

# print("----- Flight Details -----")
# print("Flight No:", flight1.flight_no)
# print("Source:", flight1.source)
# print("Destination:", flight1.destination)
# print("Price:", flight1.price)

# print()


# # 20. Hotel Class
# class Hotel:
#     name = "Taj Hotel"
#     location = "Mumbai"
#     room_type = "Deluxe"
#     price = 8000


# hotel1 = Hotel()

# print("----- Hotel Details -----")
# print("Name:", hotel1.name)
# print("Location:", hotel1.location)
# print("Room Type:", hotel1.room_type)
# print("Price:", hotel1.price)

# print()


# # ============================================================
# #                    INSTANCE METHODS
# # ============================================================


# # 21. Student - display() method
# class StudentMethod:
#     name = "Nakshtra"
#     age = 21
#     marks = 85

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Marks:", self.marks)


# student2 = StudentMethod()

# print("----- Student Display Method -----")
# student2.display()

# print()


# # 22. Employee - display_salary() method
# class EmployeeMethod:
#     salary = 50000

#     def display_salary(self):
#         print("Salary:", self.salary)


# employee2 = EmployeeMethod()

# print("----- Employee Salary -----")
# employee2.display_salary()

# print()


# # 23. Car - start() method
# class CarMethod:

#     def start(self):
#         print("Car Started")


# car3 = CarMethod()

# print("----- Car Start -----")
# car3.start()

# print()


# # 24. Mobile - call() method
# class MobileMethod:

#     def call(self):
#         print("Calling someone...")


# mobile2 = MobileMethod()

# print("----- Mobile Call -----")
# mobile2.call()

# print()


# # 25. Person - greet() method
# class PersonMethod:

#     def greet(self):
#         print("Hello, welcome!")


# person4 = PersonMethod()

# print("----- Person Greeting -----")
# person4.greet()

# print()


# # 26. BankAccount - display_balance() method
# class BankAccountMethod:
#     balance = 50000

#     def display_balance(self):
#         print("Current Balance:", self.balance)


# account2 = BankAccountMethod()

# print("----- Bank Account Balance -----")
# account2.display_balance()

# print()


# # 27. Book - display_book() method
# class BookMethod:
#     title = "Python Programming"
#     author = "John"
#     price = 500

#     def display_book(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Price:", self.price)


# book2 = BookMethod()

# print("----- Book Display -----")
# book2.display_book()

# print()


# # 28. Product - display_product() method
# class ProductMethod:
#     product_name = "Laptop"
#     price = 60000
#     quantity = 2

#     def display_product(self):
#         print("Product:", self.product_name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)


# product2 = ProductMethod()

# print("----- Product Display -----")
# product2.display_product()

# print()


# # ============================================================
# #                    SELF KEYWORD PRACTICE
# # ============================================================


# 29. Student - self.name and self.marks
# class StudentSelf:

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)


# student3 = StudentSelf()

# student3.name = "Nakshtra"
# student3.marks = 90

# print("----- Student Self Keyword -----")
# student3.display()

# print()


# # 30. Employee - self.salary
# class EmployeeSelf:

#     def display_salary(self):
#         print("Employee Salary:", self.salary)


# employee3 = EmployeeSelf()

# employee3.salary = 60000

# print("----- Employee Self Keyword -----")
# employee3.display_salary()

# print()


# # 31. Car - self.brand and self.model
# class CarSelf:

#     def display_car(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)


# car4 = CarSelf()

# car4.brand = "Tata"
# car4.model = "Harrier"

# print("----- Car Self Keyword -----")
# car4.display_car()

# print()


# # 32. Product - self.price
# class ProductSelf:

#     def total_price(self):
#         total = self.price * self.quantity
#         print("Total Price:", total)


# product3 = ProductSelf()

# product3.price = 500
# product3.quantity = 3

# print("----- Product Total Price -----")
# product3.total_price()

# print()


# # 33. Student - Hello + Name
# class StudentHello:

#     def hello(self):
#         print("Hello", self.name)


# student4 = StudentHello()

# student4.name = "Nakshtra"

# print("----- Student Hello -----")
# student4.hello()

# print()


# # 34. BankAccount - self.balance
# class BankAccountSelf:

#     def display_balance(self):
#         print("Current Balance:", self.balance)


# account3 = BankAccountSelf()

# account3.balance = 75000

# print("----- Bank Account Self Keyword -----")
# account3.display_balance()

# print()


# # 35. Book - self.title and self.author
# class BookSelf:

#     def display_book(self):
#         print("Title:", self.title)
#         print("Author:", self.author)


# book3 = BookSelf()

# book3.title = "Python Basics"
# book3.author = "Robert"

# print("----- Book Self Keyword -----")
# book3.display_book()

# print()


# # 36. Mobile - self.price
# class MobileSelf:

#     def display_price(self):
#         print("Mobile Price:", self.price)


# mobile3 = MobileSelf()

# mobile3.price = 45000

# print("----- Mobile Self Keyword -----")
# mobile3.display_price()

# print()



# ============================================================
#          MULTIPLE METHODS IN ONE CLASS
# ============================================================


# ============================================================
# 1. Calculator Class
# ============================================================

# class Calculator:

#     def add(self):
#         print("Addition:", self.a + self.b)

#     def subtract(self):
#         print("Subtraction:", self.a - self.b)

#     def multiply(self):
#         print("Multiplication:", self.a * self.b)

#     def divide(self):
#         print("Division:", self.a / self.b)


# calculator1 = Calculator()

# calculator1.a = 20
# calculator1.b = 10

# print("----- Calculator -----")
# calculator1.add()
# calculator1.subtract()
# calculator1.multiply()
# calculator1.divide()

# print()


# ============================================================
# 2. Student Class
# ============================================================

# class Student:

#     def display(self):
#         print("Name:", self.name)
#         print("Marks 1:", self.marks1)
#         print("Marks 2:", self.marks2)
#         print("Marks 3:", self.marks3)

#     def calculate_total(self):
#         total = self.marks1 + self.marks2 + self.marks3
#         print("Total Marks:", total)

#     def calculate_percentage(self):
#         total = self.marks1 + self.marks2 + self.marks3
#         percentage = total / 3
#         print("Percentage:", percentage)


# student1 = Student()

# student1.name = "Nakshtra"
# student1.marks1 = 85
# student1.marks2 = 90
# student1.marks3 = 88

# print("----- Student -----")
# student1.display()
# student1.calculate_total()
# student1.calculate_percentage()

# print()


# # ============================================================
# # 3. Employee Class
# # ============================================================

# class Employee:

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

#     def calculate_annual_salary(self):
#         annual_salary = self.salary * 12
#         print("Annual Salary:", annual_salary)

#     def calculate_bonus(self):
#         bonus = self.salary * 10 / 100
#         print("Bonus:", bonus)


# employee1 = Employee()

# employee1.name = "ADEET"
# employee1.salary = 50000

# print("----- Employee -----")
# employee1.display()
# employee1.calculate_annual_salary()
# employee1.calculate_bonus()

# print()


# # ============================================================
# # 4. BankAccount Class
# # ============================================================

# class BankAccount:

#     def deposit(self):
#         self.balance = self.balance + self.amount
#         print("Amount Deposited:", self.amount)

#     def withdraw(self):
#         if self.amount <= self.balance:
#             self.balance = self.balance - self.amount
#             print("Amount Withdrawn:", self.amount)
#         else:
#             print("Insufficient Balance")

#     def display_balance(self):
#         print("Current Balance:", self.balance)


# account1 = BankAccount()

# account1.balance = 50000

# print("----- Bank Account -----")

# account1.amount = 10000
# account1.deposit()

# account1.amount = 5000
# account1.withdraw()

# account1.display_balance()

# print()


# # ============================================================
# # 5. Rectangle Class
# # ============================================================

# class Rectangle:

#     def area(self):
#         print("Area:", self.length * self.width)

#     def perimeter(self):
#         print("Perimeter:", 2 * (self.length + self.width))

#     def display(self):
#         print("Length:", self.length)
#         print("Width:", self.width)


# rectangle1 = Rectangle()

# rectangle1.length = 10
# rectangle1.width = 5

# print("----- Rectangle -----")
# rectangle1.display()
# rectangle1.area()
# rectangle1.perimeter()

# print()


# # ============================================================
# # 6. Circle Class
# # ============================================================

# class Circle:

#     def area(self):
#         print("Area:", 3.14 * self.radius**2)

#     def circumference(self):
#         print("Circumference:", 2 * 3.14 * self.radius)

#     def display(self):
#         print("Radius:", self.radius)


# circle1 = Circle()

# circle1.radius = 7

# print("----- Circle -----")
# circle1.display()
# circle1.area()
# circle1.circumference()

# print()


# # ============================================================
# # 7. Product Class
# # ============================================================

# class Product:

#     def display(self):
#         print("Product Name:", self.product_name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)

#     def calculate_total(self):
#         total = self.price * self.quantity
#         print("Total Price:", total)

#     def apply_discount(self):
#         discount = self.price * 10 / 100
#         final_price = self.price - discount
#         print("Discount:", discount)
#         print("Price After Discount:", final_price)


# product1 = Product()

# product1.product_name = "Laptop"
# product1.price = 60000
# product1.quantity = 2

# print("----- Product -----")
# product1.display()
# product1.calculate_total()
# product1.apply_discount()



