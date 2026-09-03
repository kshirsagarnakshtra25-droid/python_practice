# main.py
# import calculator as calc

# print("Addition:", calc.add(20, 10))
# print("Subtraction:", calc.subtract(20, 10))
# print("Multiplication:", calc.multiply(20, 10))
# print("Division:", calc.divide(20, 10))




#2
# from message import welcome


# print("\n2. Specific Function")
# welcome()


#3
# from student import student_info
# print("\n3. Student Information")
# student_info("Nakshtra", 21, "MCA")


#4


# import calculator as calc

# print("\n4. Using Alias")

# print("Addition:", calc.add(20, 10))
# print("Multiplication:", calc.multiply(20, 10))





#5
# from calculator import cube, even_odd, square


# print("\n5. Operations Module")
# print("Square:", square(5))
# print("Cube:", cube(5))
# print("Even/Odd:", even_odd(5))








#15
# import os_module


# 15. Display Current Directory
# os_module.current_directory()


# # 16. List Files
#os_module.list_files()


# # 17. Create a Folder
# os_module.create_folder()



#20
# import calculator

# while True:

#     print("\n===== CALCULATOR =====")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")

#     choice = input("Enter choice: ")

#     if choice == "5":
#         print("Thank you")
#         break

#     if choice not in ["1", "2", "3", "4"]:
#         print("Invalid choice")
#         continue

#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))

#     if choice == "1":
#         print("Result:", calculator.add(a, b))

#     elif choice == "2":
#         print("Result:", calculator.subtract(a, b))

#     elif choice == "3":
#         print("Result:", calculator.multiply(a, b))

#     elif choice == "4":
#         print("Result:", calculator.divide(a, b))




#21
# from student import calculate_total, calculate_percentage, calculate_grade

# marks = [80, 75, 90, 85, 70]

# total = calculate_total(marks)
# percentage = calculate_percentage(marks)
# grade = calculate_grade(percentage)

# print("Total:", total)
# print("Percentage:", percentage)
# print("Grade:", grade)


#22
# from employee import employee_details, calculate_salary

# employee_details("Atharv", 101, "IT")

# salary = calculate_salary(30000, 5000, 3000)

# print("Total Salary:", salary)



#23
# import bank

# while True:

#     print("\n===== BANK =====")
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":

#         amount = float(input("Enter amount: "))
#         bank.deposit(amount)

#     elif choice == "2":

#         amount = float(input("Enter amount: "))
#         bank.withdraw(amount)

#     elif choice == "3":

#         bank.check_balance()

#     elif choice == "4":

#         print("Thank you for using the bank.")
#         break

#     else:

#         print("Invalid choice")



#24
# from authentication import register_user, login_user

# while True:

#     print("\n===== LOGIN SYSTEM =====")
#     print("1. Register")
#     print("2. Login")
#     print("3. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":

#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         register_user(username, password)

#     elif choice == "2":

#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         login_user(username, password)

#     elif choice == "3":

#         print("Thank you")
#         break

#     else:

#         print("Invalid choice")




#25
# import cart

# while True:

#     print("\n===== SHOPPING CART =====")
#     print("1. Add Product")
#     print("2. Remove Product")
#     print("3. Display Cart")
#     print("4. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":

#         name = input("Enter product name: ")
#         price = float(input("Enter price: "))

#         cart.add_product(name, price)

#     elif choice == "2":

#         name = input("Enter product name: ")

#         cart.remove_product(name)

#     elif choice == "3":

#         cart.display_cart()

#     elif choice == "4":

#         print("Thank you")
#         break

#     else:

#         print("Invalid choice")



#26
# import calculator

# print("Addition:", calculator.add(20, 10))
# print("Subtraction:", calculator.subtract(20, 10))
# print("Multiplication:", calculator.multiply(20, 10))
# print("Division:", calculator.divide(20, 10))