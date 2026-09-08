# ============================================
# FILE HANDLING QUESTIONS
# ============================================

# Q1. Create demo.txt and write "Hello Python"
with open("demo.txt", "w") as file:
    file.write("Hello Python")

print(" demo.txt created successfully")


#Q2. Create student.txt and write name, age and city
name = "Nakshtra"
age = 21
city = "Kolhapur"

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + str(age) + "\n")
    file.write("City: " + city)

print(" student.txt created successfully")


# Q3. Read and display complete contents of demo.txt
with open("demo.txt", "r") as file:
    data = file.read()


print(data)


# Q4. Create a file and write 5 different messages
with open("messages.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("Welcome to programming\n")
    file.write("Python is easy\n")
    file.write("I am learning file handling\n")
    file.write("Practice makes perfect\n")

print(" 5 messages written successfully")


# Q5. Read a file line by line

with open("messages.txt", "r") as file:
    for line in file:
        print(line.strip())


# Q6. Count number of lines in a file
with open("messages.txt", "r") as file:
    lines = file.readlines()

print(" Number of lines =", len(lines))


# Q7. Count number of words in a file
with open("messages.txt", "r") as file:
    data = file.read()

words = data.split()

print(" Number of words =", len(words))


# Q8. Count number of characters in a file
with open("messages.txt", "r") as file:
    data = file.read()

print(" Number of characters =", len(data))


# Q9. Check whether a particular word exists in a file
search_word = "Python"

with open("messages.txt", "r") as file:
    data = file.read()

if search_word in data:
    print( search_word, "exists in the file")
else:
    print( search_word, "does not exist in the file")


# Q10. Display only lines containing "Python"
print("\nQ10: Lines containing Python:")

with open("messages.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())


# ============================================
# WRITE AND APPEND
# ============================================

# Q11. Create students.txt and store 5 students
with open("students.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Amit\n")
    file.write("Sneha\n")
    file.write("Rohit\n")

print(" 5 students stored successfully")


# Q12. Add a new student without deleting old data
with open("students.txt", "a") as file:
    file.write("Neha\n")

print(" New student added successfully")


# Q13. Create numbers.txt and store numbers 1 to 10
with open("numbers.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")

print(" Numbers 1 to 10 stored")


# Q14. Append numbers 11 to 20
with open("numbers.txt", "a") as file:
    for i in range(11, 21):
        file.write(str(i) + "\n")

print(" Numbers 11 to 20 appended")


# Q15. Create cities.txt and store 5 cities
with open("cities.txt", "w") as file:
    file.write("Pune\n")
    file.write("Mumbai\n")
    file.write("Kolhapur\n")
    file.write("Nashik\n")
    file.write("Nagpur\n")

# Append 3 more cities
with open("cities.txt", "a") as file:
    file.write("Delhi\n")
    file.write("Bangalore\n")
    file.write("Chennai\n")

print("Q15: Cities stored and appended successfully")


# Q16. Take student name and marks from user
student_name = input("\nQ16 - Enter student name: ")
marks = input("Enter marks: ")

with open("student_marks.txt", "w") as file:
    file.write("Name: " + student_name + "\n")
    file.write("Marks: " + marks + "\n")

print("Student details saved successfully")


# Q17. Take 5 employee names from user
with open("employees.txt", "w") as file:
    for i in range(5):
        employee = input("Enter employee name: ")
        file.write(employee + "\n")

print(" Employee names saved successfully")


# Q18. Take 5 numbers from user
with open("numbers_user.txt", "w") as file:
    for i in range(5):
        number = input("Enter number: ")
        file.write(number + "\n")

print(" Numbers saved successfully")


# ============================================
# OOPS - LEVEL 1
# ============================================

# Q19. Create Student class and one object
class Student:
    pass

student1 = Student()

print("\n Student object created")
print(student1)


# Q20. Student class with name, age and city
class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

student1 = Student("Nakshtra", 21, "Kolhapur")


print("Name:", student1.name)
print("Age:", student1.age)
print("City:", student1.city)


# Q21. Employee class
class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

employee1 = Employee("Rahul", 30000, "IT")


print("Name:", employee1.name)
print("Salary:", employee1.salary)
print("Department:", employee1.department)


# Q22. Car class
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

car1 = Car("Tata", "Harrier", 2500000)


print("Brand:", car1.brand)
print("Model:", car1.model)
print("Price:", car1.price)


# Q23. Mobile class - 3 objects
class Mobile:
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

mobile1 = Mobile("Samsung", "S24", 70000)
mobile2 = Mobile("Apple", "iPhone 15", 60000)
mobile3 = Mobile("OnePlus", "12", 50000)



print("Mobile 1:")
print(mobile1.company, mobile1.model, mobile1.price)

print("Mobile 2:")
print(mobile2.company, mobile2.model, mobile2.price)

print("Mobile 3:")
print(mobile3.company, mobile3.model, mobile3.price)


# Q24. Book class - two objects
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Python Basics", "John", 500)
book2 = Book("Learn Python", "David", 700)



print("Book 1:")
print(book1.title, book1.author, book1.price)

print("Book 2:")
print(book2.title, book2.author, book2.price)


# Q25. Product class
class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

product1 = Product("Laptop", 60000, 2)


print("Product Name:", product1.product_name)
print("Price:", product1.price)
print("Quantity:", product1.quantity)


# Q26. Employee class and 5 employee objects
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Rahul", 30000)
employee2 = Employee("Priya", 35000)
employee3 = Employee("Amit", 40000)
employee4 = Employee("Sneha", 45000)
employee5 = Employee("Rohit", 50000)



print(employee1.name, employee1.salary)
print(employee2.name, employee2.salary)
print(employee3.name, employee3.salary)
print(employee4.name, employee4.salary)
print(employee5.name, employee5.salary)


# Q27. Laptop class
class Laptop:
    def __init__(self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

laptop1 = Laptop("HP", "16GB", "Intel Core Ultra 5", 65000)


print("Brand:", laptop1.brand)
print("RAM:", laptop1.ram)
print("Processor:", laptop1.processor)
print("Price:", laptop1.price)


# Q28. BankAccount class
class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

account1 = BankAccount("Nakshtra", "1234567890", 50000)


print("Account Holder:", account1.account_holder_name)
print("Account Number:", account1.account_number)
print("Balance:", account1.balance)