#1. Create a Student class with private __name and __marks variables. Use getter and setter methods to
#read and update them.
#-----------------------------------------------------------------------------------------------------------


# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     # Getter for name
#     def get_name(self):
#         return self.__name

#     # Setter for name
#     def set_name(self, name):
#         self.__name = name

#     # Getter for marks
#     def get_marks(self):
#         return self.__marks

#     # Setter for marks
#     def set_marks(self, marks):
#         self.__marks = marks


# # Main program
# student = Student("Nakshtra", 85)

# print("Name:", student.get_name())
# print("Marks:", student.get_marks())

# student.set_name("Rahul")
# student.set_marks(90)

# print("\nAfter updating:")
# print("Name:", student.get_name())
# print("Marks:", student.get_marks())





#2. Create an Employee class with private __salary. Allow salary changes only through a setter that rejects
#negative values.
#-----------------------------------------------------------------------------------------------------------


# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self, salary):
#         if salary >= 0:
#             self.__salary = salary
#             print("Salary updated successfully.")
#         else:
#             print("Salary cannot be negative.")


# # Main program
# employee = Employee(30000)

# print("Salary:", employee.get_salary())

# employee.set_salary(40000)
# print("Salary:", employee.get_salary())

# employee.set_salary(-5000)
# print("Salary:", employee.get_salary())



#3.Create a Person class with private __age. Create methods to set age and check whether the person is
#eligible to vote.
# class Person:
#     def __init__(self, age):
#         self.__age = age

#     def set_age(self, age):
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Age cannot be negative.")

#     def check_voting_eligibility(self):
#         if self.__age >= 18:
#             print("Person is eligible to vote.")
#         else:
#             print("Person is not eligible to vote.")


# # Main program
# person = Person(20)

# person.check_voting_eligibility()

# person.set_age(16)
# person.check_voting_eligibility()

# person.set_age(-5)



#4.Create a User class with private __email and __password. Provide methods to change the password
#only after checking the old password.
#-----------------------------------------------------------------------------------------------------------
# class User:
#     def __init__(self, email, password):
#         self.__email = email
#         self.__password = password

#     def get_email(self):
#         return self.__email

#     def change_password(self, old_password, new_password):
#         if old_password == self.__password:
#             self.__password = new_password
#             print("Password changed successfully.")
#         else:
#             print("Old password is incorrect.")


# # Main program
# user = User("user@gmail.com", "12345")

# print("Email:", user.get_email())

# user.change_password("12345", "67890")

#user.change_password("11111", "abcde")



#5.Create a Login class with private __username and __password. Add a method to validate login
#credentials.
# #-----------------------------------------------------------------------------------------------------------
# class Login:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password

#     def validate_login(self, username, password):
#         if username == self.__username and password == self.__password:
#             print("Login successful.")
#         else:
#             print("Invalid username or password.")


# # Main program
# login = Login("admin", "12345")

# login.validate_login("admin", "12345")

# login.validate_login("admin", "wrong")



#6.Create an ATM class with private __balance and __pin. Implement deposit, withdraw, and balance
#inquiry using public methods.
# class ATM:
#     def __init__(self, balance, pin):
#         self.__balance = balance
#         self.__pin = pin

#     def deposit(self, amount, pin):
#         if pin == self.__pin:
#             if amount > 0:
#                 self.__balance += amount
#                 print("Amount deposited successfully.")
#             else:
#                 print("Enter a valid amount.")
#         else:
#             print("Incorrect PIN.")

#     def withdraw(self, amount, pin):
#         if pin == self.__pin:
#             if amount > 0:
#                 if amount <= self.__balance:
#                     self.__balance -= amount
#                     print("Amount withdrawn successfully.")
#                 else:
#                     print("Insufficient balance.")
#             else:
#                 print("Enter a valid amount.")
#         else:
#             print("Incorrect PIN.")

#     def balance_inquiry(self, pin):
#         if pin == self.__pin:
#             print("Current Balance:", self.__balance)
#         else:
#             print("Incorrect PIN.")


# # Main program

# atm = ATM(10000, 1234)

# atm.balance_inquiry(1234)

# atm.deposit(2000, 1234)

# atm.balance_inquiry(1234)

# atm.withdraw(3000, 1234)

# atm.balance_inquiry(1234)

# atm.withdraw(20000, 1234)

# atm.balance_inquiry(1111)



#7.Create a ShoppingCart class with private __items and __total. Add methods to add products, remove
#products, and calculate the total.
# class ShoppingCart:
#     def __init__(self):
#         self.__items = []
#         self.__total = 0

#     def add_product(self, product, price):
#         self.__items.append(product)
#         self.__total += price

#     def remove_product(self, product, price):
#         if product in self.__items:
#             self.__items.remove(product)
#             self.__total -= price

#     def calculate_total(self):
#         print("Total:", self.__total)


# # Main program
# cart = ShoppingCart()

# cart.add_product("Laptop", 50000)
# cart.add_product("Mouse", 1000)
# cart.add_product("Keyboard", 2000)

# #cart.remove_product("Mouse", 1000)

# cart.calculate_total()




#8.Create a Vehicle class with private __fuel. Add methods refuel(), drive(), and show_fuel(). Prevent
#driving when fuel is insufficient.

# class Vehicle:
#     def __init__(self, fuel):
#         self.__fuel = fuel

#     def refuel(self, amount):
#         self.__fuel += amount

#     def drive(self, amount):
#         if amount <= self.__fuel:
#             self.__fuel -= amount
#             print("Vehicle is driving")
#         else:
#             print("Insufficient fuel")

#     def show_fuel(self):
#         print("Fuel:", self.__fuel)


# # Main program
# vehicle = Vehicle(50)

# vehicle.refuel(20)
# vehicle.drive(30)
# vehicle.show_fuel()





#9.Create a Wallet class with private __money. Add add_money() and spend_money() methods with validation.

# class Wallet:
#     def __init__(self, money):
#         self.__money = money

#     def add_money(self, amount):
#         if amount > 0:
#             self.__money += amount

#     def spend_money(self, amount):
#         if 0 < amount <= self.__money:
#             self.__money -= amount
#         else:
#             print("Invalid amount")

#     def show_money(self):
#         print("Money:", self.__money)


# wallet = Wallet(1000)
# wallet.add_money(500)
# wallet.spend_money(300)
# wallet.spend_money(100)  # Invalid amount
# wallet.show_money()





#10.Create a Salary class with private __basic_salary. Add methods to calculate HRA, DA, and gross
#salary.

# class Salary:
#     def __init__(self, basic_salary):
#         self.__basic_salary = basic_salary

#     def calculate_hra(self):
#         return self.__basic_salary * 0.20

#     def calculate_da(self):
#         return self.__basic_salary * 0.10

#     def gross_salary(self):
#         return self.__basic_salary + self.calculate_hra() + self.calculate_da()


# salary = Salary(30000)

# print("HRA:", salary.calculate_hra())
# print("DA:", salary.calculate_da())
# print("Gross Salary:", salary.gross_salary())




#11.Create a Result class with private __marks. Add a method to update marks only when the value is
#between 0 and 100.
# class Result:
#     def __init__(self, marks):
#         self.__marks = marks

#     def update_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid marks")

#     def show_marks(self):
#         print("Marks:", self.__marks)


# result = Result(80)

# result.update_marks(90)
# result.show_marks()




# 12. Contact

# class Contact:
#     def __init__(self, phone_number):
#         if len(phone_number) == 10 and phone_number.isdigit():
#             self.__phone_number = phone_number
#         else:
#             self.__phone_number = "Invalid"

#     def show_phone(self):
#         print("Phone:", self.__phone_number)


# contact = Contact("9876543210")
# contact.show_phone()


# 13. Movie

# class Movie:
#     def __init__(self, rating):
#         if 1 <= rating <= 5:
#             self.__rating = rating
#         else:
#             self.__rating = 0

#     def show_rating(self):
#         print("Rating:", self.__rating)


# movie = Movie(4)
# movie.show_rating()


# 14. Bank

# class Bank:
#     def __init__(self, interest_rate):
#         self.__interest_rate = interest_rate

#     def simple_interest(self, principal, time):
#         return (principal * self.__interest_rate * time) / 100


# bank = Bank(5)
# print("Simple Interest:", bank.simple_interest(10000, 2))


# # 15. Inventory

# class Inventory:
#     def __init__(self, quantity):
#         self.__quantity = quantity

#     def add_stock(self, quantity):
#         self.__quantity += quantity

#     def sell(self, quantity):
#         if quantity <= self.__quantity:
#             self.__quantity -= quantity
#         else:
#             print("Insufficient stock")

#     def show_quantity(self):
#         print("Quantity:", self.__quantity)


# inventory = Inventory(50)
# inventory.add_stock(20)
# inventory.sell(30)
# inventory.show_quantity()


# # 16. School

# class School:
#     def __init__(self, school_name):
#         self.__school_name = school_name
#         self.__students = []

#     def add_student(self, name):
#         self.__students.append(name)

#     def student_count(self):
#         print("Students:", len(self.__students))


# school = School("ABC School")
# school.add_student("Rahul")
# school.add_student("Rohan")
# school.add_student("Nakshtra")
# school.add_student("Atharv")
# school.student_count()


# # 17. Flight

# class Flight:
#     def __init__(self, available_seats):
#         self.__available_seats = available_seats

#     def book(self):
#         if self.__available_seats > 0:
#             self.__available_seats -= 2
#             print("Seat booked")
#         else:
#             print("No seats available")

#     def cancel(self):
#         self.__available_seats += 1
#         print("Booking cancelled")

#     def show_seats(self):
#         print("Available seats:", self.__available_seats)


# flight = Flight(5)
# flight.book()
# flight.cancel()
# flight.show_seats()


# # 18. BusTicket

# class BusTicket:
#     def __init__(self, passenger_name, fare):
#         self.__passenger_name = passenger_name
#         self.__fare = fare

#     def apply_discount(self, discount):
#         self.__fare -= self.__fare * discount / 100

#     def display_fare(self):
#         print("Passenger:", self.__passenger_name)
#         print("Final Fare:", self.__fare)


# ticket = BusTicket("Nakshtra", 500)
# ticket.apply_discount(10)
# ticket.display_fare()


# # 19. RestaurantBill

# class RestaurantBill:
#     def __init__(self):
#         self.__amount = 0

#     def add_item(self, price):
#         self.__amount += price

#     def apply_gst(self, gst):
#         self.__amount += self.__amount * gst / 100

#     def display_bill(self):
#         print("Final Bill:", self.__amount)


# bill = RestaurantBill()
# bill.add_item(500)
# bill.add_item(300)
# bill.apply_gst(5)
# bill.display_bill()



#20. Create a FreelanceProject class with private __client_name and __payment. Add a method to calculate
#payment after tax deduction.
# class FreelanceProject:
#     def __init__(self, client_name, payment):
#         self.__client_name = client_name
#         self.__payment = payment

#     def calculate_payment(self, tax):
#         final_payment = self.__payment - (self.__payment * tax / 100)
#         return final_payment
    
#     def get_client_name(self):
#         return self.__client_name

#     def show_payment(self):
#         print("Final Payment:", self.calculate_payment(10))


# project = FreelanceProject("ABC Company", 50000)


# print("Client Name:",project.get_client_name())
# project.show_payment()




#21.Create a SchoolAttendance class with private attendance percentage. Allow attendance updates only
#between 0 and 100.

# class SchoolAttendance:
#     def __init__(self, attendance):
#         self.__attendance = attendance

#     def update_attendance(self, attendance):
#         if 0 <= attendance <= 100:
#             self.__attendance = attendance
#         else:
#             print("Invalid attendance")

#     def show_attendance(self):
#         print("Attendance:", self.__attendance)


# # Main program
# student = SchoolAttendance(75)

# student.update_attendance(85)
# student.show_attendance()



#23. Create a FoodOrder class with private order total. Add items and apply coupon discounts through
#public methods.
# class FoodOrder:
#     def __init__(self):
#         self.__order_total = 0

#     def add_item(self, price):
#         self.__order_total += price

#     def apply_coupon(self, discount):
#         self.__order_total -= self.__order_total * discount / 100

#     def show_total(self):
#         print("Order Total:", self.__order_total)


# # Main program
# order = FoodOrder()

# order.add_item(200)
# order.add_item(300)

# order.apply_coupon(20)

# order.show_total()



