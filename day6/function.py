
# 1. Function to print "Hello Python"

# def hello_python():
#     print("Hello Python")

# hello_python()


# 2. Function that accepts a name

# def greet(name):
#     print("Hello", name)

# greet("Nakshtra")


# # 3. Function to add two numbers

# def add(a, b):
#     return a + b

# print("Addition:", add(10, 20))


# # 4. Functions for addition, subtraction, multiplication and division

# def addition(a, b):
#     return a + b

# def subtraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def division(a, b):
#     return a / b

# print("Addition:", addition(20, 10))
# print("Subtraction:", subtraction(20, 10))
# print("Multiplication:", multiplication(20, 10))
# print("Division:", division(20, 10))


# # 5. Function to check even or odd

# def even_odd(number):
#     if number % 2 == 0:
#         print(number, "is Even")
#     else:
#         print(number, "is Odd")

# even_odd(7)


# # 6. Function to check positive, negative or zero

# def check_number(number):
#     if number > 0:
#         print("Positive")
#     elif number < 0:
#         print("Negative")
#     else:
#         print("Zero")

# check_number(-5)


# # 7. Function to calculate factorial

# def factorial(number):
#     result = 1

#     for i in range(1, number + 1):
#         result = result * i

#     return result

# print("Factorial:", factorial(5))


# # 8. Function to find the largest of two numbers

# def largest(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print("Largest:", largest(25, 40))


# # 9. Function to calculate student percentage

# def percentage(marks):
#     total = sum(marks)
#     percentage = total / len(marks)
#     return percentage

# marks = [80, 75, 90, 85, 70]

# print("Student Percentage:", percentage(marks), "%")


# # 10. Function that accepts a list and returns its sum

def list_sum(numbers):
    return sum(numbers)

numbers = [10, 20, 30, 40, 50]

print("Sum of List:", list_sum(numbers))

